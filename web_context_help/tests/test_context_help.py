# -*- coding: utf-8 -*-
#
# Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
#
# License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
#
import json
import os
import shutil
import tempfile

from odoo.exceptions import AccessError, ValidationError
from odoo.modules.module import get_module_path
from odoo.tests import common, tagged

BASE = """.. help-page:: partner
   :model: res.partner
   :view: base.view_partner_form

Partner
=======

.. _usage:

Usage
-----

Write the invoice address.
"""

WHEN_COMPANY = """.. help-page:: company
   :model: res.partner
   :view-type: form
   :when: is_company = True
"""

WHEN_PERSON = """.. help-page:: person
   :model: res.partner
   :view-type: form
   :when: is_company = False
"""

WHEN_ITALIAN = """.. help-page:: italian
   :model: res.partner
   :view-type: form
   :when: country_id = base.it
"""

LIST = """.. help-page:: partner_list
   :model: res.partner.category
   :view-type: list

Partners
========

.. _search:

How to search
-------------

Type the name.

.. _wildcard:

Searching with the wildcard
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Module text replaced by the global one.

.. _footer:

Footer
------

Page created.
"""

INHERIT = """.. help-inherit:: wch_test_a.partner
   :section: usage
   :position: after

   Extra
   -----

   Additional carrier notes.
"""


@tagged("post_install", "-at_install")
class TestContextHelp(common.TransactionCase):
    def setUp(self):
        super(TestContextHelp, self).setUp()
        self.Page = self.env["context.help.page"]
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp)
        self.dir_a = self._help_dir(
            "a", {"common/partner.rst": BASE, "common/partner_list.rst": LIST}
        )
        self.dir_b = self._help_dir("b", {"common/extra.rst": INHERIT})
        self.dir_c = self._help_dir(
            "c", {"common/company.rst": WHEN_COMPANY, "common/person.rst": WHEN_PERSON}
        )
        own = os.path.join(get_module_path("web_context_help"), "help")
        self.modules = [
            ("web_context_help", own),
            ("wch_test_a", self.dir_a),
            ("wch_test_b", self.dir_b),
            ("wch_test_c", self.dir_c),
        ]

    def _help_dir(self, name, files):
        path = os.path.join(self.tmp, name, "help")
        for fn, text in files.items():
            full = os.path.join(path, fn)
            if not os.path.isdir(os.path.dirname(full)):
                os.makedirs(os.path.dirname(full))
            with open(full, "w") as fd:
                fd.write(text)
        return path

    def _rebuild(self):
        self.Page._wch_rebuild(self.modules, self.Page._wch_group())

    def test_own_pages_built(self):
        self.Page.sync_sources(force=True)
        pages = self.Page.search([("key", "=", "web_context_help.context_help_page")])
        self.assertEqual(sorted(pages.mapped("lang")), ["en_US", "it_IT"])
        en = pages.filtered(lambda p: p.lang == "en_US")
        self.assertIn("Editing a page", en.html)
        self.assertIn("Help pages", en.name)
        it = pages.filtered(lambda p: p.lang == "it_IT")
        self.assertIn("Modificare una pagina", it.html)
        self.assertTrue(en.section_ids.filtered(lambda s: s.question))
        self.assertFalse(self.Page.sync_sources())

    def test_rebuild_with_inherit(self):
        self._rebuild()
        page = self.Page.search([("key", "=", "wch_test_a.partner")])
        self.assertEqual(len(page), 1)
        self.assertEqual(page.model, "res.partner")
        html = page.html
        self.assertLess(html.index("invoice address"), html.index("carrier notes"))
        self.assertIn("extra", page.section_ids.mapped("label"))

    def test_list_global_wildcard(self):
        self._rebuild()
        page = self.Page.search(
            [("key", "=", "wch_test_a.partner_list"), ("lang", "=", "en_US")]
        )
        html = page.html
        self.assertNotIn("Module text replaced", html)
        self.assertEqual(html.count('id="wildcard"'), 1)
        self.assertLess(html.index("Type the name"), html.index("S%Maria%C%V"))
        self.assertLess(html.index("S%Maria%C%V"), html.index("Page created"))
        self.assertIn("Searching with the wildcard", page.section_ids.mapped("title"))
        # form pages do not get it
        form = self.Page.search([("key", "=", "wch_test_a.partner")])
        self.assertNotIn("S%Maria%C%V", form.html)

    def test_edit_and_source_change(self):
        self._rebuild()
        page = self.Page.search([("key", "=", "wch_test_a.partner")])
        page.html = "<p>Company text</p>"
        self.assertTrue(page.edited)
        self._rebuild()
        self.assertFalse(page.source_changed)
        self.assertEqual(page.html, "<p>Company text</p>")
        with open(os.path.join(self.dir_a, "common/partner.rst"), "a") as fd:
            fd.write("\nNew paragraph.\n")
        self._rebuild()
        self.assertTrue(page.source_changed)
        self.assertEqual(page.html, "<p>Company text</p>")
        self.assertIn("New paragraph", page.source_html)
        page.action_reset_to_source()
        self.assertFalse(page.edited)
        self.assertFalse(page.source_changed)
        self.assertIn("New paragraph", page.html)

    def test_edit_rebuilds_sections(self):
        self._rebuild()
        page = self.Page.search([("key", "=", "wch_test_a.partner")])
        page.html = (
            '<div class="section" id="extra-1"><span id="extra"></span>'
            "<h2>Extra</h2><p>kept</p></div>"
            "<h2>Videos</h2><div><br></div>"
            "<h3>Ordinary invoice</h3><div>The video shows</div>"
            "<p><video controls><source src='/x'>No video</video></p>"
        )
        titles = page.section_ids.mapped("title")
        self.assertEqual(titles, ["Extra", "Videos", "Ordinary invoice"])
        self.assertEqual(page.section_ids[0].label, "extra")
        self.assertEqual(page.section_ids[2].text, "The video shows")
        # an edited page keeps its sections on rebuild
        self._rebuild()
        self.assertIn("Ordinary invoice", page.section_ids.mapped("title"))
        page.action_reset_to_source()
        self.assertNotIn("Ordinary invoice", page.section_ids.mapped("title"))
        self.assertIn("extra", page.section_ids.mapped("label"))

    def test_removed_source(self):
        self._rebuild()
        page = self.Page.search([("key", "=", "wch_test_a.partner")])
        page.html = "<p>Company text</p>"
        self.modules = self.modules[:1]
        self._rebuild()
        self.assertFalse(page.active)
        self.assertTrue(page.exists())

    def test_copy(self):
        self._rebuild()
        page = self.Page.search([("key", "=", "wch_test_a.partner")])
        copy1 = page.copy()
        copy2 = page.copy()
        self.assertEqual(copy1.key, "wch_test_a.partner (copy)")
        self.assertEqual(copy2.key, "wch_test_a.partner (copy 2)")
        self.assertFalse(copy1.source_file)
        self.assertTrue(copy1.section_ids)
        # a copy has no source: the rebuild keeps it
        self._rebuild()
        self.assertTrue(copy1.exists() and copy1.active)

    def test_summary(self):
        self._rebuild()
        groups = dict(self.Page.summary("en_US"))
        # Grouped by module, one entry per key, the home page excluded
        self.assertEqual(
            [title for title, dummy in groups["wch_test_a"]],
            ["Partner", "Partners (list)"],
        )
        italian = dict(self.Page.summary("it_IT"))["wch_test_a"]
        self.assertIn("Partners (elenco)", dict(italian))
        self.assertIn(
            "/web_context_help/page/wch_test_a.partner?lang=en_US",
            dict(groups["wch_test_a"]).values(),
        )
        self.assertNotIn("wch_test_b", groups)
        own = [url for dummy, url in groups["Context help"]]
        self.assertFalse([url for url in own if "web_context_help.home" in url])
        self.assertTrue(self.Page.get_page("web_context_help.home", "it_IT"))

    def test_lookup(self):
        self._rebuild()
        form = self.env.ref("base.view_partner_form")
        page = self.Page.lookup(model="res.partner", view_type="form", view_id=form.id)
        self.assertEqual(page.key, "wch_test_a.partner")
        page = self.Page.lookup(model="res.partner", view_type="kanban")
        self.assertEqual(page.key, "wch_test_a.partner")
        self.assertFalse(self.Page.lookup(model="res.country", view_type="form"))
        self.Page.search([("key", "=", "wch_test_a.partner")]).view_type = "tree"
        page = self.Page.lookup(model="res.partner", view_type="list")
        self.assertEqual(page.key, "wch_test_a.partner")
        page = self.Page.lookup(
            model="context.help.page", view_type="form", lang="it_IT"
        )
        self.assertEqual(page.lang, "it_IT")
        page = self.Page.lookup(
            model="context.help.page", view_type="form", lang="fr_FR"
        )
        self.assertEqual(page.lang, "en_US")

    def test_lookup_when(self):
        self._rebuild()

        def lookup(**kw):
            return self.Page.lookup(model="res.partner", view_type="form", **kw)

        page = lookup(values={"is_company": True})
        self.assertEqual(page.key, "wch_test_c.company")
        self.assertEqual(page.when, "is_company = True")
        page = lookup(values={"is_company": False})
        self.assertEqual(page.key, "wch_test_c.person")
        # value unknown: both conditional pages skipped, the model page is used
        page = lookup()
        self.assertEqual(page.key, "wch_test_a.partner")

    def test_lookup_many2one(self):
        self.modules.append(
            ("wch_test_d", self._help_dir("d", {"common/italian.rst": WHEN_ITALIAN}))
        )
        self._rebuild()
        italy = self.env.ref("base.it")

        def lookup(values):
            return self.Page.lookup(
                model="res.partner", view_type="form", values=values
            )

        # the record id is matched by its xmlid, whatever form the client sends
        self.assertEqual(lookup({"country_id": italy.id}).key, "wch_test_d.italian")
        self.assertEqual(
            lookup({"country_id": [italy.id, "Italy"]}).key, "wch_test_d.italian"
        )
        self.assertEqual(
            lookup({"country_id": str(italy.id)}).key, "wch_test_d.italian"
        )
        fr = self.env.ref("base.fr").id
        self.assertEqual(lookup({"country_id": fr}).key, "wch_test_a.partner")
        self.assertEqual(lookup({"country_id": False}).key, "wch_test_a.partner")

    def _field(self, name):
        return self.env["ir.model.fields"]._get("res.partner", name)

    def test_rules(self):
        self._rebuild()
        Rule = self.env["context.help.rule"]
        italy = self.env.ref("base.it").id
        fr = self.env.ref("base.fr").id
        company = self.Page.search([("key", "=", "wch_test_c.company")])
        company.clear_cut = True
        rule = Rule.create(
            {"page_id": company.id, "field_id": self._field("country_id").id}
        )
        self.assertEqual(rule.condition, "country_id = False")
        self.assertEqual(rule.relation_model_id.model, "res.country")
        # the record is picked by the reference field, like the server actions
        rule.record_ref = "res.country,%d" % italy
        self.assertEqual(rule.res_id, italy)
        self.assertEqual(rule.condition, "country_id = %d" % italy)
        self.assertEqual(rule.record_ref, self.env.ref("base.it"))

        def lookup(values):
            return self.Page.lookup(
                model="res.partner", view_type="form", values=values
            )

        # the when of the source and one of the rules must be met
        self.assertEqual(
            lookup({"is_company": True, "country_id": italy}).key, "wch_test_c.company"
        )
        self.assertEqual(
            lookup({"is_company": True, "country_id": fr}).key, "wch_test_a.partner"
        )
        # rules are alternatives
        Rule.create(
            {
                "page_id": company.id,
                "field_id": self._field("type").id,
                "selection_ids": [
                    (
                        6,
                        0,
                        self._field("type")
                        .selection_ids.filtered(
                            lambda s: s.value in ("invoice", "delivery")
                        )
                        .ids,
                    )
                ],
            }
        )
        self.assertEqual(
            lookup({"is_company": True, "country_id": fr, "type": "delivery"}).key,
            "wch_test_c.company",
        )
        rule.active = False
        self.assertEqual(
            lookup({"is_company": True, "country_id": italy}).key, "wch_test_a.partner"
        )
        rule = Rule.create(
            {
                "page_id": company.id,
                "field_id": self._field("active").id,
                "operator": "!=",
                "value_boolean": True,
            }
        )
        self.assertEqual(rule.condition, "active != True")
        with self.assertRaises(ValidationError):
            Rule.create(
                {
                    "page_id": company.id,
                    "field_id": self.env["ir.model.fields"]
                    ._get("res.country", "code")
                    .id,
                }
            )
        # rules are kept by a rebuild
        self._rebuild()
        self.assertEqual(
            Rule.with_context(active_test=False).search_count(
                [("page_id", "=", company.id)]
            ),
            3,
        )

    def test_custom_page(self):
        self._rebuild()
        italy = self.env.ref("base.it").id
        values = {
            "model": "res.partner",
            "view_type": "form",
            "html": "<h2>Export</h2><p>Customs papers.</p>",
        }
        export = self.Page.create(
            dict(values, key="custom.export", name="Export", clear_cut=True)
        )
        self.Page.create(dict(values, key="custom.generic", name="Generic"))
        self.assertIn("Export", export.section_ids.mapped("title"))
        self.env["context.help.rule"].create(
            {
                "page_id": export.id,
                "field_id": self._field("country_id").id,
                "res_id": italy,
            }
        )

        def lookup(values):
            return self.Page.lookup(
                model="res.partner", view_type="form", values=values
            )

        # a page meeting a condition wins over a page without conditions
        self.assertEqual(lookup({"country_id": italy}).key, "custom.export")
        fr = self.env.ref("base.fr").id
        self.assertEqual(lookup({"country_id": fr}).key, "custom.generic")
        # no source: kept by a rebuild, nothing to reset to
        self._rebuild()
        self.assertTrue(export.exists() and export.active)
        export.write({"html": "<p>Changed</p>"})
        export.action_reset_to_source()
        self.assertEqual(export.html, "<p>Changed</p>")

    def test_priority(self):
        self._rebuild()
        standard = self.Page.search([("key", "=", "wch_test_a.partner")])
        self.assertEqual(standard.priority, 96)
        self.assertEqual(standard.copy().priority, 32)
        italy = self.env.ref("base.it").id
        values = {"model": "res.partner", "view_type": "form", "html": "<p>x</p>"}
        own = self.Page.create(dict(values, key="custom.own", name="Own", priority=50))
        values["clear_cut"] = True
        low = self.Page.create(dict(values, key="custom.low", name="Low", priority=90))
        high = self.Page.create(
            dict(values, key="custom.high", name="High", priority=10)
        )
        for page in (low, high):
            self.env["context.help.rule"].create(
                {
                    "page_id": page.id,
                    "field_id": self._field("country_id").id,
                    "res_id": italy,
                }
            )

        def lookup(values):
            return self.Page.lookup(
                model="res.partner", view_type="form", values=values
            ).key

        # pages with a rule met first, in priority order
        self.assertEqual(lookup({"country_id": italy}), "custom.high")
        high.priority = 95
        self.assertEqual(lookup({"country_id": italy}), "custom.low")
        # no rule met: the page without rules with the highest priority
        fr = self.env.ref("base.fr").id
        self.assertEqual(lookup({"country_id": fr}), "wch_test_a.partner (copy)")
        own.priority = 1
        self.assertEqual(lookup({"country_id": fr}), "custom.own")
        # a clear cut page is never the general page, even without rules
        own.clear_cut = True
        self.assertEqual(lookup({"country_id": fr}), "wch_test_a.partner (copy)")
        # the rules of a page not clear cut are ignored
        high.clear_cut = False
        self.assertEqual(lookup({"country_id": italy}), "custom.low")
        self.assertEqual(lookup({"country_id": fr}), "wch_test_a.partner (copy)")
        # Loose help: general pages from priority 64 on, the page shown excluded
        # own clear cut and 1, low clear cut and 90, high neither (95)
        self.assertTrue(own.has_loose_help() and low.has_loose_help())
        self.assertFalse(high.has_loose_help())
        self.assertFalse(standard.has_loose_help())

        def loose(values, key):
            return self.Page.lookup(
                model="res.partner", view_type="form", values=values, loose_from=key
            ).key

        # by priority: high (95) before the page of the module (96)
        self.assertEqual(loose({"country_id": italy}, "custom.low"), "custom.high")
        # pages of priority under 64 and clear cut pages are not general enough
        high.priority = 60
        self.assertEqual(
            loose({"country_id": italy}, "custom.low"), "wch_test_a.partner"
        )
        self.assertEqual(
            loose({"country_id": fr}, "wch_test_a.partner (copy)"), "wch_test_a.partner"
        )
        # the pages of the modules are the last fallback
        self.Page.search([("key", "like", "custom.%")]).unlink()
        self.Page.search([("key", "like", "% (copy)")]).unlink()
        self.assertEqual(lookup({"country_id": fr}), "wch_test_a.partner")

    def test_fields_help(self):
        items = self.Page.fields_help("context.help.page")
        self.assertIn("key", [name for name, dummy, dummy2 in items])
        self.assertEqual(self.Page.fields_help("no.such.model"), [])

    def test_ask(self):
        self._rebuild()
        res = self.Page.ask("carrier notes", {"model": "res.partner"})
        self.assertEqual(res["provider"], "_wch_ask_fulltext")
        self.assertEqual(res["results"][0]["page_key"], "wch_test_a.partner")
        self.assertIn("#extra", res["results"][0]["url"])
        res = self.Page.ask("zzzqqq", {})
        self.assertFalse(res["results"])
        self.assertFalse(self.Page.ask("  ")["results"])
        log = self.env["context.help.question"].search([], limit=2)
        self.assertEqual(log.mapped("found"), [False, True])


@tagged("post_install", "-at_install")
class TestContextHelpHttp(common.HttpCase):
    def _json(self, url, params):
        res = self.url_open(
            url,
            data=json.dumps({"jsonrpc": "2.0", "method": "call", "params": params}),
            headers={"Content-Type": "application/json"},
        )
        return res.json()["result"]

    def test_routes(self):
        self.env["context.help.page"].sync_sources(force=True)
        self.authenticate("admin", "admin")
        view = self.env.ref("web_context_help.context_help_page_form")
        res = self._json(
            "/web_context_help/lookup",
            {"model": "context.help.page", "view_type": "form", "view_id": view.id},
        )
        self.assertIn(
            "/web_context_help/page/web_context_help.context_help_page", res["url"]
        )
        url = res["url"]
        res = self.url_open(url)
        self.assertEqual(res.status_code, 200)
        self.assertIn("help_window.js", res.text)
        # FAQ and fields help on their own pages, linked by header buttons
        self.assertIn('id="wch_faq"', res.text)
        self.assertIn('id="wch_fields"', res.text)
        self.assertNotIn('id="wch_help"', res.text)
        self.assertNotIn('id="faq"', res.text)
        res = self.url_open(url + "&view=faq")
        self.assertEqual(res.status_code, 200)
        self.assertIn('id="faq"', res.text)
        self.assertNotIn("wch-auto-q", res.text)
        self.assertIn('id="wch_help"', res.text)
        self.assertNotIn('id="wch_faq"', res.text)
        res = self.url_open(url + "&view=fields")
        self.assertEqual(res.status_code, 200)
        self.assertIn('class="wch-field"', res.text)
        self.assertIn('id="wch_faq"', res.text)
        self.assertNotIn('id="wch_fields"', res.text)
        res = self.url_open(url + "&view=other")
        self.assertEqual(res.status_code, 200)
        self.assertIn('id="wch_fields"', res.text)
        res = self._json("/web_context_help/lookup", {"model": "res.country"})
        self.assertIn("/web_context_help/auto/res.country", res["url"])
        self.assertEqual(self.url_open(res["url"]).status_code, 200)
        self.assertEqual(
            self.url_open("/web_context_help/page/no.page").status_code, 404
        )
        self.assertEqual(
            self.url_open("/web_context_help/auto/no.model").status_code, 404
        )
        res = self._json("/web_context_help/ask", {"question": "rebuilt checksum"})
        self.assertTrue(res["results"])

    def test_loose_help(self):
        Page = self.env["context.help.page"]
        Page.sync_sources(force=True)
        standard = Page.search(
            [("key", "=", "web_context_help.context_help_page"), ("lang", "=", "en_US")]
        )
        own = standard.copy()
        self.authenticate("admin", "admin")
        # a page of the modules (96) has no Loose help button, an own page has
        res = self.url_open(Page.page_url(standard.key, "en_US"))
        self.assertNotIn('id="wch_loose"', res.text)
        res = self._json(
            "/web_context_help/lookup",
            {"model": "context.help.page", "view_type": "form", "lang": "en_US"},
        )
        self.assertEqual(res["key"], own.key)
        res = self.url_open(res["url"])
        self.assertIn('id="wch_loose"', res.text)
        # Loose help: the general page from priority 64 on, the own one excluded
        res = self._json(
            "/web_context_help/lookup",
            {
                "model": "context.help.page",
                "view_type": "form",
                "lang": "en_US",
                "loose_from": own.key,
            },
        )
        self.assertEqual(res["key"], standard.key)
        res = self.url_open("/web_context_help/loose/%s?lang=en_US" % own.key)
        self.assertIn("/web_context_help/page/%s" % standard.key, res.url)
        self.assertEqual(
            self.url_open("/web_context_help/loose/no.page").status_code, 404
        )

    def test_home_and_summary(self):
        self.env["context.help.page"].sync_sources(force=True)
        self.authenticate("admin", "admin")
        res = self.url_open("/web_context_help/home?lang=en_US")
        self.assertEqual(res.status_code, 200)
        self.assertIn("/web_context_help/page/web_context_help.home", res.url)
        self.assertIn('id="wch_summary"', res.text)
        self.assertNotIn('id="wch_home"', res.text)
        self.assertIn('id="wch_edit"', res.text)
        # A stray "?debug=1" after the lang keeps the language
        res = self.url_open(
            "/web_context_help/page/web_context_help.home?lang=it_IT?debug=1"
        )
        self.assertIn("Benvenuto", res.text)
        res = self.url_open("/web_context_help/summary?lang=en_US")
        self.assertEqual(res.status_code, 200)
        self.assertIn("Help summary", res.text)
        self.assertIn(
            "/web_context_help/page/web_context_help.context_help_page", res.text
        )
        self.assertIn('id="wch_home"', res.text)
        self.assertNotIn('id="wch_summary"', res.text)
        res = self.url_open(
            "/web_context_help/page/web_context_help.context_help_page?lang=en_US"
        )
        self.assertIn('id="wch_home"', res.text)
        self.assertIn('id="wch_summary"', res.text)
        # Edit is for the users allowed to change the pages
        self.env["res.users"].create(
            {
                "name": "Help reader",
                "login": "wch_reader",
                "password": "wch_reader_pwd",
                "groups_id": [(6, 0, [self.env.ref("base.group_user").id])],
            }
        )
        self.authenticate("wch_reader", "wch_reader_pwd")
        res = self.url_open("/web_context_help/home")
        self.assertEqual(res.status_code, 200)
        self.assertNotIn('id="wch_edit"', res.text)
        # a help editor, not an administrator, edits the pages
        self.env["res.users"].create(
            {
                "name": "Help editor",
                "login": "wch_editor",
                "password": "wch_editor_pwd",
                "groups_id": [
                    (6, 0, [self.env.ref("web_context_help.group_help_editor").id])
                ],
            }
        )
        self.authenticate("wch_editor", "wch_editor_pwd")
        res = self.url_open("/web_context_help/home")
        self.assertIn('id="wch_edit"', res.text)

    def test_help_editor(self):
        Page = self.env["context.help.page"]
        Page.sync_sources(force=True)
        editor_group = self.env.ref("web_context_help.group_help_editor")
        # the administrators are help editors
        self.assertIn(editor_group, self.env.ref("base.group_system").implied_ids)

        def user(login, groups):
            return self.env["res.users"].create(
                {"name": login, "login": login, "groups_id": [(6, 0, groups.ids)]}
            )

        reader = user("wch_r", self.env.ref("base.group_user"))
        editor = user("wch_e", editor_group)
        self.assertFalse(editor.has_group("base.group_system"))
        page = Page.search([("key", "=", "web_context_help.context_help_page")])[0]
        with self.assertRaises(AccessError):
            page.with_user(reader).write({"html": "<p>no</p>"})
        own = page.with_user(editor).copy()
        own.write({"html": "<h2>Mine</h2><p>text</p>", "clear_cut": True})
        self.assertTrue(own.edited)
        rule = (
            self.env["context.help.rule"]
            .with_user(editor)
            .create(
                {
                    "page_id": own.id,
                    "field_id": self.env["ir.model.fields"]
                    ._get("context.help.page", "edited")
                    .id,
                    "value_boolean": True,
                }
            )
        )
        self.assertEqual(rule.condition, "edited = True")
        self.env["context.help.question"].with_user(editor).search([])
        with self.assertRaises(AccessError):
            self.env["context.help.rule"].with_user(reader).search([])

    def test_videos(self):
        tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmp)
        os.makedirs(os.path.join(tmp, "videos", "sale"))
        for fn, data in (
            ("videos/intro.mp4", b"0123456789"),
            ("videos/sale/order.webm", b"webm"),
            ("videos/notes.txt", b"text"),
            ("secret.mp4", b"secret"),
        ):
            with open(os.path.join(tmp, fn), "wb") as fd:
                fd.write(data)
        self.env["ir.config_parameter"].sudo().set_param(
            "web_help_video_path", os.path.join(tmp, "videos")
        )
        Page = self.env["context.help.page"]
        listed = Page.video_list()
        self.assertTrue(listed["exists"])
        self.assertEqual(
            [v["name"] for v in listed["videos"]], ["intro.mp4", "sale/order.webm"]
        )
        self.assertFalse(Page.video_file("../secret.mp4"))
        self.assertFalse(Page.video_file("notes.txt"))
        self.authenticate("admin", "admin")
        res = self.url_open("/web_context_help/video/intro.mp4")
        self.assertEqual((res.status_code, res.content), (200, b"0123456789"))
        res = self.url_open(
            "/web_context_help/video/intro.mp4", headers={"Range": "bytes=2-4"}
        )
        self.assertEqual((res.status_code, res.content), (206, b"234"))
        res = self.url_open("/web_context_help/video/sale/order.webm")
        self.assertEqual(res.content, b"webm")
        res = self.url_open("/web_context_help/video/..%2Fsecret.mp4")
        self.assertEqual(res.status_code, 404)
        res = self.make_jsonrpc_request("/web_context_help/videos")
        self.assertEqual(len(res["videos"]), 2)
        # only the administrator lists the videos
        self.env["res.users"].create(
            {
                "name": "Video reader",
                "login": "wch_video",
                "password": "wch_video_pwd",
                "groups_id": [(6, 0, [self.env.ref("base.group_user").id])],
            }
        )
        self.authenticate("wch_video", "wch_video_pwd")
        res = self.url_open("/web_context_help/video/intro.mp4")
        self.assertEqual(res.status_code, 200)
        with self.assertRaises(Exception):
            self.make_jsonrpc_request("/web_context_help/videos")

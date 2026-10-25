# -*- coding: utf-8 -*-
#
# Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
#
# License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
#
import os
import shutil
import tempfile

from odoo.tests import common, tagged

from ..lib import html_page, rst_help

PAGE = """.. help-page:: partner
   :model: res.partner
   :view: base.view_partner_form, base.view_partner_tree
   :view-type: form

Partner
=======

.. help-include:: intro.rst

.. _usage:

Usage
-----

Fill :field:`Name <name>` as ``<first>.<last>`` then run :tour:`my_tour`.

.. help-question:: How to add a tag?

   Use the *Tags* field.

.. help-question::
   :auto:

Other
-----

Bye.
"""


@tagged("post_install", "-at_install")
class TestRstHelp(common.BaseCase):
    def setUp(self):
        super(TestRstHelp, self).setUp()
        self.help_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.help_dir)
        for subdir in ("common", "v16_20", "v10"):
            os.mkdir(os.path.join(self.help_dir, subdir))
        self._write("common/intro.rst", "Common **intro**.\n")
        self._write("common/intro.it_IT.rst", "Introduzione comune.\n")
        self._write("v10/intro.rst", "Intro for 10.\n")
        self._write("common/page.rst", PAGE)

    def _write(self, name, text):
        with open(os.path.join(self.help_dir, name), "w") as fd:
            fd.write(text)

    def _parse(self, group="v16_20", lang="en_US"):
        return rst_help.parse_file(
            os.path.join(self.help_dir, "common/page.rst"),
            self.help_dir,
            group,
            lang,
            fields_help=lambda model: [("name", "Name", "The name")],
        )

    def test_version_group(self):
        self.assertEqual(rst_help.version_group(10), "v10")
        self.assertEqual(rst_help.version_group(12), "v11_14")
        self.assertEqual(rst_help.version_group(15), "v15")
        self.assertEqual(rst_help.version_group(16), "v16_20")
        self.assertEqual(rst_help.version_group(21), "v16_20")
        self.assertEqual(rst_help.version_group(8), "v10")

    def test_split_lang(self):
        self.assertEqual(rst_help.split_lang("a.it_IT.rst"), ("a.rst", "it_IT"))
        self.assertEqual(rst_help.split_lang("a.rst"), ("a.rst", "en_US"))

    def test_sources_and_checksum(self):
        sources = rst_help.list_sources(self.help_dir, "v10")
        self.assertIn("v10", sources["intro.rst"])
        sources = rst_help.list_sources(self.help_dir, "v16_20")
        self.assertIn("common", sources["intro.rst"])
        before = rst_help.checksum(self.help_dir, "v16_20")
        self.assertEqual(before, rst_help.checksum(self.help_dir, "v16_20"))
        self.assertNotEqual(before, rst_help.checksum(self.help_dir, "v10"))
        self._write("v16_20/new.rst", "x\n")
        self.assertNotEqual(before, rst_help.checksum(self.help_dir, "v16_20"))

    def test_page_directives(self):
        doc = self._parse()
        self.assertEqual(doc.wch_page["name"], "partner")
        self.assertEqual(doc.wch_page["model"], "res.partner")
        self.assertEqual(
            doc.wch_page["view"], "base.view_partner_form,base.view_partner_tree"
        )
        self.assertEqual(doc.wch_page["view_type"], "form")
        # no :priority: the pages of the modules get 96 when stored
        self.assertIsNone(doc.wch_page["priority"])
        doc_priority = rst_help.parse(
            ".. help-page:: p\n   :priority: 80\n", "<t>", self.help_dir, "v16_20"
        )
        self.assertEqual(doc_priority.wch_page["priority"], 80)
        self.assertEqual(rst_help.page_title(doc, doc.wch_page), "Partner")
        html = rst_help.to_html(doc)
        self.assertIn("<strong>intro</strong>", html)
        self.assertIn('data-field="name"', html)
        self.assertIn('data-tour="my_tour"', html)
        self.assertIn("wch-question", html)
        self.assertIn("The name", html)
        self.assertIn("wch-auto-q", html)

    def test_include_group_and_lang(self):
        self.assertIn("Intro for 10", rst_help.to_html(self._parse(group="v10")))
        html = rst_help.to_html(self._parse(lang="it_IT"))
        self.assertIn("Introduzione comune", html)

    def test_include_missing(self):
        doc = rst_help.parse(
            ".. help-include:: none.rst\n", "x", self.help_dir, "v16_20"
        )
        self.assertNotIn("help-include", rst_help.to_html(doc))

    def test_inherit(self):
        inherit = rst_help.parse(
            ".. help-inherit:: a.partner\n   :section: usage\n   :position: after"
            "\n\n   Added\n   -----\n\n   extra text\n",
            "i",
            self.help_dir,
            "v16_20",
        ).wch_inherits
        self.assertEqual(len(inherit), 1)
        self.assertEqual(inherit[0]["target"], "a.partner")
        cases = {
            "after": lambda h: h.index("Usage")
            < h.index("extra text")
            < h.index("Other"),
            "before": lambda h: h.index("extra text") < h.index("Usage"),
            "replace": lambda h: "extra text" in h and "Fill" not in h,
            "remove": lambda h: "Fill" not in h and "extra text" not in h,
        }
        for position, check in cases.items():
            doc = self._parse()
            ok = rst_help.apply_inherit(
                doc,
                dict(inherit[0], position=position),
                self.help_dir,
                "v16_20",
                "en_US",
            )
            self.assertTrue(ok)
            self.assertTrue(check(rst_help.to_html(doc)), position)
        doc = self._parse()
        self.assertFalse(
            rst_help.apply_inherit(
                doc,
                dict(inherit[0], section="nothing"),
                self.help_dir,
                "v16_20",
                "en_US",
            )
        )
        rst_help.apply_inherit(
            doc, dict(inherit[0], section=""), self.help_dir, "v16_20", "en_US"
        )
        self.assertTrue(rst_help.to_html(doc).strip().endswith("</div>"))
        self.assertIn("extra text", rst_help.to_html(doc))

    def test_insert_global(self):
        glob = rst_help.parse(
            ".. _wildcard:\n\nWildcard\n~~~~~~~~\n\nUse the percent.\n",
            "g",
            self.help_dir,
            "v16_20",
        ).children[:]
        cases = {
            # no search section, no footer: at the end
            "end": (
                "nothing",
                lambda h: h.index("Bye") < h.index("percent"),
            ),
            # appended inside the search section, before the next section
            "append": (
                "usage",
                lambda h: h.index("Fill") < h.index("percent") < h.index("Bye"),
            ),
            "before": (
                "nothing",
                lambda h: h.index("percent") < h.index("Bye"),
            ),
        }
        for where, (section, check) in cases.items():
            doc = self._parse()
            fallback = "other" if where == "before" else "footer"
            self.assertEqual(
                rst_help.insert_global(doc, glob, "wildcard", section, fallback),
                where,
            )
            html = rst_help.to_html(doc)
            self.assertTrue(check(html), where)
            self.assertEqual(html.count("percent"), 1)
        # a page section with the same label is replaced
        doc = self._parse()
        rst_help.insert_global(doc, glob, "wildcard", "usage")
        self.assertEqual(
            rst_help.insert_global(doc, glob, "wildcard", "usage"), "replace"
        )
        self.assertEqual(rst_help.to_html(doc).count("percent"), 1)

    def test_sections(self):
        sections = rst_help.extract_sections(self._parse())
        labels = [s["label"] for s in sections]
        self.assertIn("usage", labels)
        usage = [s for s in sections if s["label"] == "usage" and not s["question"]]
        self.assertNotIn("<a", usage[0]["text"])
        self.assertIn("Fill Name as <first>.<last>", usage[0]["text"])
        questions = [s["question"] for s in sections if s["question"]]
        self.assertEqual(questions, ["How to add a tag?", "Name"])

    def test_version_match(self):
        self.assertEqual(rst_help.group_version("v16_20"), 16)
        self.assertEqual(rst_help.group_version("v11_14"), 11)
        for spec, yes, no in (
            ("16", (16,), (15, 17)),
            ("16-18", (16, 17, 18), (15, 19)),
            (">=17", (17, 20), (16,)),
            (">17", (18,), (17,)),
            ("<=16", (10, 16), (17,)),
            ("<17", (16,), (17,)),
            ("10, 16", (10, 16), (12, 17)),
            ("*", (10, 18), ()),
        ):
            for version in yes:
                self.assertTrue(rst_help.version_match(spec, version), (spec, version))
            for version in no:
                self.assertFalse(rst_help.version_match(spec, version), (spec, version))
        with self.assertRaises(ValueError):
            rst_help.version_match("odoo", 16)

    def test_version_blocks(self):
        text = """Page
====

.. help-version:: >=17

   New
   ---

   #. Press **Create Draft**.

.. help-version:: 16

   Only :field:`Sixteen <x>`.

Press :version:`16|**View Invoice**;17|*Draft Invoice*;*|Create Draft` now.
"""
        html = {}
        for version in (16, 17, 18):
            doc = rst_help.parse(
                text, "<t>", self.help_dir, "v16_20", version=version
            )
            html[version] = rst_help.to_html(doc)
        self.assertNotIn("Create Draft</strong>", html[16])
        self.assertIn('data-field="x"', html[16])
        self.assertIn("<strong>View Invoice</strong>", html[16])
        self.assertIn("<h2>New</h2>", html[17])
        self.assertNotIn('data-field="x"', html[17])
        self.assertIn("<em>Draft Invoice</em>", html[17])
        self.assertIn("Press Create Draft now", html[18])
        # unknown version: lowest version of the group
        doc = rst_help.parse(text, "<t>", self.help_dir, "v16_20")
        self.assertIn("View Invoice", rst_help.to_html(doc))
        self.assertNotEqual(
            rst_help.checksum(self.help_dir, "v16_20", 16),
            rst_help.checksum(self.help_dir, "v16_20", 18),
        )

    def test_when(self):
        self.assertEqual(
            rst_help.parse_when("move_type = out_invoice, in_invoice and a != b"),
            [("move_type", "=", ["out_invoice", "in_invoice"]), ("a", "!=", ["b"])],
        )
        self.assertRaises(ValueError, rst_help.parse_when, "move_type entry")
        match = rst_help.when_match
        self.assertTrue(match("", {}))
        self.assertTrue(match("move_type != entry", {"move_type": "out_invoice"}))
        self.assertFalse(match("move_type != entry", {"move_type": "entry"}))
        # a missing value never matches
        self.assertFalse(match("move_type != entry", {}))
        self.assertTrue(match("t = a, b and c = True", {"t": "b", "c": True}))
        self.assertFalse(match("t = a, b and c = True", {"t": "b", "c": False}))
        self.assertTrue(match("c = False", {"c": False}))
        # several forms of one value: id and xmlid of a many2one record
        self.assertTrue(match("p = base.it", {"p": ["7", "base.it"]}))
        self.assertTrue(match("p = 7", {"p": ["7", "base.it"]}))
        self.assertFalse(match("p != base.it", {"p": ["7", "base.it"]}))
        self.assertTrue(match("p != base.it", {"p": ["8", "base.fr"]}))
        self.assertTrue(match("p = False", {"p": []}))
        self.assertTrue(match("n = 0", {"n": 0}))
        self.assertEqual(rst_help.when_count("a = 1 and b != 2"), 2)
        self.assertEqual(rst_help.when_count(""), 0)
        doc = rst_help.parse(
            ".. help-page:: p\n   :when: move_type != entry\n",
            "<t>",
            self.help_dir,
            "v16_20",
        )
        self.assertEqual(doc.wch_page["when"], "move_type != entry")
        doc = rst_help.parse(
            ".. help-page:: p\n   :when: bad\n", "<t>", self.help_dir, "v16_20"
        )
        self.assertIsNone(doc.wch_page)

    def test_version_role_semicolon(self):
        text = "Press :version:`<17|**Edit**; then **Save**;*|nothing`."
        for version in (16, 18):
            html = rst_help.to_html(
                rst_help.parse(text, "<t>", self.help_dir, "v16_20", version=version)
            )
            self.assertIn(":version:", html)

    def test_field_role_wrapped(self):
        doc = rst_help.parse(
            "Write the :field:`delivery\naddress <partner_shipping_id>`.",
            "<t>",
            self.help_dir,
            "v16_20",
        )
        html = rst_help.to_html(doc)
        self.assertIn('data-field="partner_shipping_id">delivery address</a>', html)

    def test_html_sections(self):
        sections = html_page.extract_sections(
            '<div class="section" id="page"><h1>P</h1><p>intro</p>'
            '<div class="section" id="faq-1"><span id="faq"></span><h2>FAQ</h2>'
            '<div class="wch-question"><p class="wch-q">Why?</p>'
            '<div class="wch-a"><p>Because</p></div></div></div></div>'
            "<h2 id='v'>Videos</h2><h3>Invoice</h3><div>shown</div>"
        )
        self.assertEqual(
            [(s["label"], s["title"], s["text"]) for s in sections],
            [
                ("page", "P", "intro"),
                ("faq", "FAQ", "Why? Because"),
                ("v", "Videos", ""),
                ("", "Invoice", "shown"),
                ("faq", "Why?", "Because"),
            ],
        )
        self.assertEqual(sections[-1]["question"], "Why?")
        self.assertEqual(html_page.extract_sections(""), [])

    def test_split_faq(self):
        html = (
            '<div class="section" id="page"><h1>P</h1>\n'
            '<div class="section" id="description-1"><span id="description"></span>'
            "<h2>D</h2><p>d</p></div>\n"
            '<div class="section" id="faq-1"><span id="faq"></span>'
            '<h2>FAQ</h2><div class="wch-question"><p class="wch-q">Q?</p></div>'
            "</div>\n"
            '<div class="section" id="footer-1"><span id="footer"></span>'
            "<h2>F</h2></div></div>"
        )
        body, faq = html_page.split_faq(html)
        self.assertNotIn("Q?", body)
        self.assertIn('id="description"', body)
        self.assertIn('id="footer"', body)
        self.assertTrue(faq.startswith('<div class="section" id="faq-1">'))
        self.assertIn("Q?", faq)
        # docutils >= 0.18 writes <section>
        body, faq = html_page.split_faq(
            '<section id="faq"><h2>FAQ</h2><p>a</p></section><p>b</p>'
        )
        self.assertEqual((body, faq[:18]), ("<p>b</p>", '<section id="faq">'))
        self.assertEqual(html_page.split_faq("<p>x</p>"), ("<p>x</p>", ""))
        # questions from the fields help go to the Fields page
        body, faq = html_page.split_faq(
            '<section id="faq"><h2>FAQ</h2><div class="wch-question">Q?</div>'
            '<div class="wch-question wch-auto-q">Name</div></section>'
        )
        self.assertIn("Q?", faq)
        self.assertNotIn("Name", faq)
        body, faq = html_page.split_faq(
            '<section id="faq"><h2>FAQ</h2>'
            '<div class="wch-question wch-auto-q">Name</div></section><p>b</p>'
        )
        self.assertEqual((body, faq), ("<p>b</p>", ""))
        nav = {"fields": "/p?view=fields", "faq": "/p?lang=en_US&view=faq"}
        body = html_page.render("T", "<p/>", nav=nav)
        self.assertIn('id="wch_faq" href="/p?lang=en_US&amp;view=faq"', body)
        self.assertLess(body.index("wch_faq"), body.index("wch_fields"))
        body = html_page.render("T", "<p/>", lang="it_IT", nav={"help": "/p"})
        self.assertIn('id="wch_help" href="/p">Aiuto</a>', body)
        self.assertNotIn("wch-nav", html_page.render("T", "<p/>"))
        body = html_page.fields_body("P", [("name", "Name", "a<b")], lang="it_IT")
        self.assertIn('data-field="name"', body)
        self.assertIn("Campi di questa maschera", body)

    def test_html_page(self):
        body = html_page.render("T<", "<p>x</p>", lang="it_IT", warning=True)
        self.assertIn("T&lt;", body)
        self.assertIn("Segui Odoo", body)
        self.assertIn('id="wch_find" placeholder="Cerca nella pagina"', body)
        self.assertIn("wch-warning", body)
        # only the find previous / next buttons
        self.assertEqual(body.count("<button"), 2)
        self.assertIn('title="Occorrenza successiva"', body)
        self.assertEqual(html_page.ASK_ENABLED, "wch_ask" in body)
        self.assertRegex(body, r"help_window\.css\?v=[0-9]+")
        body = html_page.render_auto(
            "P", [("name", "Name", "a<b")], model="res.partner"
        )
        self.assertIn('data-field="name"', body)
        self.assertIn("a&lt;b", body)

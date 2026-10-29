# -*- coding: utf-8 -*-
#
# Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
#
# License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
#
import logging
import os
import re

from odoo import api, fields, models, release
from odoo.modules.module import get_module_path

from ..lib import html_page, rst_help

_logger = logging.getLogger(__name__)

RE_WORD = re.compile(r"\w{3,}", re.UNICODE)
# The web client says "list", arch and actions say "tree"
VIEW_TYPE_ALIASES = {"list": ("list", "tree"), "tree": ("list", "tree")}
# Page opened by the Help menu; the summary lists all the other pages
HOME_KEY = "web_context_help.home"
# 1 is the highest priority: the pages built from the sources of the modules
# are the last fallback, the pages of the administrator come before them
PRIORITY_DEFAULT = 32
PRIORITY_STANDARD = 96
# a clear cut page or a page of priority up to this one shows the Loose help
# button: the general pages from this priority on, e.g. the module pages
PRIORITY_LOOSE = 64
# Directory of the videos inserted in the help pages
VIDEO_PATH_PARAM = "web_help_video_path"
VIDEO_PATH_DEFAULT = "~/Video"
VIDEO_EXTS = (".mp4", ".m4v", ".webm", ".ogv", ".ogg", ".mov")


class ContextHelpSource(models.Model):
    _name = "context.help.source"
    _description = "Context help source checksum"

    module = fields.Char(required=True, index=True)
    checksum = fields.Char()

    _sql_constraints = [
        ("module_uniq", "unique(module)", "Module must be unique"),
    ]


class ContextHelpSection(models.Model):
    _name = "context.help.section"
    _description = "Context help section"
    _order = "page_id, sequence, id"

    page_id = fields.Many2one(
        "context.help.page", required=True, index=True, ondelete="cascade"
    )
    sequence = fields.Integer()
    label = fields.Char()
    title = fields.Char()
    text = fields.Text()
    question = fields.Char()


class ContextHelpPage(models.Model):
    _name = "context.help.page"
    _description = "Context help page"
    _order = "key, lang"

    key = fields.Char(required=True, index=True, help="<module>.<name>")
    name = fields.Char("Title", required=True)
    lang = fields.Char(required=True, default=rst_help.DEFAULT_LANG, index=True)
    module = fields.Char(index=True)
    # a copy has no source: it is a page of the administrator, kept by the rebuild
    source_file = fields.Char(readonly=True, copy=False)
    model = fields.Char(index=True)
    view_xmlid = fields.Char(
        "Views", help="Comma separated xmlids of the views this page explains"
    )
    view_type = fields.Char()
    when = fields.Char(
        help="Condition on the open record or the action context, e.g. "
        "move_type != entry"
    )
    source_html = fields.Html(sanitize=False, readonly=True)
    html = fields.Html("Content", sanitize=False)
    edited = fields.Boolean(
        readonly=True, help="Content was changed by an administrator"
    )
    source_changed = fields.Boolean(
        readonly=True,
        copy=False,
        help="Source changed after the content was edited by an administrator",
    )
    section_ids = fields.One2many("context.help.section", "page_id", "Sections")
    rule_ids = fields.One2many(
        "context.help.rule",
        "page_id",
        "Rules",
        help="Conditions set by the administrator: the page is shown when the "
        "open record meets one of them",
    )
    priority = fields.Integer(
        default=PRIORITY_DEFAULT,
        copy=False,
        help="1 is the highest. Pages with rules are checked first, in priority "
        "order: the first one with a rule met is shown. Otherwise the page "
        "without rules with the highest priority is shown. Pages built from "
        "the modules have priority %d, so they are the last fallback"
        % PRIORITY_STANDARD,
    )
    clear_cut = fields.Boolean(
        "Clear cut",
        help="Page shown only when one of its rules is met, e.g. the help of an "
        "order type. A page not clear cut is a general page: its rules are "
        "ignored and it is shown when no rule of a clear cut page is met",
    )
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ("key_lang_uniq", "unique(key, lang)", "Page key must be unique per language"),
    ]

    # ------------------------------------------------------------------
    # Admin editing
    # ------------------------------------------------------------------
    @api.model_create_multi
    def create(self, vals_list):
        pages = super(ContextHelpPage, self).create(vals_list)
        # a page created by the administrator has no source: its sections
        # come from its content
        if not self.env.context.get("wch_sync"):
            for page in pages:
                page._wch_set_sections(html_page.extract_sections(page.html))
        return pages

    def write(self, vals):
        if "html" in vals and not self.env.context.get("wch_sync"):
            vals = dict(vals, edited=True)
        res = super(ContextHelpPage, self).write(vals)
        if "html" in vals and not self.env.context.get("wch_sync"):
            for page in self:
                page._wch_set_sections(html_page.extract_sections(page.html))
        return res

    def copy_data(self, default=None):
        """The copy key ends with " (copy)", the key being unique per language"""
        vals_list = super().copy_data(default=default)
        if default and "key" in default:
            return vals_list
        for page, vals in zip(self, vals_list):
            key = "%s (copy)" % page.key
            n = 1
            while self.with_context(active_test=False).search_count(
                [("key", "=", key), ("lang", "=", vals.get("lang", page.lang))]
            ):
                n += 1
                key = "%s (copy %d)" % (page.key, n)
            vals["key"] = key
        return vals_list

    def _wch_set_sections(self, sections):
        """Replace the sections used by the full-text search"""
        self.ensure_one()
        self.section_ids.unlink()
        for seq, section in enumerate(sections):
            self.env["context.help.section"].create(
                dict(section, page_id=self.id, sequence=seq)
            )

    def has_loose_help(self):
        """Loose help button: the page is clear cut or of high priority"""
        self.ensure_one()
        return self.clear_cut or self.priority <= PRIORITY_LOOSE

    def action_reset_to_source(self):
        # a page created by the administrator has no source to go back to
        for page in self.filtered("source_file"):
            page.with_context(wch_sync=True).write(
                {"html": page.source_html, "edited": False, "source_changed": False}
            )
            page._wch_set_sections(html_page.extract_sections(page.html))
        return True

    def action_source_seen(self):
        return self.write({"source_changed": False})

    def action_rebuild(self):
        self.sudo().sync_sources(force=True)
        return True

    def action_open(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_url",
            "url": self.page_url(self.key, self.lang),
            "target": "new",
        }

    @api.model
    def page_url(self, key, lang=None, view=None):
        """URL of a page; view: "faq" or "fields" for its FAQ or Fields page"""
        url = "/web_context_help/page/%s" % key
        params = ["lang=%s" % lang] if lang else []
        if view:
            params.append("view=%s" % view)
        return "%s?%s" % (url, "&".join(params)) if params else url

    @api.model
    def edit_url(self, page):
        """URL of the backend form of a page"""
        return "/odoo/action-web_context_help.action_context_help_page/%s" % page.id

    @api.model
    def summary(self, lang=None):
        """[(module title, [(page title, url)])] of the pages of every installed
        help module, the home page excluded; sorted by title. The title ends
        with the view type of the page: Invoices (list), Invoice (form)"""
        lang = lang or self.env.context.get("lang") or rst_help.DEFAULT_LANG
        by_key = {}
        for page in self.search([("key", "!=", HOME_KEY)]):
            by_key.setdefault(page.key, self.browse())
            by_key[page.key] |= page
        tr = html_page.labels(lang)
        by_module = {}
        for key, pages in by_key.items():
            page = self._wch_best_lang(pages, lang)
            title = page.name
            # A model has a list page and a form page with the same title
            view_type = "list" if page.view_type == "tree" else page.view_type
            if tr.get("view_%s" % view_type):
                title = "%s (%s)" % (title, tr["view_%s" % view_type])
            by_module.setdefault(page.module or "", []).append(
                (title, self.page_url(key, lang))
            )
        Module = self._wch_with_lang(lang).env["ir.module.module"].sudo()
        titles = {
            m.name: m.shortdesc or m.name
            for m in Module.search([("name", "in", list(by_module))])
        }
        return sorted(
            (
                (titles.get(name, name), sorted(pages, key=lambda p: p[0].lower()))
                for name, pages in by_module.items()
            ),
            key=lambda group: group[0].lower(),
        )

    # ------------------------------------------------------------------
    # Lookup
    # ------------------------------------------------------------------
    @api.model
    def _wch_view_xmlid(self, view_id):
        if not view_id:
            return False
        data = (
            self.env["ir.model.data"]
            .sudo()
            .search(
                [("model", "=", "ir.ui.view"), ("res_id", "=", int(view_id))], limit=1
            )
        )
        return "%s.%s" % (data.module, data.name) if data else False

    @api.model
    def _wch_when_values(self, model, values, names):
        """values with the many2one fields of model among names turned into
        [id, xmlid, ...], so a condition can name the record by id or xmlid"""
        values = dict(values or {})
        if not model or model not in self.env:
            return values
        model_fields = self.env[model]._fields
        by_comodel = {}
        for name in names:
            field = model_fields.get(name)
            if name not in values or not field or field.type != "many2one":
                continue
            value = values[name]
            if isinstance(value, (list, tuple)):
                value = value[0] if value else False
            if isinstance(value, str) and value.isdigit():
                value = int(value)
            if isinstance(value, bool) or not isinstance(value, int) or not value:
                values[name] = False
                continue
            values[name] = [str(value)]
            by_comodel.setdefault(field.comodel_name, {}).setdefault(value, []).append(
                name
            )
        Data = self.env["ir.model.data"].sudo()
        for comodel, ids in by_comodel.items():
            for data in Data.search(
                [("model", "=", comodel), ("res_id", "in", list(ids))]
            ):
                for name in ids[data.res_id]:
                    values[name].append("%s.%s" % (data.module, data.name))
        return values

    @api.model
    def lookup(
        self,
        model=None,
        view_type=None,
        view_id=None,
        lang=None,
        values=None,
        loose_from=None,
    ):
        """Return the page matching the Odoo context, or an empty recordset.

        Candidates: the pages of the view xmlid, of model + view_type and of
        the model alone. A page whose ``when`` condition fails on ``values``
        is skipped (see rst_help.when_match). The clear cut pages come first,
        in priority order (1 is the highest): the first one with a rule
        (context.help.rule) met wins. Otherwise the general page (not clear
        cut, its rules ignored) with the highest priority wins: the pages of
        the administrator
        (default 32) come before the pages of the modules (96), the last
        fallback. Same priority: the more specific page wins (view xmlid,
        then view_type, then model), then the one meeting more ``when``
        conditions.

        loose_from: key of the page shown, for its Loose help button: only
        the general pages of priority PRIORITY_LOOSE or lower (number from 64
        up), that page excluded."""
        lang = lang or self.env.context.get("lang") or rst_help.DEFAULT_LANG
        xmlid = self._wch_view_xmlid(view_id)
        Rule = self.env["context.help.rule"].sudo()

        # level of each candidate page: 0 view xmlid, 1 view type, 2 model
        level = {}
        if xmlid:
            for page in self.search([("view_xmlid", "ilike", xmlid)]):
                if xmlid in (page.view_xmlid or "").split(","):
                    level.setdefault(page.id, 0)
        if model and view_type:
            types = VIEW_TYPE_ALIASES.get(view_type, (view_type,))
            for page in self.search(
                [("model", "=", model), ("view_type", "in", types)]
            ):
                level.setdefault(page.id, 1)
        if model:
            for page in self.search(
                [("model", "=", model), ("view_type", "in", (False, ""))]
            ):
                level.setdefault(page.id, 2)
        pages = self.browse(list(level))
        if loose_from:
            pages = pages.filtered(
                lambda p: not p.clear_cut
                and p.priority >= PRIORITY_LOOSE
                and p.key != loose_from
            )
        if not pages:
            return pages

        rules = {}
        clear_cut = pages.filtered("clear_cut")
        for rule in Rule.search([("page_key", "in", clear_cut.mapped("key"))]):
            rules.setdefault(rule.page_key, []).append(rule)
        specs = [p.when for p in pages if p.when]
        specs += [r.condition for items in rules.values() for r in items]
        names = set(n for spec in specs for n, op, w in rst_help.parse_when(spec))
        when_values = self._wch_when_values(model, values, names)
        with_rules, general = [], []
        for page in pages:
            if page.when and not rst_help.when_match(page.when, when_values):
                continue
            if not page.clear_cut:
                general.append(page)
            elif any(
                rst_help.when_match(r.condition, when_values)
                for r in rules.get(page.key, [])
            ):
                with_rules.append(page)
        for found in (with_rules, general):
            if found:
                best = min(
                    found,
                    key=lambda p: (
                        p.priority,
                        level[p.id],
                        -rst_help.when_count(p.when) if p.when else 0,
                        p.key,
                    ),
                )
                # every language of the page: the user's one is picked
                return self._wch_best_lang(
                    self.browse([p.id for p in found if p.key == best.key]), lang
                )
        return self.browse()

    @api.model
    def _wch_best_lang(self, pages, lang):
        for code in (lang, rst_help.DEFAULT_LANG):
            found = pages.filtered(lambda p: p.lang == code)
            if found:
                return found[0]
        return pages[0]

    @api.model
    def get_page(self, key, lang=None):
        lang = lang or self.env.context.get("lang") or rst_help.DEFAULT_LANG
        pages = self.search([("key", "=", key)])
        return self._wch_best_lang(pages, lang) if pages else pages

    @api.model
    def _wch_with_lang(self, lang):
        """Self in lang when installed: Odoo 17+ rejects any other code"""
        if lang in dict(self.env["res.lang"].get_installed()):
            return self.with_context(lang=lang)
        return self

    @api.model
    def fields_help(self, model):
        """[(name, string, help)] of the fields of model having a help"""
        if model not in self.env:
            return []
        info = self.env[model].fields_get(attributes=["string", "help"])
        return sorted(
            (name, vals.get("string") or name, vals["help"])
            for name, vals in info.items()
            if vals.get("help")
        )

    # ------------------------------------------------------------------
    # Ask
    # ------------------------------------------------------------------
    @api.model
    def _wch_ask_providers(self):
        """Ordered method names answering ``(question, context)``.

        Override to add a provider: the first one returning results wins."""
        return ["_wch_ask_fulltext"]

    @api.model
    def ask(self, question, context=None):
        context = context or {}
        question = (question or "").strip()
        if not question:
            return {"results": [], "provider": False}
        results, provider = [], False
        for method in self._wch_ask_providers():
            results = getattr(self, method)(question, context)
            if results:
                provider = method
                break
        self.env["context.help.question"].sudo().create(
            {
                "question": question[:1024],
                "model": context.get("model") or False,
                "page_key": context.get("page_key") or False,
                "found": bool(results),
                "provider": provider or False,
                "answer_page_id": results[0]["page_id"] if results else False,
            }
        )
        return {"results": results, "provider": provider}

    @api.model
    def _wch_ask_fulltext(self, question, context, limit=5):
        words = set(w.lower() for w in RE_WORD.findall(question))
        if not words:
            return []
        lang = (
            context.get("lang") or self.env.context.get("lang") or rst_help.DEFAULT_LANG
        )
        domain = [
            ("page_id.active", "=", True),
            ("page_id.lang", "in", (lang, rst_help.DEFAULT_LANG)),
        ]
        scored = []
        for section in self.env["context.help.section"].search(domain):
            title = (section.title or "").lower()
            text = (section.text or "").lower()
            score = sum(
                3 * (w in title)
                + (w in text)
                + 2 * (w in (section.question or "").lower())
                for w in words
            )
            if context.get("model") and section.page_id.model == context["model"]:
                score += 1
            if score > len(words) // 2:
                scored.append((score, section))
        scored.sort(key=lambda x: (-x[0], x[1].id))
        results, seen = [], set()
        for score, section in scored:
            page = section.page_id
            if (page.key, section.label) in seen:
                continue
            seen.add((page.key, section.label))
            results.append(
                {
                    "page_id": page.id,
                    "page_key": page.key,
                    "page_title": page.name,
                    "title": section.title,
                    "snippet": (section.text or "")[:300],
                    "url": "%s#%s"
                    % (
                        self.page_url(
                            page.key,
                            page.lang,
                            view="faq"
                            if section.label == html_page.FAQ_LABEL
                            else None,
                        ),
                        section.label,
                    ),
                    "score": score,
                }
            )
            if len(results) >= limit:
                break
        return results

    # ------------------------------------------------------------------
    # Videos
    # ------------------------------------------------------------------
    @api.model
    def _wch_video_dir(self):
        """Absolute path of the video directory (system parameter)"""
        path = (
            self.env["ir.config_parameter"].sudo().get_param(VIDEO_PATH_PARAM)
            or VIDEO_PATH_DEFAULT
        )
        return os.path.realpath(os.path.expanduser(path.strip()))

    @api.model
    def video_list(self):
        """{path, videos: [{name, size}]}: the videos of the video directory
        and its subdirectories, name relative to the directory"""
        root = self._wch_video_dir()
        videos = []
        for dirpath, dirnames, filenames in os.walk(root, followlinks=True):
            dirnames[:] = sorted(d for d in dirnames if not d.startswith("."))
            for fn in sorted(filenames):
                if fn.startswith(".") or not fn.lower().endswith(VIDEO_EXTS):
                    continue
                full = os.path.join(dirpath, fn)
                videos.append(
                    {
                        "name": os.path.relpath(full, root).replace(os.sep, "/"),
                        "size": os.path.getsize(full),
                    }
                )
        return {"path": root, "exists": os.path.isdir(root), "videos": videos}

    @api.model
    def video_file(self, name):
        """Full path of a video of the video directory, None when the name
        is not a video or goes out of the directory"""
        if not name or not name.lower().endswith(VIDEO_EXTS):
            return None
        root = self._wch_video_dir()
        full = os.path.realpath(os.path.join(root, name))
        if not full.startswith(root + os.sep) or not os.path.isfile(full):
            return None
        return full

    # ------------------------------------------------------------------
    # Build from RST sources
    # ------------------------------------------------------------------
    def _register_hook(self):
        res = super(ContextHelpPage, self)._register_hook()
        try:
            with self.env.cr.savepoint():
                self.sudo().sync_sources()
        except Exception:  # pragma: no cover
            _logger.exception("web_context_help: help sources not synchronized")
        return res

    @api.model
    def _wch_version(self):
        return release.version_info[0]

    @api.model
    def _wch_group(self):
        return rst_help.version_group(self._wch_version())

    @api.model
    def _wch_modules(self):
        """Installed modules having help sources, in dependency order"""
        mods = self.env["ir.module.module"].search(
            [("state", "in", ("installed", "to upgrade"))]
        )
        deps = {m.name: set(m.dependencies_id.mapped("name")) for m in mods}
        ordered, done = [], set()

        def visit(name, stack):
            if name in done or name not in deps or name in stack:
                return
            for dep in sorted(deps[name]):
                visit(dep, stack | {name})
            done.add(name)
            ordered.append(name)

        for name in sorted(deps):
            visit(name, set())
        result = []
        for name in ordered:
            path = get_module_path(name)
            help_dir = path and os.path.join(path, "help")
            if help_dir and os.path.isdir(help_dir):
                result.append((name, help_dir))
        return result

    @api.model
    def sync_sources(self, force=False):
        """Rebuild the pages when any help source checksum changed"""
        group = self._wch_group()
        version = self._wch_version()
        modules = self._wch_modules()
        checksums = {
            name: rst_help.checksum(path, group, version) for name, path in modules
        }
        Source = self.env["context.help.source"]
        stored = {s.module: s for s in Source.search([])}
        if not force and checksums == {m: s.checksum for m, s in stored.items()}:
            return False
        _logger.info("web_context_help: rebuilding help pages")
        self._wch_rebuild(modules, group, version)
        for name, value in checksums.items():
            if name in stored:
                if stored[name].checksum != value:
                    stored[name].checksum = value
            else:
                Source.create({"module": name, "checksum": value})
        for name, rec in stored.items():
            if name not in checksums:
                rec.unlink()
        return True

    @api.model
    def _wch_parse_module(self, module, help_dir, group, version=None):
        """Return (pages, inherits) parsed from the sources of one module"""
        pages, inherits = [], []
        for filename, path in sorted(rst_help.list_sources(help_dir, group).items()):
            base, lang = rst_help.split_lang(filename)
            try:
                doc = rst_help.parse_file(
                    path,
                    help_dir,
                    group,
                    lang,
                    fields_help=self._wch_with_lang(lang).fields_help,
                    version=version,
                )
            except Exception as e:
                _logger.warning("web_context_help: %s not parsed: %s", path, e)
                continue
            for inherit in doc.wch_inherits:
                inherits.append(dict(inherit, module=module, base=base, lang=lang))
            if doc.wch_page:
                pages.append(
                    {
                        "doc": doc,
                        "module": module,
                        "help_dir": help_dir,
                        "path": path,
                        "base": base,
                        "lang": lang,
                        "page": doc.wch_page,
                    }
                )
        return pages, inherits

    @api.model
    def _wch_inherits_for(self, inherits, key, lang):
        """Inherits of a page in lang; a source without twin applies to all"""
        result = []
        sources = {}
        for inherit in inherits:
            if inherit["target"] != key:
                continue
            sources.setdefault((inherit["module"], inherit["base"]), []).append(inherit)
        for dummy, items in sources.items():
            langs = set(i["lang"] for i in items)
            use = lang if lang in langs else rst_help.DEFAULT_LANG
            result.extend(i for i in items if i["lang"] == use)
        return result

    @api.model
    def _wch_rebuild(self, modules, group, version=None):
        version = version or self._wch_version()
        order = {name: seq for seq, (name, dummy) in enumerate(modules)}
        pages, inherits = [], []
        for module, help_dir in modules:
            p, i = self._wch_parse_module(module, help_dir, group, version)
            pages.extend(p)
            inherits.extend(i)
        inherits.sort(key=lambda i: order.get(i["module"], 0))
        globals_ = {}
        built = {}
        for item in pages:
            key = "%s.%s" % (item["module"], item["page"]["name"])
            doc = item["doc"]
            if item["page"]["view_type"] in rst_help.LIST_VIEW_TYPES:
                lang = item["lang"]
                if lang not in globals_:
                    globals_[lang] = self._wch_global_search(group, lang, version)
                if globals_[lang]:
                    rst_help.insert_global(doc, globals_[lang], "wildcard", "search")
            for inherit in self._wch_inherits_for(inherits, key, item["lang"]):
                ok = rst_help.apply_inherit(
                    doc,
                    inherit,
                    item["help_dir"],
                    group,
                    item["lang"],
                    self._wch_with_lang(item["lang"]).fields_help,
                    version,
                )
                if not ok:
                    _logger.warning(
                        "web_context_help: %s inherit from %s: section %s not found",
                        key,
                        inherit["module"],
                        inherit["section"],
                    )
            page = item["page"]
            built[(key, item["lang"])] = {
                "vals": {
                    "key": key,
                    "lang": item["lang"],
                    "name": rst_help.page_title(doc, page),
                    "module": item["module"],
                    "source_file": os.path.relpath(
                        item["path"], os.path.dirname(item["help_dir"])
                    ),
                    "model": page["model"] or False,
                    "view_xmlid": page["view"] or False,
                    "view_type": page["view_type"] or False,
                    "when": page.get("when") or False,
                    "priority": page.get("priority") or PRIORITY_STANDARD,
                    "active": True,
                },
                "html": rst_help.to_html(doc),
                "sections": rst_help.extract_sections(doc),
            }
        self._wch_store(built)

    @api.model
    def _wch_global_search(self, group, lang, version=None):
        """Nodes of the wildcard text added to the search of every list page"""
        help_dir = os.path.join(get_module_path("web_context_help"), "help")
        path = rst_help.resolve_include(help_dir, group, rst_help.GLOBAL_SEARCH, lang)
        if not path:
            return []
        try:
            doc = rst_help.parse_file(path, help_dir, group, lang, version=version)
        except Exception as e:
            _logger.warning("web_context_help: %s not parsed: %s", path, e)
            return []
        return doc.children[:]

    @api.model
    def _wch_store(self, built):
        Page = self.with_context(wch_sync=True, active_test=False)
        existing = {(p.key, p.lang): p for p in Page.search([])}
        for ident, data in built.items():
            vals = dict(data["vals"])
            page = existing.pop(ident, None)
            html = data["html"]
            if page is None:
                vals.update(source_html=html, html=html)
                page = Page.create(vals)
            else:
                if page.source_html != html:
                    vals["source_html"] = html
                    if page.edited:
                        vals["source_changed"] = True
                    else:
                        vals["html"] = html
                page.write(vals)
            # an edited page keeps the content of the administrator
            if page.edited:
                page._wch_set_sections(html_page.extract_sections(page.html))
            else:
                page._wch_set_sections(data["sections"])
        for page in existing.values():
            if not page.source_file:
                # created by the administrator: no source, kept as it is
                continue
            if page.edited:
                page.active = False
            else:
                page.unlink()


class ContextHelpQuestion(models.Model):
    _name = "context.help.question"
    _description = "Context help question log"
    _order = "id desc"

    question = fields.Char(required=True)
    model = fields.Char()
    page_key = fields.Char()
    user_id = fields.Many2one("res.users", default=lambda self: self.env.uid)
    found = fields.Boolean()
    provider = fields.Char()
    answer_page_id = fields.Many2one("context.help.page", ondelete="set null")

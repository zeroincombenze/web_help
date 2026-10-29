# -*- coding: utf-8 -*-
#
# Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
#
# License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
#
import mimetypes
import os
import re

from markupsafe import escape
from werkzeug.exceptions import Forbidden, NotFound

from odoo import http
from odoo.http import Stream, request

from ..lib import html_page
from ..models.context_help_page import HOME_KEY

RE_LANG = re.compile(r"^[a-z]{2,3}(_[A-Za-z0-9]+)?(@\w+)?$")


class ContextHelp(http.Controller):
    def _lang(self, lang=None):
        """lang of the request; a malformed one is cut at the first bad char,
        e.g. it_IT?debug=1 (a second "?" in the URL) gives it_IT"""
        if lang and not RE_LANG.match(lang):
            lang = re.split(r"[^\w@]", lang, maxsplit=1)[0]
        if lang and RE_LANG.match(lang):
            return lang
        return request.env.context.get("lang") or request.env.user.lang

    def _nav(self, lang, current=None):
        """Buttons of every help window page: Home and Summary"""
        Page = request.env["context.help.page"]
        nav = {}
        if current != "home" and Page.get_page(HOME_KEY, lang):
            nav["home"] = Page.page_url(HOME_KEY, lang)
        if current != "summary":
            nav["summary"] = "/web_context_help/summary?lang=%s" % lang
        return nav

    def _html(self, body):
        return request.make_response(
            body, headers=[("Content-Type", "text/html; charset=utf-8")]
        )

    @http.route("/web_context_help/home", type="http", auth="user")
    def home(self, lang=None, **kw):
        """Page of the Help menu; the summary when the page is missing"""
        lang = self._lang(lang)
        Page = request.env["context.help.page"]
        if Page.get_page(HOME_KEY, lang):
            return request.redirect(Page.page_url(HOME_KEY, lang))
        return request.redirect("/web_context_help/summary?lang=%s" % lang)

    @http.route("/web_context_help/summary", type="http", auth="user")
    def summary(self, lang=None, **kw):
        """Pages of every installed help module, grouped by module"""
        lang = self._lang(lang)
        groups = request.env["context.help.page"].summary(lang)
        return self._html(
            html_page.render(
                html_page.labels(lang)["summary_title"],
                html_page.summary_body(groups, lang),
                lang=lang,
                nav=self._nav(lang, "summary"),
            )
        )

    @http.route("/web_context_help/lookup", type="json", auth="user")
    def lookup(
        self,
        model=None,
        view_type=None,
        view_id=None,
        lang=None,
        values=None,
        loose_from=None,
        **kw
    ):
        """loose_from: key of the page shown, for its Loose help button"""
        lang = self._lang(lang)
        Page = request.env["context.help.page"]
        page = Page.lookup(
            model=model,
            view_type=view_type,
            view_id=view_id,
            lang=lang,
            values=values if isinstance(values, dict) else None,
            loose_from=loose_from if isinstance(loose_from, str) else None,
        )
        if page:
            return {"url": Page.page_url(page.key, lang), "key": page.key}
        if model and model in request.env:
            return {"url": "/web_context_help/auto/%s?lang=%s" % (model, lang)}
        return {"url": False}

    @http.route("/web_context_help/loose/<string:key>", type="http", auth="user")
    def loose(self, key, lang=None, **kw):
        """Loose help of a page opened without the Odoo tab: the record is
        unknown, the general page is looked up by the model of the page"""
        lang = self._lang(lang)
        Page = request.env["context.help.page"]
        page = Page.get_page(key, lang)
        if not page or not page.model:
            raise NotFound()
        found = Page.lookup(
            model=page.model, view_type=page.view_type, lang=lang, loose_from=key
        )
        if found:
            return request.redirect(Page.page_url(found.key, lang))
        return request.redirect(
            "/web_context_help/auto/%s?lang=%s" % (page.model, lang)
        )

    @http.route("/web_context_help/page/<string:key>", type="http", auth="user")
    def page(self, key, lang=None, view=None, **kw):
        """view: None for the page, "faq" or "fields" for its FAQ (section of
        the page) or Fields (fields help of its model) page"""
        lang = self._lang(lang)
        Page = request.env["context.help.page"]
        page = Page.get_page(key, lang)
        if not page:
            raise NotFound()
        content, faq_html = html_page.split_faq(page.html or "")
        fields_help = (
            Page._wch_with_lang(lang).fields_help(page.model) if page.model else []
        )
        pages = {None: True, "faq": faq_html, "fields": fields_help}
        if view not in pages or not pages[view]:
            return request.redirect(Page.page_url(page.key, lang))
        tr = html_page.labels(lang)
        title = page.name
        if view == "faq":
            title = "%s - %s" % (page.name, tr["faq"])
            content = "<h1>%s</h1>\n%s" % (escape(page.name), faq_html)
        elif view == "fields":
            title = "%s - %s" % (page.name, tr["fields"])
            content = html_page.fields_body(page.name, fields_help, lang)
        nav = {
            name: Page.page_url(page.key, lang, view=None if name == "help" else name)
            for name in ("help", "faq", "fields")
            if name != (view or "help") and pages[None if name == "help" else name]
        }
        if page.model and page.has_loose_help():
            nav["loose"] = "/web_context_help/loose/%s?lang=%s" % (page.key, lang)
        nav.update(self._nav(lang, "home" if page.key == HOME_KEY else None))
        if page.has_access("write"):
            nav["edit"] = Page.edit_url(page)
        body = html_page.render(
            title,
            content,
            lang=lang,
            page_key=page.key,
            model=page.model or "",
            warning=page.source_changed
            and request.env.user.has_group("web_context_help.group_help_editor"),
            nav=nav,
        )
        return self._html(body)

    @http.route("/web_context_help/auto/<string:model>", type="http", auth="user")
    def auto(self, model, lang=None, **kw):
        lang = self._lang(lang)
        if model not in request.env:
            raise NotFound()
        Page = request.env["context.help.page"]._wch_with_lang(lang)
        title = (
            request.env["ir.model"]
            .with_env(Page.env)
            .search([("model", "=", model)], limit=1)
            .name
        )
        body = html_page.render_auto(
            title or model,
            Page.fields_help(model),
            lang=lang,
            model=model,
            nav=self._nav(lang),
        )
        return self._html(body)

    @http.route("/web_context_help/ask", type="json", auth="user")
    def ask(self, question=None, context=None, **kw):
        context = dict(context or {})
        context.setdefault("lang", self._lang())
        return request.env["context.help.page"].ask(question, context)

    @http.route("/web_context_help/videos", type="json", auth="user")
    def videos(self, **kw):
        """Videos that a help editor can insert in a help page"""
        if not request.env.user.has_group("web_context_help.group_help_editor"):
            raise Forbidden()
        return request.env["context.help.page"].video_list()

    @http.route("/web_context_help/video/<path:name>", type="http", auth="user")
    def video(self, name, **kw):
        """A video of the video directory, streamed with HTTP range support"""
        path = request.env["context.help.page"].video_file(name)
        if not path:
            raise NotFound()
        stat = os.stat(path)
        stream = Stream(
            type="path",
            path=path,
            mimetype=mimetypes.guess_type(path)[0] or "application/octet-stream",
            download_name=os.path.basename(path),
            etag="%d-%d" % (int(stat.st_mtime), stat.st_size),
            last_modified=stat.st_mtime,
            size=stat.st_size,
        )
        return stream.get_response(as_attachment=bool(kw.get("download")))

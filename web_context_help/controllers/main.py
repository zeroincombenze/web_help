# -*- coding: utf-8 -*-
#
# Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
#
# License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
#
from markupsafe import escape
from werkzeug.exceptions import NotFound

from odoo import http
from odoo.http import request

from ..lib import html_page


class ContextHelp(http.Controller):
    def _lang(self, lang=None):
        return lang or request.env.context.get("lang") or request.env.user.lang

    @http.route("/web_context_help/lookup", type="json", auth="user")
    def lookup(
        self, model=None, view_type=None, view_id=None, lang=None, values=None, **kw
    ):
        lang = self._lang(lang)
        Page = request.env["context.help.page"]
        page = Page.lookup(
            model=model,
            view_type=view_type,
            view_id=view_id,
            lang=lang,
            values=values if isinstance(values, dict) else None,
        )
        if page:
            return {"url": Page.page_url(page.key, lang), "key": page.key}
        if model and model in request.env:
            return {"url": "/web_context_help/auto/%s?lang=%s" % (model, lang)}
        return {"url": False}

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
            for name in html_page.NAV
            if name != (view or "help") and pages[None if name == "help" else name]
        }
        body = html_page.render(
            title,
            content,
            lang=lang,
            page_key=page.key,
            model=page.model or "",
            warning=page.source_changed
            and request.env.user.has_group("base.group_system"),
            nav=nav,
        )
        return request.make_response(
            body, headers=[("Content-Type", "text/html; charset=utf-8")]
        )

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
            title or model, Page.fields_help(model), lang=lang, model=model
        )
        return request.make_response(
            body, headers=[("Content-Type", "text/html; charset=utf-8")]
        )

    @http.route("/web_context_help/ask", type="json", auth="user")
    def ask(self, question=None, context=None, **kw):
        context = dict(context or {})
        context.setdefault("lang", self._lang())
        return request.env["context.help.page"].ask(question, context)

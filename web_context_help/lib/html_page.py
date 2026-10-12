# -*- coding: utf-8 -*-
#
# Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
#
# License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
#
"""Standalone HTML document of the help window; no QWeb, version independent"""
from __future__ import unicode_literals

import json
import os

from lxml import html as lxml_html

try:  # pragma: no cover
    from markupsafe import escape
except ImportError:  # pragma: no cover
    from cgi import escape

STATIC = "/web_context_help/static/src/common"
# The question box is hidden until the ask feature is released
ASK_ENABLED = False
STATIC_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static", "src", "common"
)


def asset_version():
    """Cache buster: last change of the help window assets"""
    try:
        return int(
            max(
                os.path.getmtime(os.path.join(STATIC_DIR, fn))
                for fn in os.listdir(STATIC_DIR)
            )
        )
    except (OSError, ValueError):
        return 0


LABELS = {
    "en_US": {
        "follow": "Follow Odoo",
        "find": "Find in page",
        "prev": "Previous match",
        "next": "Next match",
        "any_word": "any word",
        "faq": "FAQ",
        "fields": "Fields",
        "help": "Help",
        "ask": "Ask a question",
        "none": "No answer found",
        "auto": "Fields of this form",
        "changed": "The original source has changed since this page was edited.",
    },
    "it_IT": {
        "follow": "Segui Odoo",
        "find": "Cerca nella pagina",
        "prev": "Occorrenza precedente",
        "next": "Occorrenza successiva",
        "any_word": "qualsiasi parola",
        "faq": "FAQ",
        "fields": "Campi",
        "help": "Aiuto",
        "ask": "Fai una domanda",
        "none": "Nessuna risposta trovata",
        "auto": "Campi di questa maschera",
        "changed": "La sorgente originale è cambiata dopo la modifica di questa pagina.",
    },
}


def labels(lang):
    return LABELS.get(lang) or LABELS.get((lang or "")[:2] + "_IT") or LABELS["en_US"]


FAQ_LABEL = "faq"


def _section(el):
    """Section of an element: itself or an ancestor (docutils <section> or
    <div class="section">); the label is often an empty <span id=..> in it"""
    while el is not None:
        if el.tag == "section" or "section" in (el.get("class") or "").split():
            return el
        el = el.getparent()
    return None


def split_faq(body_html):
    """Return (body without the FAQ section, FAQ section html or "").

    The questions built from the fields help (wch-auto-q) are dropped: the
    Fields page shows them. A FAQ left with its title only is ""."""
    if not body_html or ('id="%s"' % FAQ_LABEL) not in body_html:
        return body_html, ""
    root = lxml_html.fragment_fromstring(body_html, create_parent="div")
    found = root.xpath("//*[@id=$label]", label=FAQ_LABEL)
    section = _section(found[0]) if found else None
    if section is None or section is root:
        return body_html, ""
    section.drop_tree()
    xpath = './/*[contains(concat(" ", @class, " "), " wch-auto-q ")]'
    for auto in section.xpath(xpath):
        auto.drop_tree()
    title = section.xpath("./h1|./h2|./h3|./h4|./h5|./h6")
    rest = section.text_content()
    if title:
        rest = rest.replace(title[0].text_content(), "", 1)
    faq = lxml_html.tostring(section, encoding="unicode") if rest.strip() else ""
    body = (root.text or "") + "".join(
        lxml_html.tostring(child, encoding="unicode") for child in root
    )
    return body, faq


NAV = ("help", "faq", "fields")


def render(
    title, body_html, lang="en_US", page_key="", model="", warning=False, nav=None
):
    """nav: {"help"|"faq"|"fields": url} buttons in the header, in NAV order"""
    tr = labels(lang)
    config = json.dumps(
        {"page_key": page_key, "model": model, "lang": lang, "labels": tr}
    ).replace("</", "<\\/")
    return """<!DOCTYPE html>
<html lang="%(lang)s">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>%(title)s</title>
<link rel="stylesheet" href="%(static)s/help_window.css?v=%(version)s"/>
</head>
<body class="wch-body">
<header class="wch-header">
  <label class="wch-follow"><input type="checkbox" id="wch_follow"/> %(follow)s</label>
  <div class="wch-find">
    <input type="search" id="wch_find" placeholder="%(find)s" autocomplete="off"/>
    <span id="wch_find_count" class="wch-find-count"></span>
    <button type="button" id="wch_find_prev" class="wch-find-nav" title="%(prev)s">&#9650;</button>
    <button type="button" id="wch_find_next" class="wch-find-nav" title="%(next)s">&#9660;</button>
  </div>
%(nav)s%(ask_form)s</header>
%(answers)s%(warning)s<main class="wch-content">
%(body)s
</main>
<script>window.wchConfig = %(config)s;</script>
<script src="%(static)s/help_window.js?v=%(version)s"></script>
</body>
</html>
""" % {
        "lang": escape(lang.replace("_", "-")),
        "title": escape(title),
        "static": STATIC,
        "version": asset_version(),
        "follow": escape(tr["follow"]),
        "nav": "".join(
            '  <a class="wch-nav" id="wch_%s" href="%s">%s</a>\n'
            % (name, escape(nav[name]), escape(tr[name]))
            for name in NAV
            if (nav or {}).get(name)
        ),
        "find": escape(tr["find"]),
        "prev": escape(tr["prev"]),
        "next": escape(tr["next"]),
        "ask_form": (
            '  <form class="wch-ask" id="wch_ask">\n'
            '    <input type="search" id="wch_question" placeholder="%s"'
            ' autocomplete="off"/>\n'
            "  </form>\n" % escape(tr["ask"])
            if ASK_ENABLED
            else ""
        ),
        "answers": (
            '<div id="wch_answers" class="wch-answers"></div>\n'
            if ASK_ENABLED
            else ""
        ),
        "warning": (
            '<div class="wch-warning">%s</div>\n' % escape(tr["changed"])
            if warning
            else ""
        ),
        "body": body_html,
        "config": config,
    }


def fields_body(title, fields_help, lang="en_US"):
    """Body listing the fields help; a field name highlights it in Odoo"""
    tr = labels(lang)
    rows = "\n".join(
        '<dt><a href="#" class="wch-field" data-field="%s">%s</a></dt><dd>%s</dd>'
        % (escape(name), escape(string), escape(text))
        for name, string, text in fields_help
    )
    return '<h1>%s</h1>\n<h2>%s</h2>\n<dl class="wch-auto">\n%s\n</dl>' % (
        escape(title),
        escape(tr["auto"]),
        rows,
    )


def render_auto(title, fields_help, lang="en_US", model=""):
    """Page built on the fly from the fields help of a model"""
    return render(title, fields_body(title, fields_help, lang), lang=lang, model=model)

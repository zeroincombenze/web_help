# -*- coding: utf-8 -*-
#
# Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
#
# License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
#
from odoo import _, api, fields, models
from odoo.exceptions import UserError

from markupsafe import escape

try:  # pragma: no cover
    from urllib.parse import quote
except ImportError:  # pragma: no cover - Python 2
    from urllib import quote

VIDEO_URL = "/web_context_help/video/"


def video_url(name):
    """URL of a video of the video directory, every path part quoted"""
    parts = []
    for part in name.split("/"):
        if not isinstance(part, bytes):
            part = part.encode("utf-8")
        parts.append(quote(part, safe=""))
    return VIDEO_URL + "/".join(parts)


def video_html(name):
    """Player of a video, in its own paragraph, started by a click"""
    url = video_url(name)
    return (
        '<p><video src="%(url)s" controls="controls" preload="metadata"'
        ' style="max-width:100%%; width:960px;" title="%(title)s">'
        '%(cannot)s<a href="%(url)s?download=1">%(download)s</a>.</video></p>'
    ) % {
        "url": escape(url),
        "title": escape(name),
        "cannot": escape(_("The browser cannot play the video: ")),
        "download": escape(_("download it")),
    }


class ContextHelpVideoWizard(models.TransientModel):
    """Odoo 10 has no editor plugin: a help editor picks a video of the video
    directory (system parameter web_help_video_path) and it is added at the
    end of the page, or after the paragraph containing a given text."""

    _name = "context.help.video.wizard"
    _description = "Insert a help video"

    page_id = fields.Many2one("context.help.page", required=True, ondelete="cascade")
    video = fields.Selection("_selection_video", required=True)
    video_path = fields.Char("Video directory", compute="_compute_video_path")
    after_text = fields.Char(
        "After the text",
        help="The video is inserted after the paragraph (or heading) holding "
        "this text; at the end of the page when empty or not found",
    )

    @api.model
    def _selection_video(self):
        if not self.env.user.has_group("web_context_help.group_help_editor"):
            return []
        listed = self.env["context.help.page"].video_list()
        return [(v["name"], v["name"]) for v in listed["videos"]]

    @api.depends("page_id")
    def _compute_video_path(self):
        path = self.env["context.help.page"]._wch_video_dir()
        for wizard in self:
            wizard.video_path = path

    @api.model
    def _insert(self, html, player, after_text):
        """html with player after the block holding after_text, else at end"""
        html = html or ""
        if after_text:
            from lxml import html as lxml_html

            root = lxml_html.fragment_fromstring(html, create_parent="div")
            needle = " ".join(after_text.split()).lower()
            blocks = (
                "p",
                "h1",
                "h2",
                "h3",
                "h4",
                "h5",
                "h6",
                "li",
                "pre",
                "blockquote",
                "table",
            )
            for el in root.iter(*blocks):
                if needle in " ".join(el.text_content().split()).lower():
                    # out of lists: a paragraph is not allowed there
                    while el.getparent() is not None and el.getparent().tag in (
                        "ul",
                        "ol",
                        "li",
                    ):
                        el = el.getparent()
                    el.addnext(lxml_html.fragment_fromstring(player))
                    return (root.text or "") + "".join(
                        lxml_html.tostring(child, encoding="unicode") for child in root
                    )
        return html + player

    @api.multi
    def action_insert(self):
        self.ensure_one()
        if not self.env["context.help.page"].video_file(self.video):
            raise UserError(
                _("The video %s is not in the video directory") % self.video
            )
        page = self.page_id
        page.html = self._insert(page.html, video_html(self.video), self.after_text)
        return {"type": "ir.actions.act_window_close"}

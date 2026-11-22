# -*- coding: utf-8 -*-
#
# Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
#
# License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
#
from odoo import api, models


class IrUiMenu(models.Model):
    _inherit = "ir.ui.menu"

    @api.model
    def _visible_menu_ids(self, debug=False):
        """The Help menus are hidden to the users without help"""
        visible = super(IrUiMenu, self)._visible_menu_ids(debug=debug)
        if not self.env.user._wch_help_disabled():
            return visible
        root = self.env.ref("web_context_help.menu_help_root", raise_if_not_found=False)
        if not root:
            return visible
        # full_list: the search must not filter the menus again (endless recursion)
        full = self.sudo().with_context(**{"ir.ui.menu.full_list": True})
        return visible - set(full.search([("id", "child_of", root.id)]).ids)

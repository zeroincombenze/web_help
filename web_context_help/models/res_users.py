# -*- coding: utf-8 -*-
#
# Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
#
# License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
#
from odoo import models

GROUP_NO_HELP = "web_context_help.group_no_help"
GROUP_HELP_USER = "web_context_help.group_help_user"


class ResUsers(models.Model):
    _inherit = "res.users"

    def _wch_help_disabled(self):
        """The help is hidden to the users of the No help group; the User and
        System levels, that imply it, keep the help"""
        self.ensure_one()
        return self.has_group(GROUP_NO_HELP) and not self.has_group(GROUP_HELP_USER)

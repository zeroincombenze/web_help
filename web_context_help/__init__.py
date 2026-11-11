# -*- coding: utf-8 -*-
#
# Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
#
# License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
#
from . import controllers
from . import models

from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry):
    """The administrators start as System help editors, then the Context Help
    field of the user form sets their level"""
    env = api.Environment(cr, SUPERUSER_ID, {})
    admins = env.ref("base.group_system").with_context(active_test=False).users
    env.ref("web_context_help.group_help_editor").write(
        {"users": [(4, user.id) for user in admins]}
    )

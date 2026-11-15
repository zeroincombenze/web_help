# -*- coding: utf-8 -*-
#
# Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
#
{
    "name": "Context help tours",
    "version": "18.0.1.0.0",
    "category": "Hidden/Tools",
    "summary": "Guided tours of the context help pages, played in the Odoo tab",
    "author": "Zeroincombenze srls",
    "website": "https://github.com/zeroincombenze/web_help",
    "development_status": "Alpha",
    "license": "LGPL-3",
    "depends": ["web_context_help"],
    "assets": {
        "web.assets_backend": [
            "web_context_help_tour/static/src/v18/tour_player.js",
            "web_context_help_tour/static/src/v18/tour_player.scss",
        ],
    },
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}

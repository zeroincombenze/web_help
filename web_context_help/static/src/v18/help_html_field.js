/* Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
 * License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
 *
 * VERSION-DEPENDENT: Odoo 18 adapter.
 * Html field of the help pages: the standard html field (code view in
 * developer mode) with the Help video button in the floating toolbar.
 */
import {registry} from "@web/core/registry";
import {HtmlField, htmlField} from "@html_editor/fields/html_field";
import {HelpVideoPlugin} from "./help_video_plugin";

export class HelpHtmlField extends HtmlField {
    getConfig() {
        const config = super.getConfig();
        config.Plugins = [...config.Plugins, HelpVideoPlugin];
        return config;
    }
}

export const helpHtmlField = {
    ...htmlField,
    component: HelpHtmlField,
};

registry.category("fields").add("wch_html", helpHtmlField);

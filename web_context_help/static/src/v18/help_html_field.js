/* Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
 * License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
 *
 * VERSION-DEPENDENT: Odoo 18 adapter.
 * Html field of the help pages: the code view button (</>) without the
 * developer mode, needed to insert a <video> or other raw HTML.
 */
import {registry} from "@web/core/registry";
import {htmlField} from "@html_editor/fields/html_field";

export const helpHtmlField = {
    ...htmlField,
    extractProps(fieldInfo, dynamicInfo) {
        return {...htmlField.extractProps(fieldInfo, dynamicInfo), codeview: true};
    },
};

registry.category("fields").add("wch_html", helpHtmlField);

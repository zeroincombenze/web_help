/* Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
 * License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
 *
 * VERSION-DEPENDENT: Odoo 10 adapter.
 * The form widgets of Odoo 10 carry no field name in the DOM: the <field> of
 * the arch is replaced by the root of the widget, which only has the
 * o_form_field class (Odoo 11+ writes name="..." on .o_field_widget). The name
 * is written here, so the field: targets of the tour player find the widget.
 */
odoo.define("web_context_help_tour.form_field_name", function (require) {
    "use strict";

    var form_common = require("web.form_common");

    form_common.AbstractField.include({
        renderElement: function () {
            this._super.apply(this, arguments);
            if (this.name) {
                this.$el.attr("data-wch-field", this.name);
            }
        },
    });
});

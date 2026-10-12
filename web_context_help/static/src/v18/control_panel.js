/* Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
 * License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
 *
 * VERSION-DEPENDENT: Odoo 18 adapter, [?] button in the control panel.
 */
import {ControlPanel} from "@web/search/control_panel/control_panel";
import {patch} from "@web/core/utils/patch";
import {useService} from "@web/core/utils/hooks";
import {onMounted} from "@odoo/owl";

patch(ControlPanel.prototype, {
    setup() {
        super.setup(...arguments);
        this.contextHelp = useService("context_help");
        onMounted(() => {
            // Dialogs (e.g. Search More) keep the help of the main view
            if (!this.env.inDialog) {
                this.contextHelp.notify(this.getContextHelpContext());
            }
        });
    },
    getContextHelpContext() {
        const config = this.env.config || {};
        return {
            model:
                (this.env.searchModel && this.env.searchModel.resModel) ||
                (this.env.model && this.env.model.root && this.env.model.root.resModel),
            viewType: config.viewType,
            viewId: config.viewId,
            values: this.getContextHelpValues(),
        };
    },
    /**
     * Values checked by the "when" condition of the help pages: the
     * default_<name> keys of the action context (as <name>), overridden by the
     * selection and boolean fields of the open record (form view)
     */
    getContextHelpValues() {
        const values = {};
        const searchModel = this.env.searchModel;
        const context = (searchModel && searchModel.globalContext) || {};
        for (const [key, value] of Object.entries(context)) {
            const scalar = ["string", "number", "boolean"].includes(typeof value);
            if (key.startsWith("default_") && scalar) {
                values[key.slice(8)] = value;
            }
        }
        const root = this.env.model && this.env.model.root;
        if (root && root.data && root.fields && !root.records) {
            for (const [name, field] of Object.entries(root.fields)) {
                if (["selection", "boolean"].includes(field.type) && name in root.data) {
                    values[name] = root.data[name];
                }
            }
        }
        return values;
    },
    onContextHelpClick() {
        this.contextHelp.open(this.getContextHelpContext());
    },
});

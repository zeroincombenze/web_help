/* Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
 * License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
 *
 * VERSION-DEPENDENT: Odoo 18 adapter, [?] button in the control panel.
 */
import {ControlPanel} from "@web/search/control_panel/control_panel";
import {FormController} from "@web/views/form/form_controller";
import {patch} from "@web/core/utils/patch";
import {useService} from "@web/core/utils/hooks";
import {onMounted, useSubEnv} from "@odoo/owl";

/**
 * Values checked by the "when" condition and the rules of the help pages: the
 * default_<name> keys of the action context (as <name>), overridden by the
 * selection, boolean and many2one (its id) fields of the open record (form
 * view). The list view puts its model in env.model, the form view in
 * env.wchModel (see the FormController patch below).
 */
export function contextHelpValues(env) {
    const values = {};
    const searchModel = env.searchModel;
    const context = (searchModel && searchModel.globalContext) || {};
    for (const [key, value] of Object.entries(context)) {
        const scalar = ["string", "number", "boolean"].includes(typeof value);
        if (key.startsWith("default_") && scalar) {
            values[key.slice(8)] = value;
        }
    }
    const model = env.model || env.wchModel;
    const root = model && model.root;
    if (root && root.data && root.fields && !root.records) {
        for (const [name, field] of Object.entries(root.fields)) {
            if (!(name in root.data)) {
                continue;
            }
            if (["selection", "boolean"].includes(field.type)) {
                values[name] = root.data[name];
            } else if (field.type === "many2one") {
                // [id, display_name], {id, display_name} or false
                const value = root.data[name];
                values[name] =
                    (value && (Array.isArray(value) ? value[0] : value.id)) || false;
            }
        }
    }
    return values;
}

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
    getContextHelpValues() {
        return contextHelpValues(this.env);
    },
    onContextHelpClick() {
        this.contextHelp.open(this.getContextHelpContext());
    },
});

/**
 * The form view does not share its model with the control panel (the list
 * view does, as env.model): share it as env.wchModel, so the help sees the
 * fields of the open record, and follow the record when it is saved or the
 * pager moves to another one.
 */
patch(FormController.prototype, {
    setup() {
        super.setup(...arguments);
        useSubEnv({wchModel: this.model});
        this.contextHelp = useService("context_help");
    },
    notifyContextHelp() {
        if (this.env.inDialog || !this.model.root) {
            return;
        }
        this.contextHelp.notify({
            model: this.model.root.resModel,
            viewType: "form",
            viewId: this.env.config && this.env.config.viewId,
            values: contextHelpValues(this.env),
        });
    },
    async onRecordSaved() {
        const result = await super.onRecordSaved(...arguments);
        this.notifyContextHelp();
        return result;
    },
    async onPagerUpdate() {
        const result = await super.onPagerUpdate(...arguments);
        this.notifyContextHelp();
        return result;
    },
});

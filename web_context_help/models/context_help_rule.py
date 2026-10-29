# -*- coding: utf-8 -*-
#
# Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
#
# License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
#
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

RULE_FIELD_TYPES = ("selection", "boolean", "many2one")


class ContextHelpRule(models.Model):
    """Condition set by the administrator on a help page, no source needed:
    the page is shown when the open record (or the menu context) meets it.

    Several rules of a page are alternatives: one met is enough. The page
    ``when`` of the RST source must be met too."""

    _name = "context.help.rule"
    _description = "Context help rule"
    _order = "page_key, sequence, id"

    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
    page_id = fields.Many2one(
        "context.help.page",
        "Page",
        required=True,
        index=True,
        ondelete="cascade",
        # the rules choose among the clear cut pages only
        domain=[("model", "!=", False), ("clear_cut", "=", True)],
    )
    # the rule applies to the page in every language
    page_key = fields.Char(related="page_id.key", store=True, index=True)
    model = fields.Char(related="page_id.model", store=True)
    field_id = fields.Many2one(
        "ir.model.fields",
        "Field",
        required=True,
        ondelete="cascade",
        domain="[('model', '=', model), "
        "('ttype', 'in', ['selection', 'boolean', 'many2one'])]",
    )
    field_type = fields.Selection(related="field_id.ttype", readonly=True)
    relation = fields.Char(related="field_id.relation", readonly=True)
    operator = fields.Selection(
        [("=", "is"), ("!=", "is not")], required=True, default="="
    )
    # Odoo 10 has no model of the selection values: their keys are written
    selection_values = fields.Char(
        "Values",
        help="Selection field: any of these values, keys comma separated, "
        "e.g. draft, sent",
    )
    selection_help = fields.Char("Allowed values", compute="_compute_selection_help")
    value_boolean = fields.Boolean("Value", help="Boolean field: checked or not")
    res_id = fields.Integer(
        "Record id",
        help="Many2one field: id of the record, 0 when the field is empty",
    )
    # the record of a many2one rule is picked by a reference field, whose
    # model must be the comodel of the field
    record_ref = fields.Reference(
        string="Record",
        selection="_selection_target_model",
        compute="_compute_record_ref",
        inverse="_inverse_record_ref",
        help="Many2one field: this record; empty when the field is empty",
    )
    condition = fields.Char(
        compute="_compute_condition",
        store=True,
        help="Condition checked by the help lookup, same syntax as :when:",
    )

    @api.model
    def _selection_target_model(self):
        return [(m.model, m.name) for m in self.env["ir.model"].sudo().search([])]

    @api.multi
    def _selection_keys(self):
        self.ensure_one()
        return [
            x.strip() for x in (self.selection_values or "").split(",") if x.strip()
        ]

    @api.depends("field_id")
    def _compute_selection_help(self):
        for rule in self:
            field = rule.field_id
            if field.ttype != "selection" or field.model not in self.env:
                rule.selection_help = False
                continue
            info = self.env[field.model].fields_get([field.name], ["selection"])
            rule.selection_help = ", ".join(
                "%s (%s)" % (key, label)
                for key, label in info.get(field.name, {}).get("selection") or []
            )

    @api.depends("relation", "res_id")
    def _compute_record_ref(self):
        for rule in self:
            rule.record_ref = (
                "%s,%s" % (rule.relation, rule.res_id)
                if rule.relation and rule.res_id
                else False
            )

    @api.multi
    def _inverse_record_ref(self):
        for rule in self:
            ref = rule.record_ref
            if ref and ref._name != rule.relation:
                raise ValidationError(
                    _("The record must be a record of %s") % rule.relation
                )
            rule.res_id = ref.id if ref else 0

    @api.onchange("record_ref")
    def _onchange_record_ref(self):
        self.res_id = self.record_ref.id if self.record_ref else 0

    @api.depends("field_id", "operator", "selection_values", "value_boolean", "res_id")
    def _compute_condition(self):
        for rule in self:
            field = rule.field_id
            if not field:
                rule.condition = False
                continue
            if field.ttype == "selection":
                values = rule._selection_keys() or ["False"]
            elif field.ttype == "boolean":
                values = [str(bool(rule.value_boolean))]
            else:
                values = [str(rule.res_id) if rule.res_id else "False"]
            rule.condition = "%s %s %s" % (field.name, rule.operator, ", ".join(values))

    @api.multi
    def name_get(self):
        return [
            (rule.id, "%s: %s" % (rule.page_id.name or "", rule.condition or ""))
            for rule in self
        ]

    @api.constrains("field_id", "page_id", "selection_values")
    def _check_field(self):
        for rule in self:
            if rule.field_id.model != rule.page_id.model:
                raise ValidationError(
                    _("The field %(field)s is not a field of %(model)s")
                    % {"field": rule.field_id.name, "model": rule.page_id.model}
                )
            if rule.field_id.ttype not in RULE_FIELD_TYPES:
                raise ValidationError(
                    _("Only selection, boolean and many2one fields can be used")
                )
            if rule.field_id.ttype == "selection":
                info = self.env[rule.field_id.model].fields_get(
                    [rule.field_id.name], ["selection"]
                )
                allowed = [
                    "%s" % key
                    for key, dummy in info[rule.field_id.name].get("selection") or []
                ]
                wrong = [x for x in rule._selection_keys() if x not in allowed]
                if wrong:
                    raise ValidationError(
                        _("Values %(wrong)s are not allowed; use %(allowed)s")
                        % {"wrong": ", ".join(wrong), "allowed": ", ".join(allowed)}
                    )

    @api.onchange("field_id")
    def _onchange_field_id(self):
        self.selection_values = False
        self.value_boolean = False
        self.res_id = 0
        self.record_ref = False

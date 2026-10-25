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
    field_type = fields.Selection(related="field_id.ttype")
    relation = fields.Char(related="field_id.relation")
    operator = fields.Selection(
        [("=", "is"), ("!=", "is not")], required=True, default="="
    )
    selection_ids = fields.Many2many(
        "ir.model.fields.selection",
        string="Values",
        domain="[('field_id', '=', field_id)]",
        help="Selection field: any of these values",
    )
    value_boolean = fields.Boolean("Value", help="Boolean field: checked or not")
    res_id = fields.Many2oneReference(
        "Record id",
        model_field="relation",
        help="Many2one field: id of the record, 0 when the field is empty",
    )
    # the record of a many2one rule is picked as on the server actions: a
    # reference whose model is the comodel of the field
    relation_model_id = fields.Many2one("ir.model", compute="_compute_relation_model")
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

    @api.depends("relation")
    def _compute_relation_model(self):
        for rule in self:
            rule.relation_model_id = (
                self.env["ir.model"]._get_id(rule.relation) if rule.relation else False
            )

    @api.depends("relation", "res_id")
    def _compute_record_ref(self):
        for rule in self:
            rule.record_ref = (
                "%s,%s" % (rule.relation, rule.res_id)
                if rule.relation and rule.res_id
                else False
            )

    def _inverse_record_ref(self):
        for rule in self:
            rule.res_id = rule.record_ref.id if rule.record_ref else 0

    @api.onchange("record_ref")
    def _onchange_record_ref(self):
        self._inverse_record_ref()

    @api.depends("field_id", "operator", "selection_ids", "value_boolean", "res_id")
    def _compute_condition(self):
        for rule in self:
            field = rule.field_id
            if not field:
                rule.condition = False
                continue
            if field.ttype == "selection":
                values = rule.selection_ids.mapped("value") or ["False"]
            elif field.ttype == "boolean":
                values = [str(bool(rule.value_boolean))]
            else:
                values = [str(rule.res_id) if rule.res_id else "False"]
            rule.condition = "%s %s %s" % (field.name, rule.operator, ", ".join(values))

    @api.depends("page_id", "condition")
    def _compute_display_name(self):
        for rule in self:
            rule.display_name = "%s: %s" % (
                rule.page_id.name or "",
                rule.condition or "",
            )

    @api.constrains("field_id", "page_id")
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

    @api.onchange("field_id")
    def _onchange_field_id(self):
        self.selection_ids = False
        self.value_boolean = False
        self.res_id = 0
        self.record_ref = False

from odoo import fields, models
from odoo import api
from odoo.exceptions import ValidationError


class ApprovalCategory(models.Model):
    _inherit = 'approval.category'

    approver_sequence = fields.Boolean('Approvers Sequence?')
    line_manager_approval = fields.Selection([('approver', 'Is Approver'), ('required', 'Is Required Approver')],
                                             string="Employee's Line Manager")
    notify_even_when_refused = fields.Boolean(string='Notify Approvers Even If Refused')
    priority_type = fields.Selection([('high', 'Before Line Managers'), ('low', 'After Line Managers')], default='low',
                                     string='Approvers Priority Type')

    @api.constrains('approver_sequence')
    def _constrains_approver_sequence(self):
        if any(a.approver_sequence and not a.approval_minimum for a in self):
            raise ValidationError('')

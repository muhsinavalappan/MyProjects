from odoo import fields
from odoo import models
from odoo import api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    approval_block_id = fields.Many2one(
        'approval.block', string='Approval Block',
        compute="_compute_approval_block", inverse="_inverse_approval_block")

    @api.depends('amount_total')
    def _compute_approval_block(self):
        for record in self:
            records = self.approval_block_id.search(
                [('amount_limit', '<=', record.amount_total)])
            record.approval_block_id = max(records)

    def _inverse_approval_block(self):
        pass

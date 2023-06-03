from odoo import fields
from odoo import  models


class ApprovalBlock(models.Model):
    _name = "approval.block"
    _description = "Approval block for PO"
    _inherit = 'mail.thread'
    _order = 'amount_limit desc'

    name = fields.Char('Name')
    amount_limit = fields.Integer('Limit')

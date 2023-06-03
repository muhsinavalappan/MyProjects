from odoo import fields
from odoo import models


class CustomerInherit(models.Model):
    _inherit = 'res.partner'

    credit_limit = fields.Boolean('Active Credit Limit', default=True)
    warning_amt = fields.Float('Warning Amount')
    blocking_amt = fields.Float('Blocking Amount')
    block = fields.Boolean(compute='_compute_block')
    warn = fields.Boolean(compute='_compute_warn')
    blocking_msg = fields.Text('Blocking Message')
    warning_msg = fields.Text('Warning Message')

    def _compute_block(self):
        if self.credit > self.blocking_amt:
            self.block = True
        else:
            self.block = False

    def _compute_warn(self):
        if self.credit > self.warning_amt:
            self.warn = True
        else:
            self.warn = False

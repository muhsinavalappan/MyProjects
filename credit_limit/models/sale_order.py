from odoo import models, fields, api, _


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    amount_due = fields.Monetary(related='partner_id.credit')
    warn = fields.Boolean(related='partner_id.warn')

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        if self.partner_id.block:
            title = _("Blocking for %s") % self.partner_id.name
            message = self.partner_id.blocking_msg
            self.partner_id = False
            warning = {
                'title': title,
                'message': message
            }
            return {'warning': warning}
        elif self.partner_id.warn:
            title = _("Warning for %s") % self.partner_id.name
            message = self.partner_id.warning_msg
            warning = {
                'title': title,
                'message': message
            }
            return {'warning': warning}
        return {}

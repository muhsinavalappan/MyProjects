from odoo import fields
from odoo import models


class ResPartnerInherit(models.Model):
    _inherit = "res.partner"

    activate_p_limit = fields.Boolean("Activate Purchase Limit")
    purchase_limit = fields.Float("Purchase Limit")


class PosSessions(models.Model):
    _inherit = 'pos.session'

    def _loader_params_res_partner(self):
        result = super()._loader_params_res_partner()
        result['search_params']['fields'].append('activate_p_limit')
        result['search_params']['fields'].append('purchase_limit')
        return result

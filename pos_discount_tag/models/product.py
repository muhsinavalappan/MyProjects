from odoo import models
from odoo import api
from odoo import fields


class ProductInherit(models.Model):
    _inherit = 'product.product'

    disc_price_tag = fields.Float('Discount Price')
    old_price = fields.Float(
        'New Price', compute='_compute_old_price', store=True)

    @api.depends('disc_price_tag')
    def _compute_old_price(self):
        for rec in self:
            price = rec.lst_price-rec.disc_price_tag
            rec.lst_price = price
            rec.old_price = rec.lst_price+rec.disc_price_tag


class PosSessionsInherit(models.Model):
    _inherit = 'pos.session'

    def _loader_params_product_product(self):
        result = super()._loader_params_product_product()
        result['search_params']['fields'].append('disc_price_tag')
        result['search_params']['fields'].append('old_price')
        return result

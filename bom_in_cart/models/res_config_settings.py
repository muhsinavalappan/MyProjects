from odoo import models
from odoo import fields
from odoo import api
from ast import literal_eval


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    product_ids = fields.Many2many('product.template')

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'bom_in_cart.product_ids', self.product_ids.ids)
        print(res)
        return res

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        with_product = self.env['ir.config_parameter'].sudo()
        bom_products = with_product.get_param('bom_in_cart.product_ids')
        print(bom_products)
        res.update(product_ids=[
            (6, 0, literal_eval(bom_products))]if bom_products else False, )
        return res

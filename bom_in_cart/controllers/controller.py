from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request


class WebsiteSale(WebsiteSale):
    def cart(self, **post):
        val = super().cart(**post)
        product = eval(request.env['ir.config_parameter'].sudo().get_param(
            'bom_in_cart.product_ids'))
        val.qcontext.update({
            'value': product
        })
        return val


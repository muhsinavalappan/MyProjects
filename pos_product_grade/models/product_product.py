from odoo import fields
from odoo import models


class ProductTemplateInherit(models.Model):
    _inherit = "product.product"

    product_grade = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
    ], string="Grade", default='a')


class PosSessions(models.Model):
    _inherit = 'pos.session'

    def _loader_params_product_product(self):
        result = super()._loader_params_product_product()
        result['search_params']['fields'].append('product_grade')
        print(result)
        return result

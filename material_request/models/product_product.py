from odoo import models, fields


class ProductLines(models.Model):
    _name = "product.line"

    order_id = fields.Many2one('material.order')
    product_id = fields.Many2one(
        'product.product', string='Product', required=True)

    sequence = fields.Integer(string="Sequence", default=10)
    type = fields.Selection([('po', 'Purchase Order'),
                             ('it', 'Internal Transfer')],
                            default='po', string="Type")

    price_unit = fields.Float(
        string="Unit Price", related='product_id.lst_price',
        digits='Product Price', readonly=False,)
    product_qty = fields.Float('Quantity', default=1)
    location_id = fields.Many2one(
        'stock.location', string="Source Location",
        default=lambda self: self.env.ref('stock.stock_location_stock').id)
    location_dest_id = fields.Many2one(
        'stock.location', string="Destination Location",
        default=lambda self: self.env.ref(
            'stock.stock_location_components').id)
    operation_type_id = fields.Many2one(
        'stock.picking.type', string="Operation type",
        default=lambda self: self.env.ref('stock.picking_type_internal').id)

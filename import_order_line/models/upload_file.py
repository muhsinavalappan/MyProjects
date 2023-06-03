from odoo import fields
from odoo import models
from odoo import _
import openpyxl
import base64
from io import BytesIO
from odoo.exceptions import UserError


class UploadFile(models.Model):
    _name = "upload.file"

    file = fields.Binary('Upload File', required=True)

    def import_order_line(self):
        try:
            wb = openpyxl.load_workbook(
                filename=BytesIO(base64.b64decode(self.file)), read_only=True)
            ws = wb.active
            for record in ws.iter_rows(min_row=2, max_row=None, min_col=None,
                                       max_col=None, values_only=True):
                if record[0]:
                    product = self.env['product.product'].search(
                        [('name', '=like', record[0])])
                    if product:
                        active_id = self.env.context.get('active_ids')
                        vals = {
                            'product_id': product.id,
                            'name': record[1],
                            'product_uom': product.uom_id.id,
                            'price_unit': record[4],
                            'product_uom_qty': record[2],
                        }
                        sale_order = self.env['sale.order'].browse(active_id)
                        sale_order.update({
                            'order_line': [(0, 0, vals)]})
                    else:
                        new_product = self.env['product.product'].create({
                            'name': record[0],
                            'default_code': record[1],
                            'lst_price': record[4],

                        })
                        vals = {
                            'product_id': new_product.id,
                            'name': new_product.default_code,
                            'product_uom': new_product.uom_id.id,
                            'price_unit': record[4],
                            'product_uom_qty': record[2],

                        }
                        active_id = self.env.context.get('active_ids')
                        sale_order = self.env['sale.order'].browse(active_id)
                        sale_order.update({
                            'order_line': [(0, 0, vals)]})

        except:
            raise UserError(_('Please insert a valid file'))


class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

    def action_merge(self):
        for line in self.order_line:
            if line.id in self.order_line.ids:
                line_ids = self.order_line.filtered(
                    lambda m: m.product_id.id == line.product_id.id)
                quantity = 0
                for qty in line_ids:
                    quantity += qty.product_uom_qty
                line_ids[0].write({'product_uom_qty': quantity,
                                   'order_id': line_ids[0].order_id.id})
                line_ids[1:].unlink()

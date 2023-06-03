from odoo import fields
from odoo import models
from odoo import api
from odoo import _
from odoo.exceptions import ValidationError


class MaterialOrder(models.Model):
    _name = "material.order"
    _description = "Material Request Orders"
    _inherit = 'mail.thread'

    name = fields.Char(
        readonly=True, copy=False, default=lambda self: _('New'))
    employee_id = fields.Many2one(
        'hr.employee', string='Employee', required=True,
        default=lambda self: self.env.user.employee_id.id)
    manager_id = fields.Many2one(
        related='employee_id.parent_id', string='Manager')
    state = fields.Selection([
        ('draft', 'RFQ'),
        ('to approve', 'To Approve'),
        ('approved', 'Approved'),
        ('purchase', 'Purchase Order'),
        ('done', 'Done'),
        ('reject', 'Rejected'),
        ('cancel', 'Cancelled')
    ], default='draft')
    date = fields.Date('Date', default=fields.Date.today(),
                       required=False, readonly=False)
    order_ids = fields.One2many('product.line', 'order_id', required=True)
    po = fields.Char()
    transfer = fields.Char()

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'material.order') or _('New')
        res = super(MaterialOrder, self).create(vals)
        return res

    def button_confirm(self):
        self.write({
            'state': "to approve"
        })

    def btn_approve_manager(self):
        self.write({
            'state': "approved"
        })

    def btn_approve_head(self):
        self.write({
            'state': "purchase"
        })
        for line in self.order_ids:
            if line.type == 'po':
                self.env['purchase.requisition'].create({
                    'origin': self.name,
                    'line_ids': [(0, 0, {
                        'product_id': line.product_id.id,
                        'price_unit': line.price_unit,
                        'product_qty': line.product_qty,
                    })],
                })
            else:
                self.env['stock.move'].create({
                    'name': 'abcd',
                    'product_id': line.product_id.id,
                    'location_id': line.location_id.id,
                    'location_dest_id': line.location_dest_id.id,
                    'origin': self.name,
                })

    def action_purchase_order(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Purchase Orders',
            'view_mode': 'tree,form',
            'res_model': 'purchase.requisition',
            'domain': [('origin', '=', self.name)],
        }

    def action_internal_transfer(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Internal Transfers',
            'view_mode': 'tree',
            'view_id': self.env.ref('stock.view_move_tree').id,
            'res_model': 'stock.move',
            'domain': [('origin', '=', self.name)],

        }

    def btn_reject_head(self):

        self.write({
            'state': "reject"
        })

    @api.constrains('order_ids')
    def _constrains_order_ids(self):
        if not self.order_ids or len(self.order_ids) == 0:
            raise ValidationError(
                "You must add at least one product")

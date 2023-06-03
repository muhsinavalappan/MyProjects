# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Muhsina V (<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import models, fields, api


class DeliverySlot(models.Model):
    """ Model to create delivery slots"""
    _name = 'delivery.slot'
    _rec_name = 'delivery_date'

    delivery_date = fields.Date('Delivery Date')
    slot = fields.Many2one('slot.time', string="slot")
    product_id = fields.Many2one('product.product', string="Product")
    sale_order = fields.Many2one('sale.order')
    delivery_ids = fields.One2many('sale.order', 'slot_id',
                                   compute='_compute_sale_ids')
    delivery_limit = fields.Integer("Delivery Limit", default=100)
    total_delivery = fields.Integer("Total No of Deliveries",
                                    compute='_onchange_delivery_ids',
                                    stote=True)
    remaining_slots = fields.Integer("Available No of Deliveries",
                                     compute='_onchange_total_delivery')
    active = fields.Boolean('Active', default=True)

    @api.onchange('delivery_ids')
    def _onchange_delivery_ids(self):
        """sets the total deliveries of the delivery slot"""
        self.total_delivery = len(self.delivery_ids)

    @api.onchange('total_delivery', 'delivery_limit')
    def _onchange_total_delivery(self):
        """Finds remaining slots for each of the delivery slot"""
        self.remaining_slots = self.delivery_limit - self.total_delivery
        if self.remaining_slots <= 0:
            self.active = False

    def _compute_sale_ids(self):
        """Computing the related sale orders of each delivery slot"""
        for rec in self:
            sale_order = self.env['sale.order'].search(
                [('slot_per_product', '=', True)])
            for order in sale_order:
                for line in order.order_line:
                    if line.delivery_date == rec.delivery_date and \
                            line.slot == rec.slot:
                        rec.delivery_ids = [(4, order.id)]


class SlotTime(models.Model):
    """Model to create time slots"""
    _name = 'slot.time'

    name = fields.Char('Slot')
    slot_type = fields.Selection([('home', 'Home Hours'),
                                  ('office', 'Office Hours')])
    time_from = fields.Selection([
        ('0', '12:00 AM'),
        ('1', '1:00 AM'),
        ('2', '2:00 AM'),
        ('3', '3:00 AM'),
        ('4', '4:00 AM'),
        ('5', '5:00 AM'),
        ('6', '6:00 AM'),
        ('7', '7:00 AM'),
        ('8', '8:00 AM'),
        ('9', '9:00 AM'),
        ('10', '10:00 AM'),
        ('11', '11:00 AM'),
        ('12', '12:00 PM'),
        ('13', '1:00 PM'),
        ('14', '2:00 PM'),
        ('15', '3:00 PM'),
        ('16', '4:00 PM'),
        ('17', '5:00 PM'),
        ('18', '6:00 PM'),
        ('19', '7:00 PM'),
        ('20', '8:00 PM'),
        ('21', '9:00 PM'),
        ('22', '10:00 PM'),
        ('23', '11:00 PM')], string='Time From')
    time_to = fields.Selection([
        ('0', '12:00 AM'),
        ('1', '1:00 AM'),
        ('2', '2:00 AM'),
        ('3', '3:00 AM'),
        ('4', '4:00 AM'),
        ('5', '5:00 AM'),
        ('6', '6:00 AM'),
        ('7', '7:00 AM'),
        ('8', '8:00 AM'),
        ('9', '9:00 AM'),
        ('10', '10:00 AM'),
        ('11', '11:00 AM'),
        ('12', '12:00 PM'),
        ('13', '1:00 PM'),
        ('14', '2:00 PM'),
        ('15', '3:00 PM'),
        ('16', '4:00 PM'),
        ('17', '5:00 PM'),
        ('18', '6:00 PM'),
        ('19', '7:00 PM'),
        ('20', '8:00 PM'),
        ('21', '9:00 PM'),
        ('22', '10:00 PM'),
        ('23', '11:00 PM')], string='Time To')

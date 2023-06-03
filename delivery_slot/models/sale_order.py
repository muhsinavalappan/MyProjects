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
from datetime import timedelta
from odoo.addons.sale_stock.models.sale_order_line import SaleOrderLine
from odoo import models, fields


class SaleOrderLineInherit(models.Model):
    """Inheriting sale order line to add slot fields"""
    _inherit = 'sale.order.line'

    delivery_date = fields.Date("Delivery Date")
    slot = fields.Many2one('slot.time', string="Time Slot")
    delivery_slot = fields.Many2one('delivery.slot')

    def _prepare_procurement_values(self, group_id=False):
        """ Prepare specific key for moves or other components that will be
        created from a stock rule coming from a sale order line. This method
        could be overridden in order to add other custom key that could
        be used in move/po creation.
        """
        date_deadline = self.delivery_date or (
                self.order_id.date_order + timedelta(
            days=self.customer_lead or 0.0))
        date_planned = date_deadline - timedelta(
            days=self.order_id.company_id.security_lead)
        values = {
            'group_id': group_id,
            'sale_line_id': self.id,
            'date_planned': date_planned,
            'date_deadline': date_deadline,
            'route_ids': self.route_id,
            'warehouse_id': self.order_id.warehouse_id or False,
            'product_description_variants': self.with_context(
                lang=self.order_id.partner_id.lang).
            _get_sale_order_line_multiline_description_variants(),
            'company_id': self.order_id.company_id,
            'product_packaging_id': self.product_packaging_id,
            'sequence': self.sequence,
        }
        if self.order_id.slot_per_product:
            values.update({"slot_per_product": 'True'})
            if self.slot:
                values.update({'slot_time_id': self.slot.id})
        return values

    SaleOrderLine._prepare_procurement_values = _prepare_procurement_values


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    slot_per_product = fields.Boolean(
        string="Delivery Slot per Product", default=lambda self: self.env[
            'ir.config_parameter'].sudo().get_param(
            'DeliverySlot.enable_delivery_date'))
    slot_id = fields.Many2one('delivery.slot')
    slot_count = fields.Integer(compute='_compute_delivery_slot_count')
    is_delivery_slot = fields.Boolean(
        default=lambda self: self.env['ir.config_parameter'].sudo().get_param(
            'DeliverySlot.enable_delivery_date'))

    def action_confirm(self):
        if self.slot_per_product:
            for line in self.order_line:
                delivery_slot = self.env['delivery.slot'].search(
                    [('delivery_date', '=', line.delivery_date),
                     ('slot', '=', line.slot.id),
                     ('active', '=', True)])
                if delivery_slot:
                    delivery_slot.total_delivery += 1
                elif line.delivery_date and line.slot:
                    self.env['delivery.slot'].create({
                        'delivery_date': line.delivery_date,
                        'slot': line.slot.id,
                        'total_delivery': 1,
                    })
                else:
                    self.env['delivery.slot'].create({
                        'delivery_date': self.date_order,
                        'slot': line.slot.id,
                        'total_delivery': 1,
                    })

        return super().action_confirm()

    def _compute_delivery_slot_count(self):
        """Returns total no of delivery slot"""
        for record in self:
            recs = []
            if record.slot_per_product:
                for line in record.order_line:
                    slot_record = self.env['delivery.slot'].search([
                        ('delivery_date', '=', line.delivery_date),
                        ('slot', '=', line.slot.id),
                        ('active', '=', True)])
                    if slot_record:
                        recs.append(slot_record.id)
                rec = [*set(recs)]
                record.slot_count = len(rec)
            else:
                record.slot_count = 0

    def action_view_delivery_slot(self):
        """Returns all delivery slot related to the sale order"""
        rec = []
        for record in self:
            if record.slot_per_product:
                for line in record.order_line:
                    slot_record = self.env['delivery.slot'].search([
                        ('delivery_date', '=', line.delivery_date),
                        ('slot', '=', line.slot.id),
                        ('active', '=', True)])
                    if slot_record:
                        rec.append(slot_record.id)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Delivery Slots',
            'view_mode': 'tree,form',
            'res_model': 'delivery.slot',
            'domain': [('id', 'in', rec)],
            'context': "{'create': False}"
        }

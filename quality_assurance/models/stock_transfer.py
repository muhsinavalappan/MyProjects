# -*- coding: utf-8 -*-
from odoo import models, fields, _
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    alert_count = fields.Integer(compute='_compute_alert_count')

    def _compute_alert_count(self):
        """Function to find the no of quality alerts"""
        for record in self:
            record.alert_count = self.env['quality.alert'].search_count(
                [('source', '=', self.name)])

    def action_view_quality_alert(self):
        """ returns the quality alerts"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Quality Alerts',
            'view_mode': 'tree,form',
            'res_model': 'quality.alert',
            'domain': [('source', '=', self.name)],
            'context': "{'create': False}"
        }

    def button_validate(self):
        if self.alert_count == 0:
            products = self.move_ids_without_package.product_id
            for line in products:
                quality_recs = self.env['quality.measure'].search([
                    ('product_id', '=', line.id)])
                for i in quality_recs.trigger_ids:
                    if i.operation_type_id.id == self.picking_type_id.id:
                        self.env['quality.alert'].create({
                            'product_id': line.id,
                            'date': self.scheduled_date,
                            'source': self.name,
                        })
        if self.alert_count > 0:
            alerts = self.env['quality.alert'].search(
                [('source', '=', self.name)])
            for rec in alerts:
                if rec.test_ids:
                    for i in rec.test_ids:
                        if i.status == 'pass':
                            continue
                        elif i.status == 'fail':
                            raise ValidationError(
                                _('There are item failed in quality test.'))
                        else:
                            raise ValidationError(
                                _('There are item to perform the quality test.'))

                else:
                    raise ValidationError(
                        _('There are item to perform the quality test.'))

        res = super(StockPicking, self).button_validate()
        return res

    def action_set_quantities_to_reservation(self):
        if self.alert_count == 0:
            products = self.move_ids_without_package.product_id
            for line in products:
                quality_recs = self.env['quality.measure'].search([
                    ('product_id', '=', line.id)])
                for i in quality_recs.trigger_ids:
                    if i.operation_type_id.id == self.picking_type_id.id:
                        self.env['quality.alert'].create({
                            'product_id': line.id,
                            'date': self.scheduled_date,
                            'source': self.name,
                        })
        return super(StockPicking, self).action_set_quantities_to_reservation()

# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class QualityAssurance(models.Model):
    """ Model to create quality measures for each product"""
    _name = "quality.measure"
    _description = "Quality Measures"
    _inherit = 'mail.thread'

    name = fields.Char("Test", default='Color : Green')
    product_id = fields.Many2one(
        'product.product', required=True, string="Product")
    test_type = fields.Selection([
        ('qualitative', 'Qualitative'),
        ('quantitative', 'Quantitative')],
        string="Test Type", default='qualitative')

    trigger_ids = fields.One2many(
        'trigger.quality', 'quality_id', string="Trigger On")


class TriggerQualityLines(models.Model):
    """ quality measure trigger lines"""
    _name = 'trigger.quality'

    quality_id = fields.Many2one('quality.measure')
    operation_type_id = fields.Many2one('stock.picking.type')
    operation_type = fields.Char(related='operation_type_id.name')
    warehouse_id = fields.Many2one(related='operation_type_id.warehouse_id')
    sequence_id = fields.Many2one(related='operation_type_id.sequence_id')
    company_id = fields.Many2one(related='operation_type_id.company_id')


class QualityAlert(models.Model):
    """Model to generate quality alert"""
    _name = 'quality.alert'
    _inherit = 'mail.thread'

    name = fields.Char(
        readonly=True, default=lambda self: _('New'), copy=False)
    product_id = fields.Many2one('product.product')
    created_by = fields.Many2one(
        'res.users', domain=[('share', '=', False)],
        default=lambda self: self.env.user.partner_id)
    date = fields.Datetime('Scheduled Date')
    source = fields.Char('Source Operation')
    test_ids = fields.One2many('quality.test', 'quality_alert_id')

    @api.model
    def create(self, vals):
        """ function to generate sequence number for quality alert"""
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'quality.alert') or _('New')
        res = super(QualityAlert, self).create(vals)
        return res

    def action_generate_tests(self):
        """ function to generate test from button"""
        print(self.env.context)
        quality_records = self.env['quality.measure'].search(
            [('product_id', '=', self.product_id.id)])
        for rec in quality_records:
            self.env['quality.test'].create({
                'name': rec.name,
                'measure_id': rec.id,
                'quality_alert_id': self.id,
                'assigned_to': self.env.user.id,
                'product': self.product_id,
            })

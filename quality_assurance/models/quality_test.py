# -*- coding: utf-8 -*-
from odoo import models, fields, _


class QualityTest(models.Model):
    """ model to generate quality tests"""
    _name = "quality.test"
    _description = "Quality tests"
    _inherit = 'mail.thread'

    name = fields.Char(string="Name")
    test_type = fields.Selection(
        [('qualitative', 'Qualitative'),
         ('quantitative', 'Quantitative')],
        string="Test Type", default='qualitative')
    result = fields.Selection(
        [('satisfied', 'Satisfied'),
         ('failed', 'Not Satisfied')],
        string="Result", tracking=True)
    status = fields.Selection(
        [('pass', 'Passed'),
         ('fail', 'Failed')], tracking=True, string="Status")
    measure_id = fields.Many2one('quality.measure', string="Measure")
    quality_alert_id = fields.Many2one('quality.alert', string="Quality Alert")
    product = fields.Many2one(
        related='quality_alert_id.product_id', string="Product")
    assigned_to = fields.Many2one(
        'res.users', tracking=True, domain=[('share', '=', False)],
        string="Assigned To")
    quantitative_result = fields.Float(string="Quantitative Result")



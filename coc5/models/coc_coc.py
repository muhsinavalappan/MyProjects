from odoo import fields, models


class CocBot(models.Model):
    _name = "coc.coc"

    resistance = fields.Selection([
        ('Pass', 'Pass'),
        ('Fail', 'Fail')
    ], string="Resistance")


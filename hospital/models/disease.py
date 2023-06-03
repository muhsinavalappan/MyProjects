from odoo import fields, models


class Disease(models.Model):
    _name = "patient.disease"
    _description = "Diseases"
    _category = "hospital"
    _inherit = 'mail.thread'

    name = fields.Char(string='Disease Name')

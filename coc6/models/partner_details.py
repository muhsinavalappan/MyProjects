from odoo import fields, models


class PartnerDetails(models.Model):
    _name = "partner.details"
    # _inherit = 'ir.model.fields'

    partner_id = fields.Many2one('res.partner')
    details = fields.Char("Add a details")


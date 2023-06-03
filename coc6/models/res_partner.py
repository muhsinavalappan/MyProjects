from odoo import fields, models


class ResPartnerInherit(models.Model):
    _inherit = "res.partner"

    partner_details = fields.Properties(definition='team_id.lead_properties_definition')

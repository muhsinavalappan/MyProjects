from odoo import models
from odoo import fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    api_key = fields.Char('Open Weather API Key',
                          config_parameter='OpenWeather.api_key')

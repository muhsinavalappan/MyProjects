
from ast import literal_eval
from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    """Inherited the res.config.settings model to add a field to select the
    messages"""
    _inherit = 'res.config.settings'

    message_ids = fields.Many2many(
        'pos.custom.message')

    def set_values(self):
        """
        Override the 'set_values' method to save the selected messages as
        configuration parameters.
        """
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'pos_custom_message.message_ids', self.message_ids.ids)
        return res

    @api.model
    def get_values(self):
        """
        Override the 'get_values' method to retrieve the selected messages from
        configuration parameters.
        """
        res = super(ResConfigSettings, self).get_values()
        selected_message_ids = self.env['ir.config_parameter'].sudo().get_param(
            'pos_custom_message.message_ids')
        res.update(message_ids=[
            (6, 0, literal_eval(selected_message_ids))]
        if selected_message_ids else False, )
        return res

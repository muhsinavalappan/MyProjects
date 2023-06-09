
from ast import literal_eval
from odoo import models, fields


class POSCustomMessage(models.Model):
    """Model to manage custom popup messages for the Point of Sale system."""
    _name = 'pos.custom.message'
    _rec_name = 'title'

    message_type = fields.Selection([
        ('alert', 'Alert'),
        ('warn', 'Warning'),
        ('info', 'Information'),
    ], string="Message Type", default='alert')
    title = fields.Char(string="Title")
    message_text = fields.Char(string="Message Text")
    execution_time = fields.Float(string="Execution Time")
    pos_config = fields.Many2many('pos.config')


class PosSessionsInherit(models.Model):
    """Inherited model for extending the Point of Sale sessions."""
    _inherit = 'pos.session'

    def _pos_ui_models_to_load(self):
        """Add 'pos.custom.message' to the models to be loaded in the Point of
        Sale UI."""
        res = super()._pos_ui_models_to_load()
        res.append('pos.custom.message')
        return res

    def _loader_params_pos_custom_message(self):
        """Retrieve the loader parameters for 'pos.custom.message'."""
        ids = (self.env['ir.config_parameter'].sudo().get_param(
            'pos_custom_message.message_ids'))
        message_ids = self.browse(literal_eval(ids))

        return {
            'search_params': {
                'domain': [('id', 'in', message_ids.ids)],
                'fields': [
                    'message_type', 'title', 'message_text', 'execution_time',
                    'pos_config'
                ],
            }
        }

    def _get_pos_ui_pos_custom_message(self, params):
        """Get 'pos.custom.message' records based on the provided search
        parameters."""
        return self.env['pos.custom.message'].search_read(
            **params['search_params'])

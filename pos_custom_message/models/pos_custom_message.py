# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Muhsina V (<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from ast import literal_eval
from datetime import timedelta

from odoo import models, fields, api


class POSCustomMessage(models.Model):

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

    def show_popup(self):
        print('hhhhh')
        # you will need to store a value (is_running: True|False) in the database, maybe in ir.config_parameter
        # if current_hour not in (1, 2, 3, 4, 5):
        #     return None
        # elif is_running:
        #     return None
        # else:
        #     # Mark that the action is in process, have to commit to the database
        #     is_running = True
        #     self.env.cr.commit()
        #     # Then call your actual action function
        #     do_some_real_thing()
        #     # Mark that the action is done
        #     is_running = False


class ResConfigSettings(models.TransientModel):

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


class PosSessionsInherit(models.Model):
    _inherit = 'pos.session'

    def _pos_ui_models_to_load(self):
        res = super()._pos_ui_models_to_load()
        res.append('pos.custom.message')
        return res

    def _loader_params_pos_custom_message(self):
        print('loading params')
        ids = eval(self.env['ir.config_parameter'].sudo().get_param(
            'pos_custom_message.message_ids'))
        return {
            'search_params': {
                'domain': [('id', 'in', ids)],
                'fields': [
                    'message_type', 'title', 'message_text', 'execution_time',
                    'pos_config'
                ],
            }
        }

    def _get_pos_ui_pos_custom_message(self, params):
        return self.env['pos.custom.message'].search_read(
            **params['search_params'])



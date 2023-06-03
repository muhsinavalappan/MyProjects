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
from odoo import models, fields, api, _


class PosConfigInherit(models.Model):
    _inherit = 'pos.config'

    def show_popup(self):
        print('ff')
        message_ids = self.env['ir.config_parameter'].sudo().get_param(
            'pos_custom_message.message_ids')
        print(eval(message_ids))
        for msg_id in eval(message_ids):
            rec = self.env['pos.custom.message'].browse(msg_id)
            title = _(rec.title)
            message = rec.message_text
            warning = {
                'title': title,
                'message': message
            }
            return {'warning': warning}



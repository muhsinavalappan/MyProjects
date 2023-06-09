
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



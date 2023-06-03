# -*- coding: utf-8 -*-
import datetime
import logging

from odoo import http, _, fields
from odoo.http import request
from odoo.osv.expression import AND
from odoo.tools import format_amount
from odoo.addons.account.controllers.portal import PortalAccount
from odoo.addons.point_of_sale.controllers.main import PosController


class PosControllerInherit(PortalAccount):

    @http.route(['/pos/web', '/pos/ui'], type='http', auth='user')
    def pos_web(self, **k):
        val = super().pos_web(**k)

        # Fetch the message_ids from the system parameters
        message_ids = request.env['ir.config_parameter'].sudo().get_param(
            'pos_custom_message.message_ids')
        print(message_ids)

        # Fetch the messages from the model using the message_ids
        messages = request.env['pos.custom.message'].sudo().browse(
            eval(message_ids))

        # Iterate through the messages and display the popup
        for message in messages:
            time_float = message.execution_time  # Assuming time_float is a float value
            time_minutes = int(time_float * 60)  # Convert hours to minutes
            time_formatted = datetime.timedelta(minutes=time_minutes)
            # time = message.execution_time
            title = message.title
            body = message.message_text
            print(title, body, time_formatted)
            # Show the popup using the title and body
            # Implement your own logic to display the popup here

        return val

# # -*- coding: utf-8 -*-
# import logging
#
# from odoo import http, _, fields
# from odoo.http import request
# from odoo.osv.expression import AND
# from odoo.tools import format_amount
# from odoo.addons.account.controllers.portal import PortalAccount
# from odoo.addons.point_of_sale.controllers.main import PosController
#
#
# class PosControllerInherit(PortalAccount):
#
#     @http.route(['/pos/web', '/pos/ui'], type='http', auth='user')
#     def pos_web(self, **k):
#         val = super().pos_web(**k)
#         print(self, k)
#
#         # message_ids = self.env['ir.config_parameter'].sudo().get_param(
#         #     'pos_custom_message.message_ids')
#         # print(message_ids)
#         return val

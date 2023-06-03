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
{
    'name': 'Delivery Slot',
    'version': '16.0.1.0.0',
    'sequence': -300,
    'summary': "Time slot selection for deliveries",
    'description': "This module helps to choose delivery slot for each product from the cart.",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': ['base', 'sale_management', 'stock', 'account', 'website_sale'],
    'assets': {
        'web.assets_frontend': [
            'delivery_slot/static/src/js/Slot_time.js',
            'delivery_slot/static/src/js/delivery_slot.js',
        ],
    },
    'data': [
        'data/delivery_slot.xml',
        'security/ir.model.access.csv',
        'views/slot_time_views.xml',
        'views/delivery_slot_views.xml',
        'views/sale_order_views.xml',
        'views/res_config_settings.xml',
        'views/website_delivery_slot.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'licence': 'AGPL-3',
}

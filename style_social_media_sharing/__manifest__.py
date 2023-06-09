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
    'name': 'Style Social Media Sharing',
    'version': '16.0.1.0.0',
    'sequence': -400,
    'summary': "Customized Style for Social Media Sharing",
    'description': "This module helps to customize Social Media Sharing Style",
    'category': 'Website',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': ['base', 'website_sale'],
    'assets': {
        'web.assets_frontend': [
            'style_social_media_sharing/static/src/css/*',
        ],

    },
    'data': [
        'views/res_config_settings.xml',
        'views/share_social_media_template.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'licence': 'AGPL-3',
}

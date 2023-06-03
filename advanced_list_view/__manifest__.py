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
    'name': 'Advanced Listview',
    'version': '16.0.1.0.0',
    'sequence': -420,
    'description': "Advanced Listview- pdf, excel, csv and copy to clipboard",
    'summary': 'Advanced List View',
    'category': 'Hidden',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': ['base', 'web', 'account', 'sale'],
    'data': [
        'views/pdf_template.xml',
    ],
    'assets': {
    'web.assets_backend': [
        'advanced_list_view/static/src/js/list_controller.js',
        'advanced_list_view/static/src/xml/list_controller.xml',
        'advanced_list_view/static/src/xml/list_pagination.xml',

    ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
    'licence': 'AGPL-3',
}

# -*- coding: utf-8 -*-
{
    'name': "Quality",
    'version': '16.0.1.0.0',
    'sequence': -300,
    'summary': "Quality Checks of Products.",
    'depends': ['stock', 'purchase', 'sale_management'],
    'data': [
        'security/user_groups.xml',
        'security/ir_rules.xml',
        'security/ir.model.access.csv',
        'views/quality_views.xml',
        'views/quality_alert_view.xml',
        'views/stock_transfer_views.xml',
        'views/quality_test_views.xml',
    ],
    'application': True,
    'licence': 'LGPL-3',
}

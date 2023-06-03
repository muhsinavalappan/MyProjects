# -*- coding: utf-8 -*-
{
    'name': "CRM Dashboard",
    'version': '16.0.1.0.0',
    'sequence': 25,
    'summary': 'CRM Dashboard',
    'author': 'Muhsina v',
    'depends': ['crm', 'base', 'web', 'sale_management'],
    'data': [
        'views/dashboard_menu.xml',
        'views/sale_team_views.xml',
    ],
    'assets': {
        'web.assets_backend': {
            'https://cdn.jsdelivr.net/npm/chart.js',
            'crm_dashboard/static/src/css/dashboard.css',
            'crm_dashboard/static/src/css/style.scss',
            'crm_dashboard/static/src/xml/dashboard.xml',
            'crm_dashboard/static/src/js/dashboard.js',

        },
    },
    'installable': True,
    'application': False,
}
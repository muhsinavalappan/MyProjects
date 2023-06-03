{
    'name': 'Customer Credit Limit',
    'sequence': -121,
    'version': '16.0.1.0.0',
    'application': 'True',
    'installable': 'True',
    'depends': ['contacts', 'account', 'base', 'sale'],
    'data': [
        'views/res_partner.xml',
        'views/sale_order_views.xml',
    ]

}

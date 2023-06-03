{
    'name': 'Material Request',
    'sequence': -101,
    'version': '16.0.1.0.0',
    'category': 'purchase',
    'summary': 'material request orders',
    'application': True,
    'installable': True,
    'auto_install': False,
    'depends': ['purchase_requisition', 'base', 'sale_management', 'stock'],
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/material_request_views.xml',
        'views/material_request_menus.xml',
        'views/order_id.xml',

    ]
}

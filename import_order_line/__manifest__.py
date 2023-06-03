{
    'name': 'Import Order Lines',
    'sequence': -122,
    'version': '16.0.1.0.0',
    'application': 'True',
    'installable': 'True',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/upload_file.xml',
        'views/sale_order_views.xml',
    ]

}

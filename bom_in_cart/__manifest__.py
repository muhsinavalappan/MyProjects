{
    'name': 'Bill Of Material',
    'sequence': -151,
    'version': '16.0.1.0.0',
    'summary': 'BoM in website cart',
    'application': True,
    'installable': True,
    'auto_install': False,
    'depends': ['website', 'base', 'mrp', 'stock'],
    'data': [
        'views/res_config_settings.xml',
        'views/website_bom_lines.xml',
    ]
}

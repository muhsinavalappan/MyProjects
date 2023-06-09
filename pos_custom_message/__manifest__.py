
{
    'name': 'POS Custom Message',
    'version': '16.0.1.0.0',
    'sequence': -422,
    'description': "POS Screen custom popup messages",
    'summary': 'Custom popup messages in pos screen',
    'category': 'Hidden',
    'depends': ['base', 'point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/pos_custom_message_views.xml',
        'views/res_config_settings.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_custom_message/static/src/js/*.js',
            'pos_custom_message/static/src/xml/pos_popup_template.xml',
        ],
    },

    'installable': True,
    'auto_install': False,
    'application': True,
    'licence': 'AGPL-3',
}

{
    'name': 'QR Code Generator',
    'version': '16.0.1.0.0',
    'summary': 'QR Code Generator',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv'
    ],
    'assets': {
        'web.assets_backend': {
            'qr_code/static/src/xml/qr_icon.xml',
            'qr_code/static/src/xml/qr_template.xml',
            'qr_code/static/src/js/qr_icon.js',

        },

    },
    'installable': True,

}

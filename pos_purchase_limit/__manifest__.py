{
    'name': 'POS Purchase Limit',
    'sequence': -251,
    'version': '16.0.1.0.0',
    'summary': 'Purchase Limit in Pos',
    'application': True,
    'installable': True,
    'depends': ['point_of_sale', 'contacts'],
    'data': [
        'views/res_partner.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_purchase_limit/static/src/js/pos_popup.js',
            'pos_purchase_limit/static/src/js/pos_purchase_limit.js',
            'pos_purchase_limit/static/src/xml/pos_purchase_limit.xml',

        ],

    },
}

{
    'name': 'POS Product Grade',
    'sequence': -250,
    'version': '16.0.1.0.0',
    'summary': 'Product Grade in Pos',
    'application': True,
    'installable': True,
    'depends': ['point_of_sale', 'base'],
    'data': [
        'views/product_views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_product_grade/static/src/xml/receipt_pos.xml',
            'pos_product_grade/static/src/js/pos_receipt.js',

        ],
    },
}

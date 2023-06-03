{
    'name': "POS Discount Tag",
    'sequence': -252,
    'application':'true',
    'installable':'true',
    'depends': ['point_of_sale'],
    'data':[
        'views/product.xml',
    ],
    'assets':{
        'point_of_sale.assets':[
            'pos_discount_tag/static/src/css/discount_tag.scss',
            'pos_discount_tag/static/src/xml/discount_tag.xml',
            'pos_discount_tag/static/src/xml/pos_receipt.xml',
            'pos_discount_tag/static/src/js/discount_tag.js',
            'pos_discount_tag/static/src/js/pos_receipt.js',
],
    }
}
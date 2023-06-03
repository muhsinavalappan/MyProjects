{
    'name': 'Snippet',
    'sequence': -150,
    'version': '16.0.6.0.0',
    'application': True,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'sale', 'web', 'website'],
    'assets': {
        'web.assets_frontend': [
            'snippet/static/src/xml/carousel_view.xml',
            'snippet/static/src/css/snippet.css',
            'snippet/static/src/js/snippet.js',
        ],
    },
    'data': [
        'views/snippet_template.xml',
        'views/my_snippet.xml',

    ]

}

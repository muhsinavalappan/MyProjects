{
    'name': 'Upcoming Events',
    'sequence': -250,
    'version': '16.0.1.0.0',
    'installable': True,
    'application': True,
    'depends': ['base', 'website_event', 'web', 'utm', 'website'],
    'data': [
        'data/event_expire.xml',
        'security/ir.model.access.csv',
        'views/university_event.xml',
        'views/university.xml',
        'views/portal_event_template.xml',
        'views/portal_event_content.xml',
    ],

}
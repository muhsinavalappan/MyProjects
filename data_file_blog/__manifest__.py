{
    'name': 'Datafile Blog',
    'sequence': 10,
    'application': True,
    'installable': True,
    'depends': ['sale', 'base'],
    'data': [
        'data/data_record.xml',
        'security/ir.model.access.csv',
        'views/datafile_blog.xml',
        'views/delete_data.xml',
    ]
}

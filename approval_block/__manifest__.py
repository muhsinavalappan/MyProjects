{
    'name': 'Approval Block',
    'sequence': -120,
    'version': '16.0.1.0.0',
    'summary': 'Approval Block',
    'application': True,
    'installable': True,
    'depends': ['purchase', 'base'],
    'data': [
        'data/data_record.xml',
        'security/ir.model.access.csv',
        'views/approval_block_views.xml',
        'views/purchase_views.xml',
    ]
}

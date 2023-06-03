{
    'name': 'Hospital Management',
    'sequence': -150,
    'version': '16.0.6.0.0',
    'category': 'hospital',
    'summary': 'hospital management',
    'application': True,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'sale', 'web', 'hr', 'contacts', 'website'],
    'assets': {
        'web.assets_backend': [
            'hospital/static/src/js/action_manager.js'
        ],
        'web.assets_frontend': [
            'hospital/static/src/js/script.js',
            'hospital/static/src/css/new_patient.scss',
        ],
    },
    'data': [
        'data/token_action.xml',
        'security/user_groups.xml',
        'security/ir_rules.xml',
        'security/ir.model.access.csv',
        'wizard/report_wizard.xml',
        'data/website_menu.xml',
        # 'views/action_manager.xml',
        'views/patient_details_views.xml',
        'views/hospital_op_views.xml',
        'views/res_partner_views.xml',
        'views/disease_views.xml',
        'views/consultation_views.xml',
        'views/appointment_views.xml',
        'views/hospital_menus.xml',
        'views/patient_id_views.xml',
        'report/hospital_template.xml',
        'report/hospital_report.xml',
        'views/website_views.xml',
        'views/website_submit.xml',
        'views/website_create_patient.xml',

    ]

}

{
    'name': 'Attendance Report',
    'version': '16.0.1.0.0',
    'summary': 'Attendance report',
    'installable': True,
    'depends': ['hr', 'base', 'hr_attendance', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/attendance_report_wizard.xml',
        'report/attendance_report_action.xml',
        'report/attendance_report_template.xml',
        'data/email_template.xml',

    ]
}

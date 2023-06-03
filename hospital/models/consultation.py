from odoo import fields, models


class Consultation(models.Model):
    _name = "hospital.consultation"
    _description = "Consultation Details"
    _category = "hospital"
    _inherit = 'mail.thread'

    patient_id = fields.Many2one(
        'hospital.patient', string='Patient Card', required=True,
        readonly=False)
    name = fields.Many2one(
        string='Patient Name', related='patient_id.patient_name_id')
    consult_type = fields.Selection([
        ('op', 'OP'), ('ip', ' IP')],
        string="Consultation Type", required=True, default='op')
    doctor_id = fields.Many2one(
        'hr.employee', string='Doctor', domain=[('is_doctor', '=', 'True')],
        default=lambda self: self.env.user.partner_id.id, required=True)
    department_id = fields.Many2one(
        string='Department', related='doctor_id.department_id')
    date = fields.Date('Date', default=fields.Date.today(),
                       required=False, readonly=False, select=True)
    disease = fields.Many2one('patient.disease', string='Disease')
    diagnose = fields.Html(string='Diagnose')
    treatment_ids = fields.One2many('hospital.treatment', 'treatment_id')


class Treatment(models.Model):
    _name = "hospital.treatment"
    _description = "Treatment Details"

    medicine = fields.Text(string='Medicine')
    dose = fields.Char(string='Dose')
    days = fields.Text(string='Days')
    description = fields.Text(string='Description')
    treatment_id = fields.Many2one('hospital.consultation')

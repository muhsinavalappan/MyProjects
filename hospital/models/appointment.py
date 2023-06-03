from odoo import fields, models, api


class Appointment(models.Model):
    _name = "hospital.appointment"
    _description = "Appointment Details"
    _category = "hospital"
    _inherit = 'mail.thread'
    _rec_name = "patient_id"

    patient_id = fields.Many2one(
        'hospital.patient', string='Patient Card', required=True,
        readonly=False)
    name_id = fields.Many2one(
        string='Patient Name', related='patient_id.patient_name_id')
    doctor_id = fields.Many2one(
        'hr.employee', string='Doctor', domain=[('is_doctor', '=', 'True')],
        required=True)
    department_id = fields.Many2one(
        string='Department', related='doctor_id.department_id')
    date = fields.Datetime('Date', default=fields.Datetime.now,
                           required=False, readonly=False)
    token_no = fields.Integer(string='Token no', readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('appointment', 'Appointment'),
        ('op', ' OP')],
        string="Status", required=True, readonly=True, copy=False,
        tracking=True, default='draft')
    op_ticket = fields.Char(
        string="OP Ticket", store=True, copy=False, readonly=True)

    @api.model
    def create(self, vals):
        res = super(Appointment, self).create(vals)
        token = res.doctor_id.token_no
        res.doctor_id.token_no = token+1
        res.token_no = res.doctor_id.token_no
        token1 = res.doctor_id.token_no
        res.doctor_id.token_no = token1-1
        print(token)
        return res

    def btn_appointment_confirm(self):
        self.write({
            'state': "appointment"
        })

    def btn_op_convert(self):
        return {
            'name': 'hospital.op.form',
            'res_model': 'hospital.op',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': self.env.ref("hospital.view_hospital_op_form").id,
            'context': {
                'default_model': 'hospital.appointment',
                'default_patient_id': self.patient_id.id,
                'default_name': self.name_id.id,
                'default_doctor_id': self.doctor_id.id,
                'default_date': self.date,
                'default_token_no': self.token_no,
            },
        }

    def action_open_op(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'OP Ticket',
            'view_mode': 'tree,form',
            'res_model': 'hospital.op',
            'domain': [
                ('patient_id.id', '=', self.patient_id.id),
                ('doctor_id.id', '=', self.doctor_id.id),
                ('date', '=', self.date)
                       ],
            'context': "{'create': False}"
        }

    def get_patient_id(self, patient_val):
        record = self.env['hospital.patient'].search([('id', '=', patient_val)])
        for rec in record:
            print(rec.patient_name_id)
            values = {
                'patient_name_id': rec.patient_name_id.name
            }
            print(values)
            return values

    def get_dept_id(self, doctor):
        dept = self.env['hr.employee'].search([('id', '=', doctor)])
        for rec in dept:
            values = {
                'department': rec.department_id.name
            }
            return values

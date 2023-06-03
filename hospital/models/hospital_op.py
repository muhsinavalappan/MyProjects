from odoo import fields, models, api


class HospitalOp(models.Model):
    _name = "hospital.op"
    _description = "Hospital Patient OP"
    _category = "hospital"
    _inherit = 'mail.thread'

    patient_id = fields.Many2one(
        'hospital.patient', string='Patient Card', required=True,
        readonly=False)
    name = fields.Many2one(
        string='Patient Name', related='patient_id.patient_name_id')
    age = fields.Integer(related='patient_id.age')
    gender = fields.Selection(string="Gender", related='patient_id.gender')
    blood_group = fields.Selection(
        string="Blood Group", related='patient_id.blood_group')
    doctor_id = fields.Many2one(
        'hr.employee', string='Doctor', domain=[('is_doctor', '=', 'True')],
        required=True)
    department_id = fields.Many2one(
        string='Department', related='doctor_id.department_id')
    date = fields.Datetime('Date', default=fields.Datetime.now,
                           required=False, readonly=False,
                           related=False)
    token_no = fields.Integer(string='Token no', readonly=True, copy=False)
    company_id = fields.Many2one(
        'res.company', store=True, copy=False, string="Company",
        default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  related='company_id.currency_id')
    fee = fields.Float(related='doctor_id.fee', currency_field='currency_id')
    state = fields.Selection([
        ('draft', 'Draft'), ('op', ' OP'), ('invoiced', ' Invoiced')],
        string="Status", required=True, readonly=True,
        copy=False, tracking=True, default='draft')
    invoices = fields.Char(
        string="Invoices", store=True, copy=False, readonly=True)

    def button_op(self):
        self.write({
            'state': "op"
        })
        self.env['hospital.appointment'].search([
            ('patient_id', '=', self.patient_id.id)]).state = 'op'

    def reset_token_no(self):
        re_token = self.env['hr.employee'].search([('is_doctor', '=', 'True')])
        re_token.write({'token_no': 0})

    @api.model
    def create(self, vals):
        res = super(HospitalOp, self).create(vals)
        token = res.doctor_id.token_no
        res.doctor_id.token_no = token + 1
        res.token_no = res.doctor_id.token_no
        return res

    def button_fee_payment(self):
        self.write({
            'state': "invoiced"
        })
        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.name.id,
            'payment_reference': self.date,
            'invoice_line_ids': [(0, 0, {
                'name': 'OP Fee',
                'price_unit': self.fee,

            })],
        })
        return {
            'name': 'account.move.form',
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': self.env.ref("account.view_move_form").id,
            'res_id': invoice.id,
            'target': 'current'

        }

    def action_open_invoice(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoices',
            'view_mode': 'tree,form',
            'res_model': 'account.move',
            'domain': [('partner_id.id', '=', self.name.id),
                       ('payment_reference', '=', self.date)],
            'context': "{'create': False}"
        }

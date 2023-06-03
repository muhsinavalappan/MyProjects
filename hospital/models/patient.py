from odoo import fields
from odoo import models
from odoo import api
from odoo import _


class Patient(models.Model):
    _name = "hospital.patient"
    _description = "Patient"
    _category = "hospital"
    _inherit = 'mail.thread'

    name = fields.Char(readonly=True, default=lambda self: _('New'), copy=False)
    patient_name_id = fields.Many2one(
        'res.partner', string='Patient name', required=True)
    date_of_birth = fields.Date(string='DOB',
                                readonly=False, related='patient_name_id.dob')
    age = fields.Integer(string="Age", compute="_compute_age", store=True, copy=False)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    mobile = fields.Char(string="Mobile No", related='patient_name_id.mobile')
    telephone = fields.Char(
        string="Telephone", related='patient_name_id.phone')
    blood_group = fields.Selection([
        ('a', 'A'), ('b', 'B'), ('c', 'C'), ('o', 'O')])
    history_ids = fields.One2many('hospital.op', 'patient_id', readonly=True)

    @api.depends('date_of_birth')
    def _compute_age(self):
        if self.date_of_birth:
            for record in self:
                today = fields.Date.today()
                record.age = today.year - record.date_of_birth.year - (
                        (today.month, today.day) < (record.date_of_birth.month,
                                                    record.date_of_birth.day))

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'hospital.patient') or _('New')
        res = super(Patient, self).create(vals)
        return res


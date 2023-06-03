from odoo import fields, models


class ResPartnerInherit(models.Model):
    _inherit = "res.partner"

    dob = fields.Date(string="DOB")


class EmployeeInherit(models.Model):
    _inherit = "hr.employee"

    is_doctor = fields.Boolean(string="Doctor")
    token_no = fields.Integer(string="Token No", readonly=True)
    company_id = fields.Many2one(
        'res.company', store=True, copy=False, string="Company",
        default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one(
        'res.currency', string="Currency", related='company_id.currency_id')
    fee = fields.Float(string="Fee", currency_field='currency_id')

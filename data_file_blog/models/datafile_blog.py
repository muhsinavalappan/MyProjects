from odoo import fields, models


class ApprovalBlock(models.Model):
    _name = "datafile.blog"
    _inherit = 'mail.thread'
    _order = 'amount_limit desc'

    name = fields.Char('Name')
    amount_limit = fields.Integer('Limit')
    date = fields.Date('Date')

    def action_test(self):
        self.create({
            'name': 'New Record',
            'date': fields.Date.today()
        })

    def create_action(self):
        self.name_create(10)
        a= self.default_get(['name','limit'])
        print(a)

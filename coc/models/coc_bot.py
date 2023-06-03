from odoo import fields, models


class CocBot(models.Model):
    _name = "coc.bot"

    name = fields.Char(string="Name")
    partner_id = fields.Many2one('res.partner', string="Partner")

    def action_find_customer(self):
        partner_id = self.env['res.partner'].search([('name', '=', 'COC Bot')])
        self.partner_id = partner_id.id

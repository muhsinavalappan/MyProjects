from odoo import models
from odoo import fields


class UniversityEvent(models.Model):
    _name = "university.event"
    _inherit = 'mail.thread'
    _rec_name = 'u_name'

    u_name = fields.Many2one(
        'university.name', string="University", reqired=True)
    code = fields.Integer('University Code', related='u_name.code', store=True)
    u_type = fields.Char('University Type', related='u_name.type')
    u_event = fields.Many2one(
        'event.event', string="University Event", required=True)
    event_type = fields.Many2one(
        string='University Event Type', related='u_event.event_type_id')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'Ongoing'),
        ('expired', 'Expired'),
    ], default='draft')
    event_slot_ids = fields.One2many('event.slot', 'event_slot_id')

    def button_confirm(self):
        """ confirm button action"""
        print(fields.Date.today())
        self.state = 'ongoing'

    def event_expire(self):
        """ scheduled action for expired events"""
        today = fields.Date.today()
        record = self.env['university.event'].search([
            ('end_date', '<', today), ('state', '=', 'ongoing')
        ])
        print(record)
        for rec in record:
            if rec.end_date:
                if rec.end_date < fields.Date.today():
                    rec.state = 'expired'


class EventEvent(models.Model):
    """ event slot model"""
    _name = 'event.slot'

    event_slot_id = fields.Many2one('university.event')
    time = fields.Datetime('Time')
    content = fields.Char('Content')


class University(models.Model):
    """ university model"""
    _name = "university.name"

    name = fields.Char('University Name')
    code = fields.Integer("university Code")
    type = fields.Char('University Type')

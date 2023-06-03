from odoo import models
from odoo import fields
from odoo import api
from odoo.tools import date_utils


class SalesTeam(models.Model):
    _inherit = 'crm.team'

    lead_stage_id = fields.Many2one('crm.stage')


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'mark opportunity as same stage of sale team from ' \
                   'sale order when you confirm order'

    def _action_confirm(self):
        sale_team_state = self.team_id.lead_stage_id
        opportunity_id = self.opportunity_id
        if opportunity_id and sale_team_state:
            opportunity_id.stage_id = sale_team_state

        return super(SaleOrder, self)._action_confirm()


class CrmDashboard(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def get_data(self):
        """Returns data to the tiles of dashboard"""
        manager = self.env.user.has_group('sales_team.group_sale_manager')
        if manager:
            lead = self.search(
                [('type', '=', 'lead')])
            opportunity = self.search(
                [('type', '=', 'opportunity')])
        else:
            lead = self.search(
                [('user_id', '=', self.env.user.id), ('type', '=', 'lead')])
            opportunity = self.search(
                [('type', '=', 'opportunity'),
                 ('user_id', '=', self.env.user.id)])
        expected_revenue = round(sum(self.search(
            [('type', '=', 'opportunity'),
             ('company_id', '=', self.env.user.company_id.id)]).mapped(
            'expected_revenue')), 2)
        currency_id = self.env.user.company_id.currency_id.symbol
        order_id = round(
            sum(self.env['sale.order'].search([
                ('user_id', '=', self.env.user.id)]).mapped(
                'amount_total')), 2)
        won = self.search_count(
            [('stage_id.is_won', '=', True)])
        win_ratio = round(
            (won / (len(lead) + len(
                opportunity))) * 100, 2)
        return {
            'lead_templates': len(lead),
            'opportunity_templates': len(opportunity),
            'expected_revenue': expected_revenue,
            'currency_id': currency_id,
            'order_id': order_id,
            'win_ratio': win_ratio,
        }

    @api.model
    def get_year(self, lead_val):
        """Returns data of current year,month,week
           ,quarter to the tiles of dashboard"""
        currency_id = self.env.user.company_id.currency_id.symbol
        manager = self.env.user.has_group('sales_team.group_sale_manager')

        if lead_val == 'this_year':
            won = 0
            if manager:
                lead_templates = self.search(
                    [('type', '=', 'lead')]).filtered(
                    lambda x: x.create_date.year == fields.date.today().year)
                opportunity_templates = self.search(
                    [('type', '=', 'opportunity')]).filtered(
                    lambda x: x.create_date.year == fields.date.today().year)
            else:
                lead_templates = self.search(
                    [('user_id', '=', self.env.user.id),
                     ('type', '=', 'lead')]).filtered(
                    lambda x: x.create_date.year == fields.date.today().year)
                opportunity_templates = self.search(
                    [('type', '=', 'opportunity'),
                     ('user_id', '=', self.env.user.id)]).filtered(
                    lambda x: x.create_date.year == fields.date.today().year)
            expected_revenue = round(sum(self.search(
                [('type', '=', 'opportunity'),
                 ('company_id', '=', self.env.user.company_id.id)]).filtered(
                lambda x: x.create_date.year == fields.date.today(
                ).year).mapped('expected_revenue')), 2)
            order_id = round(sum(self.env['sale.order'].search(
                [('user_id', '=', self.env.user.id)]).filtered(
                lambda x: x.create_date.year == fields.date.today(
                ).year).mapped('amount_total')), 2)
            win = self.search(
                [('stage_id.is_won', '=', True)]).filtered(
                lambda x: x.create_date.year == fields.date.today().year)
            for i in win:
                won += 1
            win_ratio = round((won / (
                    len(lead_templates) + len(opportunity_templates))
                               ) * 100, 2)
        if lead_val == 'this_month':
            won = 0
            if manager:
                lead_templates = self.search(
                    [('type', '=', 'lead')]).filtered(
                    lambda x: x.create_date.month == fields.date.today().month)
                opportunity_templates = self.search(
                    [('type', '=', 'opportunity')]).filtered(
                    lambda x: x.create_date.month == fields.date.today().month)
            else:
                lead_templates = self.search(
                    [('user_id', '=', self.env.user.id),
                     ('type', '=', 'lead')]).filtered(
                    lambda x: x.create_date.month == fields.date.today().month)
                opportunity_templates = self.search(
                    [('type', '=', 'opportunity'),
                     ('user_id', '=', self.env.user.id)]).filtered(
                    lambda x: x.create_date.month == fields.date.today().month)
            expected_revenue = round(sum(self.search(
                [('type', '=', 'opportunity'),
                 ('company_id', '=', self.env.user.company_id.id)]).filtered(
                lambda x: x.create_date.month == fields.date.today(
                ).month).mapped('expected_revenue')), 2)
            order_id = round(sum(self.env['sale.order'].search(
                [('user_id', '=', self.env.user.id)]).filtered(
                lambda x: x.create_date.month == fields.date.today(
                ).month).mapped('amount_total')), 2)
            win = self.search(
                [('stage_id.is_won', '=', True)]).filtered(
                lambda x: x.create_date.month == fields.date.today().month)
            for i in win:
                won += 1
            win_ratio = round((won / (
                    len(lead_templates) + len(opportunity_templates))
                               ) * 100, 2)
        if lead_val == 'this_week':
            won = 0
            if manager:
                lead_templates = self.search(
                    [('type', '=', 'lead')]).filtered(
                    lambda x: x.create_date.isocalendar()[1] == fields.date.
                    today().isocalendar()[1])
                print(lead_templates)
                opportunity_templates = self.search(
                    [('user_id', '=', self.env.user.id)]).filtered(
                    lambda x: x.create_date.isocalendar()[1] == fields.date.
                    today().isocalendar()[1])
                print(opportunity_templates)
            else:
                lead_templates = self.search(
                    [('user_id', '=', self.env.user.id),
                     ('type', '=', 'lead')]).filtered(
                    lambda x: x.create_date.isocalendar()[1] == fields.date.
                    today().isocalendar()[1])
                print(lead_templates)
                opportunity_templates = self.search(
                    [('type', '=', 'opportunity'),
                     ('user_id', '=', self.env.user.id)]).filtered(
                    lambda x: x.create_date.isocalendar()[1] == fields.date.
                    today().isocalendar()[1])
                print(opportunity_templates)
            expected_revenue = round(sum(self.search(
                [('type', '=', 'opportunity'),
                 ('company_id', '=', self.env.user.company_id.id)]).filtered(
                lambda x: x.create_date.isocalendar()[1] == fields.date.today(
                ).isocalendar()[1]).mapped(
                'expected_revenue')), 2)
            print(expected_revenue)
            order_id = round(sum(
                self.env['sale.order'].search(
                    [('user_id', '=', self.env.user.id)]).filtered(
                    lambda x: x.create_date.isocalendar(
                    )[1] == fields.date.today().isocalendar()[1]).mapped(
                    'amount_total')), 2)
            print(order_id)
            win = self.search(
                [('stage_id.is_won', '=', True)]).filtered(
                lambda x: x.create_date.isocalendar()[1] == fields.date.today(
                ).isocalendar()[1])
            print(win)
            for i in win:
                won += 1
            if won == 0:
                win_ratio = 0
            if len(lead_templates) + len(opportunity_templates) == 0:
                win_ratio = 0
            else:
                win_ratio = round((won / (
                        len(lead_templates) + len(opportunity_templates))
                                   ) * 100, 2)
        if lead_val == 'this_quarter':
            today = fields.Date.today()
            quarter_start, quarter_end = date_utils.get_quarter(today)
            if manager:
                lead_templates = self.search(
                     [('type', '=', 'lead'),
                      ('create_date', '>=', quarter_start),
                      ('create_date', '<=', quarter_end)])
                opportunity_templates = self.search(
                    [('type', '=', 'opportunity'),
                     ('create_date', '>=', quarter_start),
                     ('create_date', '<=', quarter_end)])
            else:
                lead_templates = self.search(
                    [('user_id', '=', self.env.user.id),
                     ('type', '=', 'lead'),
                     ('create_date', '>=', quarter_start),
                     ('create_date', '<=', quarter_end)])
                opportunity_templates = self.search(
                    [('type', '=', 'opportunity'),
                     ('user_id', '=', self.env.user.id),
                     ('create_date', '>=', quarter_start),
                     ('create_date', '<=', quarter_end)])
            expected_revenue = round(sum(self.search(
                [('type', '=', 'opportunity'),
                 ('company_id', '=', self.env.user.company_id.id),
                 ('create_date', '>=', quarter_start),
                 ('create_date', '<=', quarter_end)]).mapped(
                'expected_revenue')), 2)
            order_id = round(sum(
                self.env['sale.order'].search(
                    [('user_id', '=', self.env.user.id),
                     ('create_date', '>=', quarter_start),
                     ('create_date', '<=', quarter_end)]).mapped(
                    'amount_total')), 2)
            won = self.env['crm.lead'].search_count(
                [('stage_id.is_won', '=', True),
                 ('create_date', '>=', quarter_start),
                 ('create_date', '<=', quarter_end)])
            win_ratio = round((won / (
                    len(lead_templates) + len(opportunity_templates))
                               ) * 100, 2)
        return {
            'lead_templates': len(lead_templates),
            'opportunity_templates': len(opportunity_templates),
            'expected_revenue': expected_revenue,
            'currency_id': currency_id,
            'order_id': order_id,
            'win_ratio': win_ratio,
        }

    @api.model
    def get_lead_chart(self):
        """Returns data to the graph of dashboard"""
        lead_template = {}
        opportunity = {}
        exp_revenue = {}
        team_id = self.env['crm.team'].search([])
        manager = self.env.user.has_group('sales_team.group_sale_manager')
        for i in team_id:
            lead_templates = self.search_count(
                [('type', '=', 'lead'), ('team_id', '=', i.id)])
            lead_template[i.name] = lead_templates
            opportunity_templates = self.search_count(
                [('type', '=', 'opportunity'), ('team_id', '=', i.id)])
            opportunity[i.name] = opportunity_templates
            expected_revenue = round(sum(self.search(
                [('type', '=', 'opportunity'), ('team_id', '=', i.id),
                 ('company_id', '=', self.env.user.company_id.id)]).mapped(
                'expected_revenue')), 2)
            exp_revenue[i.name] = expected_revenue
        return {
            'lead_templates': lead_template,
            'opportunity': opportunity,
            'expected_revenue': exp_revenue,
        }

    @api.model
    def get_lead_chart_values(self, lead_val):
        """Returns data of current month,year
           ,week,quarter to the graph of dashboard"""
        lead_template = {}
        team_id = self.env['crm.team'].search([])
        if lead_val == 'this_month':
            for i in team_id:
                lead_templates = self.env['crm.lead'].search(
                    [('type', '=', 'lead'), ('team_id', '=', i.id)]).filtered(
                    lambda x: x.create_date.month == fields.date.today().month)
                lead = len(lead_templates)
                lead_template[i.name] = lead
        if lead_val == 'this_year':
            for i in team_id:
                lead_templates = self.env['crm.lead'].search(
                    [('type', '=', 'lead'), ('team_id', '=', i.id)]).filtered(
                    lambda x: x.create_date.year == fields.date.today().year)
                lead = len(lead_templates)
                lead_template[i.name] = lead
        if lead_val == 'this_week':
            for i in team_id:
                lead_templates = self.env['crm.lead'].search(
                    [('type', '=', 'lead'), ('team_id', '=', i.id)]).filtered(
                    lambda x: x.create_date.isocalendar(
                    )[1] == fields.date.today().isocalendar()[1])
                lead = len(lead_templates)
                lead_template[i.name] = lead
        if lead_val == 'this_quarter':
            today = fields.Date.today()
            quarter_start, quarter_end = date_utils.get_quarter(today)
            for i in team_id:
                lead_templates = self.env['crm.lead'].search(
                    [('type', '=', 'lead'), ('team_id', '=', i.id),
                     ('create_date', '>=', quarter_start),
                     ('create_date', '<=', quarter_end)])
                lead = len(lead_templates)
                lead_template[i.name] = lead
        return {
            'lead_templates': lead_template,
        }

    @api.model
    def get_opportunity_chart_values(self, lead_val):
        """Returns data of current month,year
           ,week,quarter to the graph of dashboard"""
        opportunity = {}
        team_id = self.env['crm.team'].search([])
        if lead_val == 'this_month':
            for i in team_id:
                opportunity_templates = self.search(
                    [('type', '=', 'opportunity'),
                     ('team_id', '=', i.id)]).filtered(
                    lambda x: x.create_date.month == fields.date.today().month)
                lead = len(opportunity_templates)
                opportunity[i.name] = lead
        if lead_val == 'this_year':
            for i in team_id:
                opportunity_templates = self.search(
                    [('type', '=', 'opportunity'),
                     ('team_id', '=', i.id)]).filtered(
                    lambda x: x.create_date.year == fields.date.today().year)
                lead = len(opportunity_templates)
                opportunity[i.name] = lead
        if lead_val == 'this_week':
            for i in team_id:
                opportunity_templates = self.search(
                    [('type', '=', 'opportunity'),
                     ('team_id', '=', i.id)]).filtered(
                    lambda x: x.create_date.isocalendar(
                    )[1] == fields.date.today().isocalendar()[1])
                lead = len(opportunity_templates)
                opportunity[i.name] = lead
        if lead_val == 'this_quarter':
            today = fields.Date.today()
            quarter_start, quarter_end = date_utils.get_quarter(today)
            for i in team_id:
                opportunity_templates = self.search(
                    [('type', '=', 'opportunity'),
                     ('team_id', '=', i.id),
                     ('create_date', '>=', quarter_start),
                     ('create_date', '<=', quarter_end)])
                lead = len(opportunity_templates)
                opportunity[i.name] = lead
        return {
            'opportunity': opportunity,
        }

    @api.model
    def check_user_group(self):
        """Checking user group"""
        user = self.env.user
        if user.has_group('sales_team.group_sale_manager'):
            return True
        else:
            return False

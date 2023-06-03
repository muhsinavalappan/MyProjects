from dateutil.relativedelta import relativedelta
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo import http
from odoo.http import request
from odoo import fields, _
from odoo.addons.portal.controllers.portal import pager as portal_pager


class PortalAccount(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        """ returns the upcoming events count"""

        values = super()._prepare_home_portal_values(counters)
        today = fields.Date.today()
        three_month = fields.Date.today() + relativedelta(months=+3)
        if 'event_count' in counters:
            values['event_count'] = request.env[
                'university.event'].search_count([
                ('start_date', '<', three_month), ('start_date', '>=', today)
            ])
        return values

    def _get_event_searchbar_sortings(self):
        return {
            'date': {'label': _('Start Date'), 'order': 'start_date'},
            'u_name': {'label': _('University'), 'order': 'u_name'},
        }

    @http.route(['/upcoming/events', '/upcoming/events/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_upcoming_events(self, page=1, sortby=None, **kwargs):
        """ render the upcoming events to the template"""

        upcoming_event = request.env['university.event']

        today = fields.Date.today()
        three_month = fields.Date.today() + relativedelta(months=+3)

        if not sortby:
            sortby = 'date'

        url = "/upcoming/events"
        domain = [
            ('start_date', '<', three_month), ('start_date', '>=', today)]

        searchbar_sortings = self._get_event_searchbar_sortings()

        sort_order = searchbar_sortings[sortby]['order']

        pager_values = portal_pager(
            url=url,
            total=upcoming_event.search_count(domain),
            page=page,
            step=self._items_per_page,
            url_args={'sortby': sortby},
        )

        events = upcoming_event.sudo().search(
            domain, order=sort_order, limit=self._items_per_page,
            offset=pager_values['offset'])
        vals = {
            'name': events,
            'default_url': url,
            'page_name': 'event',
            'pager': pager_values,
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,

        }
        request.session['upcoming_events'] = vals['name'].ids[
                                                   :100]
        return request.render('upcoming_events.portal_event_template', vals)

# class EventPortalTemplate(http.Controller):
    @http.route(['/upcoming/events/<int:order_id>'], type='http', auth="public"
                , website=True)
    def portal_order_page(self, order_id, **kw):

        values = request.env['university.event'].sudo().browse(order_id)
        print(values)
        user = values.env.user

        vals = {
            'name': values,
            'user': user,
            'page_name': 'events',

        }
        return request.render(
            'upcoming_events.portal_upcoming_event_page', vals)

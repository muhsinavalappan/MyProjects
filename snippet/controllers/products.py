import itertools
import operator
from odoo import http
from odoo.http import request


class Sales(http.Controller):
    @http.route(["/total_product_sold"], type="json", auth="public")
    def sold_total(self):
        print('controller top')
        values = {}
        vals = []
        new_list = []
        products = request.env['product.template'].sudo().search([])
        for i in products:
            values.update({
                i: i.sales_count,
            })
        sorted_dict = dict(sorted(values.items(), key=operator.itemgetter(1),
                                  reverse=True))
        limit = dict(itertools.islice(sorted_dict.items(), 20))
        print('limit', limit)
        for i in limit:
            vals.append([
                i.name, i.id,
            ])
        print('vals', vals)
        # return vals
        for i in range(0, len(vals), 4):
            new_list.append(vals[i:i+4])
        print(new_list)
        return new_list

    @http.route(['/total_viewed_product'], type="json", auth="public")
    def most_viewed(self):
        website_products = request.env['website.track'].sudo().search([]).\
            filtered(lambda l: l.product_id).product_id
        print('website_products', website_products)
        values = [
            [rec.name, rec.product_tmpl_id.id]for rec in website_products]
        new_list = [values[i:i+4]for i in range(0, len(values), 4)]
        print(new_list)
        return new_list
        # return values

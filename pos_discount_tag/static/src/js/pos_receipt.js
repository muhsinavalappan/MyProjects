odoo.define('pos_discount_tag.receipt', function(require) {
    'use strict';
    var { Orderline } = require('point_of_sale.models');
    var Registries = require('point_of_sale.Registries');

    const PosOrderline = (Orderline) => class PosOrderline extends Orderline {
        export_for_printing() {
            var result = super.export_for_printing(...arguments);
            result.disc_price_tag = this.get_product().disc_price_tag;
            result.old_price = this.get_product().old_price;
            console.log(result.price)
            return result;
        }
    }
    Registries.Model.extend(Orderline, PosOrderline);

});
odoo.define('pos_discount_tag.OrderSummary', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');

    class ProductItem extends PosComponent {
        get price() {
            var org_price = this.env.pos.format_currency(
                this.env.pos.product.get_display_price());
            if (this.env.pos.get_product().disc_price_tag) {
                org_price = this.env.pos.get_product().old_price
            }
            return org_price;
        }
    }


    Registries.Component.extend(ProductItem);

    return ProductItem;
});
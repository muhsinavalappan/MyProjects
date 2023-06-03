odoo.define('pos_product_grade.pos', function(require) {
    "use strict";

    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    var rpc = require('web.rpc');

    const CustomPurchaseLimit = ProductScreen =>
        class extends ProductScreen {
            async _onClickPay() {
                if (!this.currentOrder.get_partner()) {
                    this.showPopup('ErrorPopup', {
                        title: ('Customer Required'),
                        body: ('Select a Customer'),
                    });
                } else {
                    super._onClickPay()
                }
            }

        };

    Registries.Component.extend(ProductScreen, CustomPurchaseLimit);

    return ProductScreen;
});
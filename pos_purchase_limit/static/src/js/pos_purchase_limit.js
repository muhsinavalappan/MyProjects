odoo.define('pos_product_grade.purchase', function(require) {
    "use strict";

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');

    const CustomPurchaseLimit = PaymentScreen =>
        class extends PaymentScreen {
            async validateOrder(isForceValidate) {
                var customer = this.currentOrder.get_partner()
                var active_limit = customer.activate_p_limit
                var limit = customer.purchase_limit
                var order_amount = this.currentOrder.selected_paymentline.amount
                if (active_limit) {
                    if (order_amount > limit) {
                        this.showPopup('ErrorPopup', {
                            title: ('Warning'),
                            body: ('Your Purchase Limit Amount is:' + limit),
                        });
                    } else {
                        super.validateOrder(...arguments);
                    }
                }
            }
        };

    Registries.Component.extend(PaymentScreen, CustomPurchaseLimit);

    return PaymentScreen;
});
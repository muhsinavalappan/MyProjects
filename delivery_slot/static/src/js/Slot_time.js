odoo.define('delivery_slot_time_hours.cart_line', function(require) {
    'use strict';

    var publicWidget = require('web.public.widget');
    const ajax = require('web.ajax');

    publicWidget.registry.websiteSlotTimeHours = publicWidget.Widget.extend({
        selector: '.slot-time-div',
        events: {
            'change input[type="radio"][name="slot_hour"]': '_onSlotTime',
        },

        _onSlotTime: function(ev) {
            var selected_option = $("input[type='radio'][name='slot_hour']:checked").val()
            ajax.jsonRpc('/shop/cart/get_option', "call", {
                    'selected_option': selected_option,
                })
                .then(function(result) {
                    const selects = document.querySelectorAll('select');
                    const input = document.querySelector('input');

                    selects.forEach((select) => {
                        const options = Array.from(select.options);
                        options.forEach((option) => {
                            option.remove();
                        });
                        result.forEach((item) => {
                            let newOption = new Option(item[1], item[0]);
                            select.add(newOption, undefined);
                        });
                    });
                });
        },
    });
});
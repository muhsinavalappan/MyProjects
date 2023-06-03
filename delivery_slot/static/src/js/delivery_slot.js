odoo.define('delivery_slot.cart', function(require) {
    'use strict';

    var publicWidget = require('web.public.widget');
    var core = require('web.core');
    const ajax = require('web.ajax');

    publicWidget.registry.websiteDeliverySlot = publicWidget.Widget.extend({
        selector: '.delivery_slot_div',
        events: {
            'change #slot_id': '_onDateChange',
            'change #date': '_onDateChange',
        },


        _onDateChange: function(ev) {
            if (ev.currentTarget.id == 'date') {
                var delivery_date = ev.currentTarget.value
                var line_id = $(ev.currentTarget).attr('data-line-id')
                ajax.jsonRpc('/shop/cart/set_delivery_date', "call", {
                    'delivery_date': delivery_date,
                    'line_id': line_id
                });

            }
            if (ev.currentTarget.id == 'slot_id') {
                var delivery_slot = ev.currentTarget.value
                var line_id = $(ev.currentTarget).attr('data-line-id')
                ajax.jsonRpc('/shop/cart/set_delivery_slot', "call", {
                    'delivery_slot': delivery_slot,
                    'line_id': line_id
                });

            }
        },
    });
});
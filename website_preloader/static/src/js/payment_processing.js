odoo.define('website_preloader.payment_post_processing', function(require) {
    'use strict';

    var PaymentPostProcessing = require('payment.post_processing');
    var _t = require('web.core')._t;
    const rpc = require('web.rpc');


    PaymentPostProcessing.include({
        displayLoading: function() {
            var msg = _t("We are processing your payment, please wait ...");
            rpc.query({
                model: 'ir.config_parameter',
                method: 'get_param',
                args: ['website_preloader.loader_style'],
            }).then(function(result) {
                console.log(result)
                var imgSrc = '/website_preloader/static/src/img/' + result + '.png';
                console.log(imgSrc)
                $.blockUI({
                    'message': '<h2 class="text-white"><img src="' + imgSrc + '"/>' +
                        '    <br />' + msg +
                        '</h2>'
                });
            })
        },
    });

    return PaymentPostProcessing;
});
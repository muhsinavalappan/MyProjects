odoo.define('snippet.dynamic', function(require) {
    var PublicWidget = require('web.public.widget');
    var rpc = require('web.rpc');
    var core = require('web.core');
    var Qweb = core.qweb;

    var Dynamic = PublicWidget.Widget.extend({
        selector: '.dynamic_snippet',
        start: async function() {
            var self = this;
            await rpc.query({
                route: "/total_product_sold",
                params: {},
            }).then(function(result) {
                var name = result;
                name[0].set_active = true;
                $('.qweb_most_sold').append(Qweb.render('snippet.product_snippets', {
                    name
                }));
            });
            await rpc.query({
                route: '/total_viewed_product',
                params: {},
            }).then(function(result) {
                var viewed = result;
                viewed[0].set_active = true;
                $('.qweb_most_sold').append(Qweb.render('snippet.product_view_snippet', {
                    viewed
                }));
            });

        },
    });
    PublicWidget.registry.DynamicSnippet = Dynamic;
    return Dynamic;
});
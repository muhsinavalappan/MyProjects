odoo.define('qr_code.qrcode', function(require) {
    "use strict";
    var core = require('web.core');
    var QWeb = core.qweb;
    var SystrayMenu = require('web.SystrayMenu');
    var Widget = require('web.Widget');
    var rpc = require('web.rpc');

    var ActionMenu = Widget.extend({


        template: 'qr_code.icon',
        events: {
            'click .my_icon': '_onclickIcon',
            'click #generate': '_onclickGenerate',
            'click #reset': '_onclickReset',
        },
        start: function () {
        this.$(".test_div").hide();
        },


        /**
         *defining function
         **/
        _onclickIcon: async function(ev) {
        /** function to execute when clicking the systray icon **/
            if ($(".test_div").is(":visible")) {
                $(".test_div").hide();
            } else {
                $(".test_div").show();
                }
            },

        _onclickGenerate: async function(){
        /** function to execute when clicking the generate button **/
            var input_text = $('#input_text').val();
            rpc.query({
                    model: 'qr.code',
                    method: 'generate_qr',
                    args: [,input_text],
                }).then(function(result) {
                var src = "data:image/png;base64,"+result
                $("#qr_img").attr('src', src)
                });
        },
        _onclickReset: async function(){
        /** function to reset the QR Code **/

            $("#qr_img").attr('src', "")
        },


        });
    SystrayMenu.Items.push(ActionMenu);
    return ActionMenu;
});
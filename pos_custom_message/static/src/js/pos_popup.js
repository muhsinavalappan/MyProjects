odoo.define('pos_custom_message.pos_popup', function (require) {
"use strict";
    var gui = require('point_of_sale.Gui');
    const Registries = require('point_of_sale.Registries');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const PosCustomMessage = ProductScreen =>
        class extends ProductScreen {
            setup() {
                super.setup();
                console.log(this,'???????????????????')
                console.log(this.env.pos.pos_custom_message)
                const msg = this.env.pos.pos_custom_message;
                if(msg){
                    console.log('/////////////')
                    var current_time = new Date().toLocaleTimeString();
                    console.log(current_time)
                    msg.forEach((message) =>{
                        console.log(message);
                        var execution_time = message.execution_time;
                        if(execution_time != current_time){
                        console.log('kkkkk')
                         var options = {
                            'title': message.title,
                            'body': message.message_text,
                            'type': type,
                            };
                        this.pos.gui.show_popup('alert', options);
                        }
                        else{console.log(';;;;;')}
//                        var hour = Math.floor(execution_time);
//                        var minute = execution_time - hour;
//                        console.log(hour,minute,',,,,,,,,,,')
//                        if (minute.length < 2) {
//                            minute = minute + '0' ;
//                            }
//                        var time = hour + ':' + minute;
//
//                        console.log(time);
//                        console.log(execution_time);

                    });
//                    var options = {
//                'title': title,
//                'body': message,
//                'type': type,
//                };
//                    this.pos.gui.show_popup('alert', options);
//                }
                }
        }
        };

    Registries.Component.extend(ProductScreen, PosCustomMessage);

    return ProductScreen;
});


















//odoo.define('pos_custom_message.pos_popup', function(require) {
//    "use strict";
//
//    const ProductScreen = require('point_of_sale.ProductScreen');
//    const PartnerListScreen = require('point_of_sale.PartnerListScreen')
//    const PaymentScreen = require('point_of_sale.PaymentScreen')
//    const Registries = require('point_of_sale.Registries');
//    var rpc = require('web.rpc');
//    var self = this;
//
//    const PosCustomMessage = ProductScreen =>
//        class extends ProductScreen {
//            setup() {
//                    console.log('pos product screen........................................')
//                    console.log(this)
//                    console.log(this.env.posbus)
//                    console.log(this.env.pos)
//                    super.setup();
//
//                }
//
//
//        };
//
//    Registries.Component.extend(ProductScreen, PosCustomMessage);
//
//    return ProductScreen;
//});
//
//
//
//
////console.log('kkkkkkkkkkkk')
////odoo.define('pos_custom_message.popup_notification', function (require) {
////    "use strict";
////
////    var bus = require('bus.bus');
////
////    bus.bus.add_channel_callback('pos_custom_message.popup_notification', function (notifications) {
////        _.each(notifications, function (notification) {
////            // Handle the notification data and display the message in the POS interface
////            var type = notification.type;  // "warning", "info", etc.
////            var title = notification.title;  // The title of the message
////            var message = notification.message;  // The content of the message
////
////            // Display the message in the POS interface using appropriate methods
////            // For example, you can use 'pos.gui.show_popup' to show a popup window
////
////            // Example using 'show_popup' method:
////            var options = {
////                'title': title,
////                'body': message,
////                'type': type,
////            };
////            this.pos.gui.show_popup('alert', options);
////        });
////    });
////});

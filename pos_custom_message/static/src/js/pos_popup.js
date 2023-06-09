console.log('kkkkkkkkkkkk')
odoo.define('pos_custom_message.popup_notification', function (require) {
    "use strict";

    var bus = require('bus.bus');

    bus.bus.add_channel_callback('pos_custom_message.popup_notification', function (notifications) {
        _.each(notifications, function (notification) {
            // Handle the notification data and display the message in the POS interface
            var type = notification.type;  // "warning", "info", etc.
            var title = notification.title;  // The title of the message
            var message = notification.message;  // The content of the message

            // Display the message in the POS interface using appropriate methods
            // For example, you can use 'pos.gui.show_popup' to show a popup window

            // Example using 'show_popup' method:
            var options = {
                'title': title,
                'body': message,
                'type': type,
            };
            this.pos.gui.show_popup('alert', options);
        });
    });
});

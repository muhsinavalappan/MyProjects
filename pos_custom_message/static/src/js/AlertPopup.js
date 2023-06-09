odoo.define('point_of_sale.AlertPopup', function(require) {
    'use strict';

    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');
    const {
        _lt
    } = require('@web/core/l10n/translation');

    /**
     * CustomMessageAlertPopup component for displaying custom messages as an alert popup.
     * Inherits from AbstractAwaitablePopup.
     */
    class CustomMessageAlertPopup extends AbstractAwaitablePopup {
        setup() {
            super.setup();
        }
    }
    CustomMessageAlertPopup.template = 'CustomMessageAlertPopup';
    CustomMessageAlertPopup.defaultProps = {
        confirmText: _lt('Ok'),
        title: '',
        body: '',
    };
    // Add the CustomMessageAlertPopup component to the Point of Sale registries.
    Registries.Component.add(CustomMessageAlertPopup);

    return CustomMessageAlertPopup;
});
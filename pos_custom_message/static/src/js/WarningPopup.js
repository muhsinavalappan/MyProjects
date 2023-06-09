odoo.define('point_of_sale.WarningPopup', function(require) {
    'use strict';

    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');
    const {
        _lt
    } = require('@web/core/l10n/translation');

    /**
     * CustomMessageWarnPopup component for displaying custom messages as a warning popup.
     * Inherits from AbstractAwaitablePopup.
     */
    class CustomMessageWarnPopup extends AbstractAwaitablePopup {
        setup() {
            super.setup();
        }
    }
    CustomMessageWarnPopup.template = 'CustomMessageWarnPopup';
    CustomMessageWarnPopup.defaultProps = {
        confirmText: _lt('Ok'),
        title: '',
        body: '',
    };

    // Add the CustomMessageWarnPopup component to the Point of Sale registries.
    Registries.Component.add(CustomMessageWarnPopup);

    return CustomMessageWarnPopup;
});
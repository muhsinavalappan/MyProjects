odoo.define('point_of_sale.InfoPopup', function(require) {
    'use strict';

    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');
    const {
        _lt
    } = require('@web/core/l10n/translation');

    /**
     * CustomMessageInfoPopup component for displaying custom messages as an informational popup.
     * Inherits from AbstractAwaitablePopup.
     */
    class CustomMessageInfoPopup extends AbstractAwaitablePopup {
        setup() {
            super.setup();
        }
    }
    CustomMessageInfoPopup.template = 'CustomMessageInfoPopup';
    CustomMessageInfoPopup.defaultProps = {
        confirmText: _lt('Ok'),
        title: '',
        body: '',
    };

    // Add the CustomMessageInfoPopup component to the Point of Sale registries.
    Registries.Component.add(CustomMessageInfoPopup);

    return CustomMessageInfoPopup;
});
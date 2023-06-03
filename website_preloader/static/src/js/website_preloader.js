/** @odoo-module **/
import {
    WebsitePreview
} from '@website/client_actions/website_preview/website_preview';
import {
    patch
} from "@web/core/utils/patch";
const {
    useState
} = owl;
const rpc = require('web.rpc');
var self = this;
patch(WebsitePreview.components.BlockPreview.prototype, 'website_preview_style', {
    /**
     * @override
     */
    setup() {
        this._super(...arguments);
        this.spin_state = useState({
            style: ''
        })
        const self = this;
        rpc.query({
            model: 'ir.config_parameter',
            method: 'get_param',
            args: ['website_preloader.loader_style'],
        }).then(function(result) {
            self.spin_state.style = result
        })

    }
});
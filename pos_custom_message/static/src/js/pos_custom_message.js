/** @odoo-module */

import {
    PosGlobalState
} from 'point_of_sale.models';
import Registries from 'point_of_sale.Registries';
const NewPosGlobalState = (PosGlobalState) => class NewPosGlobalState extends PosGlobalState {
    async _processData(loadedData) {

        await super._processData(...arguments);

        this.pos_custom_message = loadedData['pos.custom.message'];

    }
}
Registries.Model.extend(PosGlobalState, NewPosGlobalState);
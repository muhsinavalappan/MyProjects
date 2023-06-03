odoo.define('pos_product_grade.models', function(require) {
    "use strict";
    var { Orderline } = require('point_of_sale.models');
    var Registries = require('point_of_sale.Registries');

    const CustomOrderline = (Orderline) => class CustomOrderline extends Orderline {
        export_for_printing() {
            var result = super.export_for_printing(...arguments);
            result.product_grade = this.get_product().product_grade;
            return result;
        }
    }
    Registries.Model.extend(Orderline, CustomOrderline);
});
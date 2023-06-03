odoo.define("hospital.appointment", function(require) {
    "use strict";

    var publicWidget = require('web.public.widget');
    var rpc = require("web.rpc");


    publicWidget.registry.WebsiteForm = publicWidget.Widget.extend({
          selector: ".main_div",
          events: {
                'change select[name="name"]': '_onPatientChange',
                'change select[name="doctor_id"]': '_onDoctorChange',
          },

          _onPatientChange : function(ev){
            var model = 'hospital.appointment';
            var patient_val = this.$('#name').val()
            console.log(patient_val)
            rpc.query({
                model: model,
                method: 'get_patient_id',
                args: [,patient_val],
            }).then(function (data) {
                console.log(data);
                var a = Object.keys(data)
                var b = Object.values(data)
                console.log(a,b);

                $('#patient_name_id').val(b);

                });



        },

        _onDoctorChange : function(ev){
            var model = 'hospital.appointment';
            var doctor = this.$('#doctor_id').val()
            console.log(doctor)

            rpc.query({
                model: model,
                method: 'get_dept_id',
                args: [,doctor],
            }).then(function (data) {
                console.log(data);
                var c = Object.keys(data)
                var d = Object.values(data)
                console.log(c,d);

                $('#department').val(d);

                });



        },

    });
});
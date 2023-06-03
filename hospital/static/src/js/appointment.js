$('.patient_name').on('click',function(e){
    var patient = $(this);
    rpc.query({
            model: 'hospital.patient',
            method: 'create_opp_portal',
            args: [{
                contact_name: $('.new_opp_form .contact_name').val(),
                title: $('.new_opp_form .title').val(),
                description: $('.new_opp_form .description').val(),
            }],
        })
        .done(function(response){
            if (response.errors) {
                $('#new-opp-dialog .alert').remove();
                $('#new-opp-dialog div:first').prepend("<div class='alert alert-danger'>" + response.errors + "</div>");
                $btn.prop('disabled', false);

            }
            else {
                window.location = '/my/opportunity/' + response.id;
            }
        })
        .fail(function() {
            $btn.prop('disabled', false);
        });
    return false;
});
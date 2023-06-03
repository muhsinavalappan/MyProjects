from odoo import http
from odoo.http import request


class WebsiteForm(http.Controller):
    @http.route(['/appointment'], type='http', auth="user", website=True)
    def appointment(self):
        patient = request.env['hospital.patient'].search([])
        doctor = request.env['hr.employee'].search([
            ('is_doctor', '=', 'True')
        ])
        values = {

            'patients': patient,
            'doctors': doctor,

        }
        return http.request.render("hospital.online_appointment_form", values)

    @http.route(['/appointment/submit'], type='http', auth="public",
                website=True)
    def appointment_submit(self, **kw):
        val = {
            'patient_id': kw.get('name'),
            'name_id': kw.get('patient_name_id'),
            'doctor_id': kw.get('doctor_id'),
            'date': kw.get('date'),
        }
        request.env['hospital.appointment'].create(val)
        return http.request.render(
            "hospital.submit_form", {})

    @http.route(['/appointment/create'], type='http', auth="user",
                website=True)
    def patient_create(self):
        partner = request.env['res.partner'].search([])
        val = {
            'partners': partner,
        }

        return http.request.render("hospital.online_patient_form", val)

    @http.route(['/appointment/create/submit'], type='http', auth="public",
                website=True)
    def patient_submit(self, **kw):
        name = kw.get('patient_name_id')
        print(name)
        dob = kw.get('date')

        card = request.env['hospital.patient'].sudo().create({
            'patient_name_id': name,
        })

        return http.request.render(
            "hospital.submit_patient_card", {
                'card_no': card.name,
            })

    @http.route(['/appointment/create/new'], type='http', auth="user",
                website=True)
    def patient_create_new(self):
        return http.request.render("hospital.online_new_patient_form", {})

    @http.route(['/appointment/create/new/submit'], type='http', auth="public",
                website=True)
    def patient_submit_new(self, **kw):
        name = kw.get('name')
        dob = kw.get('date')
        partner = request.env['res.partner'].sudo().create({
            'name': name,
            'display_name': name,
            'dob': dob
        })
        card = request.env['hospital.patient'].sudo().create({
            'patient_name_id': partner.id
        })
        return http.request.render(
            "hospital.submit_patient_card", {
                'card_no': card.name,
            })

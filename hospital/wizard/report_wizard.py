import json
import io
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError
from odoo.tools import date_utils
try:
    from odoo.tools.misc import xlsxwriter
except ImportError:
    import xlsxwriter


class HospitalReportWizard(models.TransientModel):
    _name = "hospital.report.wizard"

    patient_id = fields.Many2one('res.partner')
    doctor_id = fields.Many2one('hr.employee', string='Doctor',
                                domain=[('is_doctor', '=', 'True')])
    from_date = fields.Date()
    to_date = fields.Date()
    disease_id = fields.Many2one('patient.disease')
    department_id = fields.Many2one(related='doctor_id.department_id')

    def print_pdf(self):
        query = """
        SELECT  hospital_patient.name , res_partner.name,
         hospital_consultation.date,
        hr_employee.name, hr_department.name,patient_disease.name
        FROM public.hospital_patient
        inner join public.res_partner
         on hospital_patient.patient_name_id =res_partner.id
        inner join public.hospital_consultation
         on hospital_patient.id= hospital_consultation.patient_id
        inner join public.hr_employee
         on hospital_consultation.doctor_id= hr_employee.id
        inner join public.hr_department
         on hr_employee.department_id= hr_department.id
        left join public.patient_disease
         on hospital_consultation.disease= patient_disease.id
        WHERE 1=1"""

        if self.patient_id:
            query += """ AND res_partner.id ='%s'""" % self.patient_id.id
        if self.doctor_id:
            query += """ AND hr_employee.id ='%s'""" % self.doctor_id.id
        if self.disease_id:
            query += """ AND patient_disease.id='%s'""" % self.disease_id.id
        if self.from_date:
            query +=\
                """ AND hospital_consultation.date >='%s'""" % self.from_date
        if self.to_date:
            query +=\
                """ AND hospital_consultation.date <='%s'""" % self.to_date
        if self.from_date and self.to_date:
            if self.from_date > self.to_date:
                raise ValidationError(" From date is greater than To date")

        self.env.cr.execute(query)
        sql_data = self.env.cr.fetchall()
        print(sql_data)
        if not sql_data:
            raise ValidationError("No Records Found")
        data = {
            'form': self.read()[0],
            'sql_data': sql_data
        }
        return self.env.ref(
            'hospital.action_report_hospital').report_action(None, data=data)

    def print_xlsx(self):
        query = """
                SELECT  hospital_patient.name , res_partner.name,
                 hospital_consultation.date,
        hr_employee.name, hr_department.name,patient_disease.name
        FROM public.hospital_patient
        inner join public.res_partner
         on hospital_patient.patient_name_id =res_partner.id
        inner join public.hospital_consultation
         on hospital_patient.id= hospital_consultation.patient_id
        inner join public.hr_employee
         on hospital_consultation.doctor_id= hr_employee.id
        inner join public.hr_department
         on hr_employee.department_id= hr_department.id
        left join public.patient_disease
         on hospital_consultation.disease= patient_disease.id
                WHERE 1=1"""
        if self.patient_id:
            query += """ AND res_partner.id ='%s'""" % self.patient_id.id
        if self.doctor_id:
            query += """ AND hr_employee.id ='%s'""" % self.doctor_id.id
        if self.disease_id:
            query += """ AND patient_disease.id='%s'""" % self.disease_id.id
        if self.from_date:
            query += \
                """ AND hospital_consultation.date >='%s'""" % self.from_date
        if self.to_date:
            query += \
                """ AND hospital_consultation.date <='%s'""" % self.to_date
        if self.from_date and self.to_date:
            if self.from_date > self.to_date:
                raise ValidationError(" From date should be less than To date")

        self.env.cr.execute(query)
        sql_data = self.env.cr.fetchall()
        if not sql_data:
            raise ValidationError("No Records Found!!")
        data = {
            'id': self.id,
            'patient_id': self.patient_id.name,
            'doctor_id': self.doctor_id.name,
            'from_date': self.from_date,
            'to_date': self.to_date,
            'disease_id': self.disease_id.name,
            'sql_data': sql_data
        }
        return {
            'type': 'ir.actions.report',
            'data': {'model': 'hospital.report.wizard',
                     'options': json.dumps(data,
                                           default=date_utils.json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Excel Report',
                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, data, response):
        from_date = data['from_date']
        to_date = data['to_date']
        patient = data['patient_id']
        doctor = data['doctor_id']
        disease = data['disease_id']
        sql_data = data['sql_data']
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        sheet.set_column(1, 6, 18)
        cell_format = workbook.add_format(
            {'font_size': '12px', 'align': 'center'})
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '13px'})
        txt = workbook.add_format({'font_size': '10px', 'align': 'center'})
        sheet.merge_range('D3:E3', 'MEDICAL REPORT', head)
        row = 5
        col = 1
        if patient:
            sheet.write(row, col, 'Patient ', cell_format)
            sheet.write(row, col+1,  patient, txt)
            row += 1
        if from_date:
            sheet.write(row, col, 'Date From ', cell_format)
            sheet.write(row, col+1, from_date, txt)
            row += 1
        if to_date:
            sheet.write(row, col, 'Date To ', cell_format)
            sheet.write(row, col+1, to_date, txt)
            row += 1
        if doctor:
            sheet.write(row, col, 'Doctor ', cell_format)
            sheet.write(row, col+1, doctor, txt)
            row += 1
        if disease:
            sheet.write(row, col, 'Disease ', cell_format)
            sheet.write(row, col+1, disease, txt)
            row += 1

        if sql_data:
            sl_no = 1
            col = 0
            row += 2
            sheet.write(row, col, 'SL No', cell_format)
            col += 1
            sheet.write(row, col, 'OP', cell_format)
            if not patient:
                col += 1
                sheet.write(row, col, 'Patient', cell_format)
            col += 1
            sheet.write(row, col, 'Date', cell_format)
            if not doctor:
                col += 1
                sheet.write(row, col, 'Doctor', cell_format)
            if not disease:
                col += 1
                sheet.write(row, col, 'Disease', cell_format)
            row += 1

            for line in sql_data:
                row += 1
                col = 0
                sheet.write(row, col, sl_no, txt)
                col += 1
                sheet.write(row, col, line[0], txt)
                if not patient:
                    col += 1
                    sheet.write(row, col, line[1], txt)
                col += 1
                sheet.write(row, col, line[2], txt)

                if not doctor:
                    col += 1
                    sheet.write(row, col, line[3], txt)
                if not disease:
                    col += 1
                    sheet.write(row, col, line[5], txt)
                sl_no += 1

        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()

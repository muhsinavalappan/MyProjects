import base64

from odoo import models
from odoo import fields
from odoo.exceptions import ValidationError


class AttendanceReportWizard(models.Model):
    """ wizard for printing the attendance report """
    _name = "attendance.report.wizard"

    employee_id = fields.Many2one('hr.employee')
    from_date = fields.Date()
    to_date = fields.Date()

    def print_attendance_report(self):
        """ Returns the data into the report template by
        executing the query"""

        query = """select name as employee,check_in,check_out,
        round(worked_hours::numeric,2)
         from hr_attendance
         inner join hr_employee
         on hr_employee.id=employee_id
         WHERE 1=1"""
        if self.employee_id:
            query += """ and hr_employee.id ='%s'""" % self.employee_id.id
        if self.from_date:
            query += \
                """ AND hr_attendance.check_in >='%s'""" % self.from_date
        if self.to_date:
            query += \
                """ AND hr_attendance.check_out <='%s'""" % self.to_date
        if self.from_date and self.to_date:
            if self.from_date > self.to_date:
                raise ValidationError(" From date is greater than To date")
        self.env.cr.execute(query)
        sql_data = self.env.cr.fetchall()
        if not sql_data:
            raise ValidationError("No Records Found")

        data = {
            'model_id': self.id,
            'to_date': self.to_date,
            'from_date': self.from_date,
            'employee_id': self.employee_id.name,
            'sql_data': sql_data,
        }
        return self.env.ref(
            'attendance_report.action_attendance_report').report_action(
            None, data=data)

    def send_email_pdf_report(self):
        """ sending the pdf attendance report to hr manager"""

        query = """select name as employee,check_in,check_out,
                round(worked_hours::numeric,2)
                 from hr_attendance
                 inner join hr_employee
                 on hr_employee.id=employee_id
                 WHERE 1=1"""
        if self.employee_id:
            query += """ and hr_employee.id ='%s'""" % self.employee_id.id
        if self.from_date:
            query += \
                """ AND hr_attendance.check_in >='%s'""" % self.from_date
        if self.to_date:
            query += \
                """ AND hr_attendance.check_out <='%s'""" % self.to_date
        if self.from_date and self.to_date:
            if self.from_date > self.to_date:
                raise ValidationError(" From date is greater than To date")
        self.env.cr.execute(query)
        sql_data = self.env.cr.fetchall()
        if not sql_data:
            raise ValidationError("No Records Found")

        data = {
            'model_id': self.id,
            'to_date': self.to_date,
            'from_date': self.from_date,
            'employee_id': self.employee_id.name,
            'sql_data': sql_data,
        }

        attendance_report_id = self.env.ref(
            'attendance_report.action_attendance_report')
        report_id = attendance_report_id._render_qweb_pdf(attendance_report_id,
                                                          self.id, data)
        data_record = base64.b64encode(report_id[0])
        ir_values = {
            'name': "Attendance Report.pdf",
            'type': 'binary',
            'datas': data_record,
            'store_fname': data_record,
            'mimetype': 'application/pdf',
            'res_model': 'attendance.report.wizard'
        }
        data_id = self.env['ir.attachment'].sudo().create(ir_values)
        template = self.env.ref('attendance_report.email_template_attendance')
        template.attachment_ids = [(6, 0, [data_id.id])]
        manager = self.env['res.groups'].search([
            ('category_id', '=', 'Attendances')])
        mail = [i.login for i in manager.users]
        cc = mail.pop(0)

        email_values = {'email_to': mail[0],
                        'email_from': self.env.user.login,
                        '0': cc
                        }
        template.send_mail(self.id, email_values=email_values,
                           force_send=True)
        template.attachment_ids = [(6, 0, [data_id.id])]
        return True

try:
    import qrcode
except ImportError:
    qrcode = None
try:
    import base64
except ImportError:
    base64 = None
from io import BytesIO
from odoo import models


class QRCode(models.TransientModel):

    _name = "qr.code"

    def generate_qr(self, input_text):
        """method to generate QR code"""
        # if qrcode and base64:
        qr = qrcode.QRCode(
            version=7,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=3,
            border=5,
        )
        qr.add_data("Input : ")
        qr.add_data(input_text)
        qr.make(fit=True)
        img = qr.make_image()
        temp = BytesIO()
        img.save(temp, format="PNG")
        qr_image = base64.b64encode(temp.getvalue())
        return qr_image

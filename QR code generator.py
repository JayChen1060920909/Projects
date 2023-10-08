# Project Name: QR code generator
# Creator: Jay Chen
# Create Date: 2017/8/5

import qrcode


def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=20,
                       border=2)

    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black',backcolor='white')
    img.save(file_name)

# Input text to generate QR code
text = "https://www.instagram.com/"

# File name to save the QR code image
file_name = 'QR_code.jpeg'

generate_qr_code(text, file_name)
print(f"QR code save as {file_name}")



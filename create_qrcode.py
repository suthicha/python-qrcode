# import qrcode
import qrcode

qr = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10, 
    border=2, 
)
qr.add_data('www.google.com')

qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
 
# img.show()
img.save('qr_google.jpg')
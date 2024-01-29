import qrcode
from PIL import Image
qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 20, border = 10,)
print("Enter Link: ")
str = input()
qr.add_data(str)
qr.make(fit = True)
img = qr.make_image(fill_color = "red", back_color = "white")
img.save("Generated_QR.png")

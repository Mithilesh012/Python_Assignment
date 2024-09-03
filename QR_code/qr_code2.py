import qrcode
from PIL import Image

qr=qrcode.QRCode(version = 1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=20,border=4,)
qr.add_data("https://www.youtube.com/watch?v=i2xxhRTs5Uc")
qr.make(fit=True)
img=qr.make_image(fill_color="gray",back_color="white")
img.save("carry_youtube(web).png")

import qrcode
from urllib.parse import urlparse

#Day 1: QR Code Generator

def create_qrcode(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=2,
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = 'red', back_color = 'black')
    img.save(file_name)

url = input("Enter a link to turn into a QR Code: ")
filename = urlparse(url).netloc.split('.')[1] + ".png"
create_qrcode(url, filename)
print("Made QR Code!")

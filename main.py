import qrcode

def generate_qrcode(url):
 
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    return img

if __name__ == "__main__":
    url = "https://google.com"
    img = generate_qrcode(url)
    img.save("qrcode.png")
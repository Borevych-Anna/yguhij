import qrcode

def make_qr(url):
    qr = qrcode.make(url)
    qr.save("output/qr_code.png")
    qr.show()

    print("QR-код збережено")
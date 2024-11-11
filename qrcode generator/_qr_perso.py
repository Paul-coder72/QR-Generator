import qrcode
from qrcode.constants import ERROR_CORRECT_L

def GenerateQrCode():

    color1 = input("Enter the first color : ")
    color2 = input("Enter the color of background : ")
    size = int(input("Enter the size of the QRCode (1-40) : "))
    name = input("Enter the name of the QRCode : ")

    qr = qrcode.QRCode(
        version=size,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=5
    )

    qr.add_data(input("Enter the text to be encoded: "))
    qr.make(fit=True)


    img = qr.make_image(fill_color=color1, back_color=color2)
    img.save(f"{name}.png")

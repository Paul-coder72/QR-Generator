import cv2

def QrRead():
    
    d = cv2.QRCodeDetector()

    val, points, qrcode = d.detectAndDecode(cv2.imread(input("Enter the path to the QR code image: ")))

    print("Decoded Data:", val)
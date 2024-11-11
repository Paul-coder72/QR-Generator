import cv2
import qrcode
from qrcode.constants import ERROR_CORRECT_L

from _qr_perso import GenerateQrCode
from _qrRead import QrRead

print("\nBienvenue dans ce lecteur/encodeur de QRCodes ! \n 1. Créer un QRCode \n 2. Lire un QRCode \n")
rep = input("Que voulez-vous faire ? ")

if rep == "1":
    GenerateQrCode()

if rep == "2":
    QrRead()
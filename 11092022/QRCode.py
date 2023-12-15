import pyqrcode
import png

qr_Code = pyqrcode.create('54564')

qr_Code.png("Number.png", scale=5)
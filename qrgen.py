import qrcode

qr0 = qrcode.QRCode(
  version=1,
  error_correction=qrcode.constants.ERROR_CORRECT_L,
  box_size=3,
  border=2,
)

qr1 = qrcode.QRCode(
  version=1,
  error_correction=qrcode.constants.ERROR_CORRECT_L,
  box_size=3,
  border=2,
)

qr2 = qrcode.QRCode(
  version=1,
  error_correction=qrcode.constants.ERROR_CORRECT_L,
  box_size=3,
  border=2,
)

qr0.add_data('96boards.org')
qr0.make(fit=True)

img = qr0.make_image().convert('RGBA')
img.save("images/qrcode-96b.png")

qr1.add_data('http://www.shiratech-solutions.com/products/fpga-mezzanine-2/')
qr1.make(fit=True)

img = qr1.make_image().convert('RGBA')
img.save("images/qrcode-stc.png")

qr2.add_data('https://www.96rocks.com/')
qr2.make(fit=True)

img = qr2.make_image().convert('RGBA')
img.save("images/qrcode-96r.png")



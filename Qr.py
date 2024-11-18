import qrcode
img = qrcode.make("https://www.linkedin.com/in/surya-pratap-singh-44188b255/")
img.save("img.png", scale = 12)
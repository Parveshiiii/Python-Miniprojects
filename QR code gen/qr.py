import qrcode as QR

def create(content, filename):
    img = QR.make(content)
    img.save(filename)
    return f"here is you file saved at {filename}"
    

result = create("https://www.bing.com/hp?mobref=0&setmkt=en-in&setlang=en-in", "example.png")
print(result)

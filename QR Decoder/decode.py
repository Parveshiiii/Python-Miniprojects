from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("your-image-path-here")

result = decode(img)

for obj in result:
    data = obj.data.decode('utf-8')
    print("decoded data", data)

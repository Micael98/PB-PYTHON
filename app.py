from PIL import Image
model = Image.open("image.jpg")
# im.show()

w, h = model.size
for x in range(w):
    for y in range(h):
        impb = model.getpixel((x, y))
        fx = (impb[0] + impb[1] + impb[2])//3
        model.putpixel((x, y), (fx, fx, fx))
model.save("image.jpg")
model.show("image.jpg")

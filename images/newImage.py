from PIL import ImageColor, Image

# 'RGBA' is the mode. (100, 100) is the tuple for the width and height.
im = Image.new('RGBA', (100, 100))

# Here, getpixel(): parameter: position
# (0, 0, 0, 0) : transparent black
print('Pixel at top: ', im.getpixel((0, 0)))

# putpixel() have parmeters: position, color:RGB
for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210))

for x in range(100):
    for y in range(50, 100):
        im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))

im.save('newPixel.png')


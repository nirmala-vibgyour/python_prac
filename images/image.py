from PIL import Image
catIm = Image.open('cat.jpg')
# image parameters
print(catIm.size)
width, height = catIm.size
print(width, height)
print(catIm.filename)
print(catIm.format)
print(catIm.format_description)

# changing the file format
catIm.save('cat.png')

# creating new image
im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImage.png')
im2 = Image.new('RGBA', (20, 20))
im2.save('transparentImage.png')

# cropping
croppedIm = catIm.crop((650,212,2800,3000))
croppedIm.save('cropped.png')


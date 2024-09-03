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
croppedIm = catIm.crop((750,280,1750,1360))
croppedIm.save('cropped.png')

# size of the cropped image
print(croppedIm.size)

# resize  of the cropped image
width, height = croppedIm.size
passportsizedIm = croppedIm.resize((384, 384), resample=Image.Resampling.LANCZOS)
passportsizedIm.save('passport.png')

# making a sheet of passport size image
catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = passportsizedIm.size
catCopyTwo = catIm.copy()
for left in range(0, catImWidth, faceImWidth):
    for top in range(0, catImHeight, faceImHeight):
        # print(left, top)
        catCopyTwo.paste(passportsizedIm, (left, top))
catCopyTwo.save('sheet.jpg')

# copy paste one photo into another
catIm = Image.open('cat.jpg')
catCopyIm = catIm.copy()
catCopyIm.paste(passportsizedIm, (0, 0))
catCopyIm.paste(passportsizedIm, (400, 500))
catCopyIm.save('pasted.png')

# rotating and flipping images
catIm.rotate(90).save('rotated90.png')
catIm.rotate(180).save('rotated180.png')
catIm.rotate(270).save('rotated270.png')
catIm.rotate(6).save('rotated6.png')
catIm.rotate(6, expand=True).save('rotated6_expanded.png')

# mirror flip
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')



from PIL import Image

imcatlogo = Image.open('logoCat.jpg')
imcatlogo.save('logoCat.png')
imbarcode = Image.open('barCode.png')
imscancode = Image.open('QRcode.jpg')
imscancode.save('QRCode.png')

imcatlogonew = Image.open('logoCat.png')
imscancodenew = Image.open('QRcode.png')

imresizedcatlogo = imcatlogonew.resize((384, 384), resample=Image.Resampling.LANCZOS)
imresizedbarcode = imbarcode.resize((384, 384), resample=Image.Resampling.LANCZOS)
imresizedscancode = imscancodenew.resize((384, 384), resample=Image.Resampling.LANCZOS)


imsample = Image.new('RGBA', (1200, 1200))

for x in range(1200):
    for y in range(1200):
        imsample.putpixel((x, y), (255, 255, 255))

imsample.paste(imresizedcatlogo, (0, 0))
imsample.paste(imresizedbarcode, (390, 390))
imsample.paste(imresizedscancode, (780, 780))

imsample.save('sample.png')


# os.walk('C:\\example_directory') or can be os.walk('C:\\')
# (
#     'C:\\example_directory',        # foldername
#     ['subdir1', 'subdir2'],         # subfolders // list
#     ['file4.txt']                   # filenames   // list
# )
# TXT files only contain plain text.

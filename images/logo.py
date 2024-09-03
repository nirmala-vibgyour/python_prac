# Add a website URL to images.
from PIL import Image, ImageDraw
import os

# for filename in os.listdir('./imagesWithUrl'):
#     # print(filename)
#     if (filename.endswith('.jpg')):
#         filepath = os.path.join('./imagesWithUrl', filename)
#         imObj = Image.open(filepath)
#         strfilename = imObj.filename.strip('.jpg')
#         newFilename = strfilename + '.png'
#         imObj.save(newFilename, 'PNG')
img = Image.open('url.png')
width, height = img.size
imgresized = img.resize((350, 100), resample=Image.Resampling.LANCZOS)
imgresized.save('urlresized.png')

text = "https://nirmala-vibgyour-webapp-web-nakdz2.streamlit.app/"
fontsize = 30
text_position = (10, 10)
text_color = (255, 165, 0)

for filename in os.listdir('./imagesWithUrl'):
    filepath = os.path.join('./imagesWithUrl', filename)
    image = Image.open(filepath)
    draw = ImageDraw.Draw(image)
    draw.text(text_position, text, fill=text_color)
    newfilename = filename.strip('.png') + 'new' + '.png'
    newfilepath = os.path.join('./imagesWithUrl' + newfilename)
    image.save(newfilepath)
    
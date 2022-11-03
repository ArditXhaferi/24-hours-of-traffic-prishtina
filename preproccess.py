from posixpath import split
from PIL import Image, ImageFont, ImageDraw 
import glob
      
for filename in glob.glob('./images/*.png'):
    image = Image.open(filename) 
    
    draw = ImageDraw.Draw(image) 
    
    # specified font size
    font = ImageFont.truetype("inter.ttf", 100)

    
    # drawing text size
    draw.text((5, 5), filename, font = font, align ="left", fill=(0,0,0)) 
    
    image.save(f'./preprocces/{filename.split("/")[2]}', 'PNG')

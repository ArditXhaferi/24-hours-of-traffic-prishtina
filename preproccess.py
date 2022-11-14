from posixpath import split
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import glob

# for filename in glob.glob('./images/13-11-2022 18:20.png'):
for filename in glob.glob('./images/*.png'):
    image = Image.open(filename) 
    
    
    # specified font size
    font = ImageFont.truetype("sf.otf", 100)

    # Create rectangle mask
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle([ (0,0), (600, 200) ], fill=255)
    mask.save('mask.png')

    # Blur image
    blurred = image.filter(ImageFilter.GaussianBlur(52))

    # Paste blurred region and save result
    image.paste(blurred, mask=mask)

    draw = ImageDraw.Draw(image) 

    # drawing text size
    draw.text((25, 35), "Koha: " + filename.split(" ")[1].replace(".png", ""), font = font, align ="left", fill="#fff") 
    shape = [(0,0), (600, 200)]
    draw.line((0, 0, 600, 0), fill="#fff", width=10)
    draw.line((0, 0, 0, 200), fill="#fff", width=10)
    draw.line((0, 200, 600, 200), fill="#fff", width=10)
    draw.line((600, 205, 600, 0), fill="#fff", width=10)
    print(f'Proccessed: { filename.split("/")[2] }')
    image.save(f'./preprocces/{filename.split("/")[2]}', 'PNG')

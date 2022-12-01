from posixpath import split
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import glob

def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (0, 0))
    result.paste(pil_img, (left, top))
    return result

# for filename in glob.glob('./images/14-11-2022 18:20.png'):
for filename in glob.glob('./images/*.png'):
    image = Image.open(filename) 
    
    image = add_margin(image, 200, 0, 0, 0, (33, 33, 33))

    # specified font size
    font = ImageFont.truetype("sf.otf", 100)
    fontSmall = ImageFont.truetype("sf.otf", 43)

    # Create rectangle mask
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle([ (0, 0), (1800, 200) ], fill=255)
    mask.save('mask.png')

    # Blur image
    blurred = image.filter(ImageFilter.GaussianBlur(52))

    # Paste blurred region and save result
    image.paste(blurred, mask=mask)

    draw = ImageDraw.Draw(image) 

    # drawing text size
    draw.text((50, 60), "Hour: " + filename.split(" ")[1].replace(".png", ""), font = font, align ="center", fill="#fff") 
    draw.text((700, 10), "Technologies: HTML, CSS, JS, Python, Selenium, PIL", font = fontSmall, align ="left", fill="#fff")
    draw.text((700, 70), "Data Source: Google Maps API V3 Traffic Layer", font = fontSmall, align ="left", fill="#fff")
    draw.text((700, 130), "Credits: Ardit Xhaferi | @ardit.dev", font = fontSmall, align ="left", fill="#fff") 
    draw.text((50, 20), "Date: 14-11-2022", font = fontSmall, align ="left", fill="#fff") 
    draw.line((650, 0, 650, 200), fill="#fff", width=10)

    draw.line((0, 200, 1800, 200), fill="#fff", width=10)

    layer = Image.open("./preprocces/test/layer.png") 
    image.paste(layer, (30, 250))


    print(f'Proccessed: { filename.split("/")[2] }')
    image.save(f'./preprocces/{filename.split("/")[2]}', 'PNG')



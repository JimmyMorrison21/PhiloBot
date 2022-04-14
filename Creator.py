import textwrap

from PIL import Image, ImageFont, ImageDraw

font_template = 'Font/Lobster-Regular.ttf'


def create_joke(template, joke_text):
    im = Image.open(template)

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font_template, size=30)
    # Place text on middle of image
    cor1, cor2 = im.size[0] / 2, im.size[1] / 2

    for line in textwrap.wrap(joke_text, width=40):
        draw.text((10, cor2), line, font=font, fill="#000000")
        cor2 += font.getsize(line)[1]

    im.save('joke_image.png')

#create_joke(template='test.jpg',joke_text='Hello world')

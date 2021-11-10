#!/usr/bin/env python
# _*_ encoding: utf-8 _*_

import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

CHARS = string.digits + string.ascii_letters

def create_captcha(loc='media/fonts', size=(350, 120), chars=CHARS, amount=6, img_type='GIF', mode='RGB', 
                   bg_color=(255, 255, 255), fg_color=(0, 0, 0), font_size=50, font_type='Arial', 
                   dlines=True, dpoints=True):
    """
    @params
    size: the size for captcha image
    chars: chars used for captcha character
    amount: character amout for captcha
    img_type: generated captcha image type
    mode: mode for color
    bg_color: background color for captcha image
    fg_color: foreground color for captcha image
    font_size: font size for captcha character
    font_type: font type for captcha character
    draw_lines: draw noise info
    draw_points: draw noise info
    """
    chars = get_chars(chars, amount)
    img = Image.new(mode, size, bg_color)
    draw = ImageDraw.Draw(img)
    if dlines:
        draw_lines(draw, size)
    if dpoints:
        draw_points(draw, size)
    draw_text(draw, loc, chars, size, font_type, font_size, fg_color)

    return chars, img, img_type

def get_chars(chars, amount):
    chars_list = random.sample(chars, amount)
    return ''.join(chars_list)

def draw_lines(draw, size):
    for i in range(random.randint(3, 10)):
        start = random.randint(0, size[0]), random.randint(0, size[1])
        end = random.randint(0, size[0]), random.randint(0, size[1])
        draw.line([start, end], fill=(80, 80, 80))

def draw_points(draw, size):
    for x in range(size[0]):
        for y in range(size[1]):
            if x + y >= random.randint(0, size[0] + size[1]):
                draw.point([x, y], fill=(180, 180, 180))

def draw_text(draw, loc, chars, size, font_type, font_size, fg_color):
    if font_type:
        try:
            font = ImageFont.truetype('%s/%s.otf' % (loc, font_type), font_size)
            font_width, font_height = font.getsize(chars)
        except IOError:
            font = None
            font_width, font_height = draw.textsize(chars)
    else:
        font = None
        font_width, font_height = draw.textsize(chars)
    draw.text([(size[0] - font_width) / 2, (size[1]-font_height) / 2], chars, font=font, fill=fg_color)


if __name__ == '__main__':
    chars, img, img_type = create_captcha(loc='../media/fonts')
    img.save("captcha.gif", "GIF")
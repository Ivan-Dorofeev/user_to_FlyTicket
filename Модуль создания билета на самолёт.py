# -*- coding: utf-8 -*-

import os

from PIL import Image, ImageDraw, ImageFont, ImageColor
import argparse


def make_ticket(fio, from_, to, date):
    path_file = os.path.join("snippets", "ticket_template.png")
    im = Image.open(path_file)
    # im.show()
    font_path = os.path.join("snippets", "ofont_ru_MurreyC.ttf")
    font_text = ImageFont.truetype(font_path, size=29)
    font_data = ImageFont.truetype(font_path, size=20)
    draw = ImageDraw.Draw(im)
    x = 40
    draw.text((x, 120), fio, font=font_text, fill=ImageColor.colormap['blue'])
    draw.text((x, 190), from_, font=font_text, fill=ImageColor.colormap['blue'])
    draw.text((x, 255), to, font=font_text, fill=ImageColor.colormap['blue'])
    draw.text((x + 250, 260), date, font=font_data, fill=ImageColor.colormap['blue'])
    path_end = 'fly_ticket_1.png'
    im.save(path_end)
    print(f'Билет сохранён {path_end}')


if __name__ == '__main__':
    make_ticket(fio='Дорофеев Иван Владимирович', from_='Москва', to='Рио-Де-Жанейро', date='29.05.2020')

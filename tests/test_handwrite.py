"""
Test handwrite by naked eye.
"""
from PIL import Image, ImageFont
from pylf import handwrite
from multiprocessing import freeze_support
import os


def main():
    im = Image.open("./data/pictures/design.jpg")
    template = {
        'background': im,
        'box': (100, 400, im.width-100, im.height-100),
        'color': (0, 0, 0),
        'font': ImageFont.truetype("./data/fonts/Gsllchb_lf.ttf"),
        'font_size': 40,
        'font_size_sigma': 2,
        'line_spacing': 40,
        'line_spacing_sigma': 1,
        'word_spacing': 0,
        'word_spacing_sigma': 2,
        'is_half_char': lambda c: c.isdigit() or c in ('!', '.', '?', ',', '，', '。'),
        'is_end_char': lambda c: c in ('!', '.', '?', ',', '，', '。')
    }
    dir_path, dir_names, file_names = list(os.walk("./data/texts"))[0]
    for filename in file_names:
        with open("{}/{}".format(dir_path, filename)) as f:
            text = f.read()
        images = handwrite(text, template)
        for image in images:
            image.show()
        input("""{} has been written.
        press ENTER to continues""".format(filename))

    template['box'] = (-100, -100, im.width+100, im.height+100)
    with open("./data/texts/荷塘月色.txt") as f:
        text = f.read()
    images = handwrite(text, template)
    for image in images:
        image.show()


if __name__ == '__main__':
    freeze_support()
    main()

# -*- coding: utf-8 -*-
"""
Created on Oct 03, 2024

@author: Emmett Hart
"""

import sys
import os
from byuimage import Image


def display_image(file: str):
    Image(file).show()


def darken(filename: str, outfile: str, percent: str):
    image = Image(filename)
    percent = float(percent)
    if percent < 0 or percent > 1:
        raise ValueError("Percentage must be between 0 and 1")
    for pixel in image:
        pixel.red *= 1 - percent
        pixel.green *= 1 - percent
        pixel.blue *= 1 - percent
    image.save(outfile)


def sepia(filename: str, outfile: str):
    image = Image(filename)
    for pixel in image:
        r = pixel.red
        g = pixel.green
        b = pixel.blue
        pixel.red = min(255, 0.393 * r + 0.769 * g + 0.189 * b)
        pixel.green = min(255, 0.349 * r + 0.686 * g + 0.168 * b)
        pixel.blue = min(255, 0.272 * r + 0.534 * g + 0.131 * b)
    image.save(outfile)


def grayscale(filename: str, outfile: str):
    image = Image(filename)
    for pixel in image:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        pixel.red = avg
        pixel.green = avg
        pixel.blue = avg
    image.save(outfile)


def make_borders(filename: str, outfile: str, thickness: str,
                 red: str, green: str, blue: str):
    image = Image(filename)
    thickness = int(thickness)
    red = int(red)
    green = int(green)
    blue = int(blue)
    output = Image.blank(image.height + 2 * thickness,
                         image.width + 2 * thickness)


def validate_commands(arguments: list[str]):
    try:
        option, *args = arguments
    except ValueError:
        raise ValueError(
            "Expected at least one flag and one positional argument")
    if option not in VALID_OPTIONS:
        raise ValueError(
            "Not a valid flag, valid flags are: {0}"
            .format(", ".join(VALID_OPTIONS.keys())))
    elif len(args) != VALID_OPTIONS[option]["nargs"]:
        raise ValueError("Expected {0} positional argument(s), {1} were given"
                         .format(VALID_OPTIONS[option]["nargs"], len(args)))
    elif not os.path.isfile(args[0]):
        raise ValueError(
            "First positional argument should be a valid filepath")
    elif len(args) >= 2 and not args[1][-3:] == "png":
        raise ValueError("Output file must be a png")
    return True


def main(arguments: list[str]):
    option, *args = arguments
    VALID_OPTIONS[option]["command"](*args)


VALID_OPTIONS = {
    "-d": {"nargs": 1,
           "command": display_image},
    "-k": {"nargs": 3,
           "command": darken},
    "-s": {"nargs": 2,
           "command": sepia},
    "-g": {"nargs": 2,
           "command": grayscale},
    "-b": {"nargs": 6,
           "command": make_borders}
}


if __name__ == "__main__":
    if validate_commands(sys.argv[1:]):
        main(sys.argv[1:])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""make_gif.py makes animated GIF from existing pictures."""

import glob
import os
import sys

from PIL import Image
from PIL import ImageGrab
from PIL import ImageTk

_script_home = os.path.abspath(os.path.dirname(__file__))


def make_gif(dirpath, picture_gif_duration, crop_left=None, crop_top=None, crop_right=None, crop_bottom=None):
    frames = []
    picture_list = glob.glob(os.path.join(dirpath, "*.png"))

    if len(picture_list) != 0:
        for picture in picture_list:
            new_frame = Image.open(picture)

            if (crop_left is not None) or (crop_top is not None) or (crop_right is not None) or (crop_bottom is not None):
                # Size of the image in pixels 
                (width, height) = new_frame.size
 
                # Set the points for the cropped image
                left = 0 if crop_left is None else crop_left*width
                top = 0 if crop_top is None else crop_top*height
                right = width if crop_right is None else crop_right*width
                bottom = height if crop_bottom is None else crop_bottom*height
 
                # Crop image
                new_frame = new_frame.crop((left, top, right, bottom))

            frames.append(new_frame)

        # Save into a GIF file that loops forever
        frames[0].save(os.path.join(dirpath, "all.gif"),
                        format='GIF',
                        append_images=frames[1:],
                        save_all=True,
                        duration=picture_gif_duration, loop=0)

        print()
        print("animated pictures as GIF is available in directory '%s'" % dirpath)

if __name__ == "__main__":

    print()
    print("Hello")
    print()
    print(f"Python sys.version = {sys.version}")

    picture_gif_duration = 500

    make_gif(os.path.join(_script_home, "game-tabletopia"), picture_gif_duration)
    make_gif(os.path.join(_script_home, "game-certu"), picture_gif_duration)
    make_gif(os.path.join(_script_home, "captures"), picture_gif_duration, crop_left=0.25, crop_top=0.40, crop_right=0.735, crop_bottom=0.87)
    make_gif(os.path.join(_script_home, "cube-moves"), picture_gif_duration, crop_left=0.25, crop_top=0.40, crop_right=0.66, crop_bottom=0.87)
    make_gif(os.path.join(_script_home, "stack-moves"), picture_gif_duration, crop_left=0.33, crop_top=0.40, crop_right=0.78, crop_bottom=0.87)
    make_gif(os.path.join(_script_home, "second-move"), picture_gif_duration, crop_left=0.30, crop_top=0.45, crop_right=0.69, crop_bottom=0.82)

    print()
    print("Bye")

    if True:
        print()
        _ = input("main: done ; press enter to terminate")

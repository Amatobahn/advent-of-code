# -*- coding: utf-8 -*-
"""

--- Day 10: The Stars Align ---

--- Part One ---

It's no use; your navigation system simply isn't capable of providing walking directions in the arctic circle,
and certainly not in 1018.

The Elves suggest an alternative. In times like these, North Pole rescue operations will arrange points of light
in the sky to guide missing Elves back to base. Unfortunately, the message is easy to miss: the points move slowly
enough that it takes hours to align them, but have so much momentum that they only stay aligned for a second.
If you blink at the wrong time, it might be hours before another message appears.

You can see these points of light floating in the distance, and record their position in the sky and their velocity,
the relative change in position per second (your puzzle input). The coordinates are all given from your perspective;
given enough time, those positions and velocities will move the points into a cohesive message!

Rather than wait, you decide to fast-forward the process and calculate what the points will eventually spell.

For example, suppose you note the following points:

position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>

Each line represents one point. Positions are given as <X, Y> pairs: X represents how far left (negative) or
right (positive) the point appears, while Y represents how far up (negative) or down (positive) the point appears.

At 0 seconds, each point has the position given. Each second, each point's velocity is added to its position.
So, a point with velocity <1, -2> is moving to the right, but is moving upward twice as quickly. If this point's
initial position were <3, 9>, after 3 seconds, its position would become <6, 3>.

Over time, the points listed above would move like this:

Initially:
........#.............
................#.....
.........#.#..#.......
......................
#..........#.#.......#
...............#......
....#.................
..#.#....#............
.......#..............
......#...............
...#...#.#...#........
....#..#..#.........#.
.......#..............
...........#..#.......
#...........#.........
...#.......#..........

After 1 second:
......................
......................
..........#....#......
........#.....#.......
..#.........#......#..
......................
......#...............
....##.........#......
......#.#.............
.....##.##..#.........
........#.#...........
........#...#.....#...
..#...........#.......
....#.....#.#.........
......................
......................

After 2 seconds:
......................
......................
......................
..............#.......
....#..#...####..#....
......................
........#....#........
......#.#.............
.......#...#..........
.......#..#..#.#......
....#....#.#..........
.....#...#...##.#.....
........#.............
......................
......................
......................

After 3 seconds:
......................
......................
......................
......................
......#...#..###......
......#...#...#.......
......#...#...#.......
......#####...#.......
......#...#...#.......
......#...#...#.......
......#...#...#.......
......#...#..###......
......................
......................
......................
......................

After 4 seconds:
......................
......................
......................
............#.........
........##...#.#......
......#.....#..#......
.....#..##.##.#.......
.......##.#....#......
...........#....#.....
..............#.......
....#......#...#......
.....#.....##.........
...............#......
...............#......
......................
......................

After 3 seconds, the message appeared briefly: HI. Of course, your message will be much longer and will
take many more seconds to appear.

What message will eventually appear in the sky?

"""

import os
import re
from itertools import count

try:
    import numpy as np
    import pytesseract
    import cv2

    os.environ['TESSDATA_PREFIX'] = r'C:\Program Files (x86)\Tesseract OCR'
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract OCR\tesseract"

except ImportError as e:
    print("You do not have all python libraries required installed:\n",
          "pip install numpy\npip install opencv-python\npip install pytesseract\n\n",
          "Pytesseract Executable must be installed: https://github.com/tesseract-ocr/tesseract/wiki/Downloads")


def get_rescue_op_message(light_data: tuple, time_steps: int, use_ocr: bool=False) -> tuple:
    """
    Cycles through each iteration of light movement until all units converge to make a string of text.

    Arguments:
    light_data (tuple [int]): Light position data and velocity
    time_steps (int): number of points in time to cycle the system
    use_ocr (bool): uses OCR (or attempts to) to capture the letters when identified
    """
    # Split values into easily accessible variables
    x, y, vx, vy = light_data[0], light_data[1], light_data[2], light_data[3]

    # Iterates through each time step (as a whole system)
    for time in count(time_steps):
        # Builds all the points generated from input data
        for i in range(len(x)):
            x[i] += vx[i]
            y[i] += vy[i]

        # Get the dimensions of the data
        min_x, min_y = min(x), min(y)
        width = max(x) - min_x + 1
        height = max(y) - min_y + 1

        # ONLY if OCR is enabled. Set to 100 for no real reason. Found that convergence happens around 10-15 max height
        if use_ocr:
            if height < 100:
                # Create empty image with padding to help with OCR
                image = np.zeros([height + 6, width + 6, 3], dtype=np.uint8)
                # Loop through X values since they will always be further in distance and set pixel value to white
                # while maintaining a partial offset (half of what we put in the base image)
                for j in range(len(x)):
                    image[(y[j] - min_y) + 3, (x[j] - min_x) + 3] = 255

                # Image processing
                # Resize to help OCR
                image = cv2.resize(image, dsize=(width * 25, height * 25), interpolation=cv2.INTER_CUBIC)
                # Convert to Grayscale. OpenCV is BGR
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                # Apply a binary threshold to solidify characters on screen
                image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]
                # Run OCR against image, configured for single line - removing spaces.
                text = pytesseract.image_to_string(image, config='--psm 7').replace(" ", "")
                # Validate if text is alphanumeric, if not we trash it - Handles for special characters
                if text.isalnum():
                    return text, time
            continue

        # ELSE we go the non-cool method and wait until height is less than 10
        elif height > 10:
            continue
        else:
            # Build initial ASCII image
            texture = [['.'] * width for _ in range(height)]

            # Loop through X values since they will always be further in distance and set pixel value to '#'
            for j in range(len(x)):
                texture[y[j] - min_y][x[j] - min_x] = '#'
            # Join all values in each line and print the line
            for val in texture:
                print(''.join(val))
            # Return Time only, since we don't have text to pass from ascii image.
            return None, time


if __name__ == "__main__":

    # Lazily build initial variables
    x, y, vx, vy = list(), list(), list(), list()
    # For each line we map to variables
    for line in open("puzzle_inputs/input_day_10.txt", 'r').readlines():
        for coord, velocity in zip([x, y, vx, vy], map(int, re.findall(r'-?\d+', line))):
            continue

    # Run function to save an elf with a not so descriptive message.
    print(get_rescue_op_message((x, y, vx, vy), 1, True))



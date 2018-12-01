# -*- coding: utf-8 -*-
"""
--- DAY 1: Chronal Calibration ---

--- Part One ---
After feeling like you've been falling for a few minutes, you look at the device's tiny screen.
"Error: Device must be calibrated before first use. Frequency drift detected. Cannot maintain destination lock."
Below the message, the device shows a sequence of changes in frequency (your puzzle input).
A value like +6 means the current frequency increases by 6;a value like -3 means the current frequency decreases by 3.

For example, if the device displays frequency changes of +1, -2, +3, +1,
then starting from a frequency of zero, the following changes would occur:

Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.

In this example, the resulting frequency is 3.

Here are other example situations:

+1, +1, +1 results in  3
+1, +1, -2 results in  0
-1, -2, -3 results in -6

Starting with a frequency of zero, what is the resulting frequency after all of the
changes in frequency have been applied?

--- Part Two ---

You notice that the device repeats the same frequency change list over and over.
To calibrate the device, you need to find the first frequency it reaches twice.

For example, using the same list of changes above, the device would loop as follows:

Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
(At this point, the device continues from the start of the list.)
Current frequency  3, change of +1; resulting frequency  4.
Current frequency  4, change of -2; resulting frequency  2, which has already been seen.

In this example, the first frequency reached twice is 2. Note that your device might need
to repeat its list of frequency changes many times before a duplicate frequency is found,
and that duplicates might be found while in the middle of processing the list.

Here are other examples:

+1, -1 first reaches 0 twice.
+3, +3, +4, -2, -4 first reaches 10 twice.
-6, +3, +8, +5, -6 first reaches 5 twice.
+7, +7, -2, -7, -4 first reaches 14 twice.

What is the first frequency your device reaches twice?

"""

import itertools


def calibrate(frequencies: list, puzzle_phase: int):
    """
    Phase One: Adds up all items in devices frequency output
    Phase Two: Locates the first repeated frequency. Can cycle more than once through data.

    Arguments:
        frequencies (list): Frequency output change from device
        puzzle_phase (int): Puzzle part to solve for
    """

    if puzzle_phase is 1:
        return f"Part One: {sum(frequencies)}"
    else:
        resulting_frequency = 0
        computed_frequencies = set([])

        for f in itertools.cycle(frequencies):
            resulting_frequency += f
            if resulting_frequency in computed_frequencies:
                return f"Part Two: {resulting_frequency}"
            computed_frequencies.add(resulting_frequency)


if __name__ == "__main__":

    inputs = [int(val) for val in open("puzzle_inputs/input_day_1.txt", "r").readlines()]
    print(calibrate(inputs, 1), calibrate(inputs, 2))





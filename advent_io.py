# -*- coding: utf-8 -*-

"""
--- Utility ---
Supplemental file for Advent of code to handle
simple file IO for puzzle inputs
"""


def get_puzzle_input(day: int):
    day = day if day > 0 else 1
    return open(f"puzzle_inputs/input_day_{day}.txt", 'r')

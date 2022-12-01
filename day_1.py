# Day 1

from itertools import groupby
from typing import List

if __name__ == "__main__":
    data: List = [list(map(int, g)) for k, g in groupby(open("_input/01.txt").read().splitlines(), lambda x: x=="") if not k]
    caloric_totals: List = sorted([sum(derp) for derp in data], reverse=True)
    print(f"A): {caloric_totals[0]} B): {sum(caloric_totals[:3])}")

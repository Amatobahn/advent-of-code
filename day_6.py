# Day 6
from collections import Counter


def get_marker_position(stream: str, buffer_size: int) -> int:
    for i in range(len(stream) - buffer_size):
        if all([x == 1 for x in Counter(stream[i:i+buffer_size]).values()]):
            return i + buffer_size


if __name__ == "__main__":
    data = open("_input/06.txt").read()
    print(f"A) {get_marker_position(data, 4)} B) {get_marker_position(data, 14)}")

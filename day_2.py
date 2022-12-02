# Day 2


if __name__ == "__main__":
    data = [[ord(a) - ord('A'), ord(b) - ord('X')] for (a, b) in (line.split() for line in open("_input/02.txt"))]

    scores = [0, 0]
    for a, b in data:
        scores[0] += (((b + 1 - a) % 3) * 3) + b + 1
        scores[1] += ((a + b + 2) % 3) + (b * 3 + 1)
    print(f"A): {scores[0]} B): {scores[1]}")

# Day 4


def iterate_line(path: str):
    for line in open(path).read().splitlines():
        yield list(map(int, line.replace(',', '-').split('-')))


if __name__ == "__main__":
    full_coverage: int = 0
    partial_coverage: int = 0

    for a1, a2, b1, b2 in iterate_line("_input/04.txt"):
        s1, s2 = set(range(a1, a2+1)), set(range(b1, b2+1))

        if s1.issubset(s2) or s2.issubset(s1):
            full_coverage += 1
        if len(s1 & s2) > 0:
            partial_coverage += 1

    print(f"A): {full_coverage} B): {partial_coverage}")

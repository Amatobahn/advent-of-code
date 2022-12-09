# Day 9

DIRS = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1)
}


def do_the_thing(knot_count: int, op_set):
    head = [[0, 0] for _ in range(knot_count)]  # Precache Knots
    positions = set()  # Use sets as they can't contain duplicates
    positions.add((0, 0))  # Add origin as starting point

    for op in op_set:
        direction, distance = op

        for _ in range(int(distance)):
            # Add the direction to the coordinates
            head[0][0] += DIRS[direction][0]
            head[0][1] += DIRS[direction][1]

            for i in range(1, len(head)):
                # Get the 'tail'
                x, y = head[i-1][0] - head[i][0], head[i-1][1] - head[i][1]
                # Check if the distance between points (including diag) > 1
                # Add +/- 1 if so to each, otherswise skip!
                if max(abs(x), abs(y)) > 1:
                    head[i][0] += 1 if x > 0 else 0 if x == 0 else -1
                    head[i][1] += 1 if y > 0 else 0 if y == 0 else -1
            positions.add(tuple(head[-1]))

    return len(positions)


if __name__ == "__main__":
    data = [op.split() for op in open("_input/09.txt").read().splitlines()]

    print(f"A) {do_the_thing(2, data)} B) {do_the_thing(10, data)}")

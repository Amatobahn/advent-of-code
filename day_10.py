# Day 10


if __name__ == "__main__":
    data = open("_input/10.txt").read().splitlines()

    screen = [[" " for x in range(40)] for y in range(6)]
    register: int = 1
    cycle_cnt: int = 0
    strength: dict = {}

    for op in data:
        cycle_cnt += 1
        strength[cycle_cnt] = (register, register * cycle_cnt)
        if op.startswith("addx"):
            cycle_cnt += 1
            strength[cycle_cnt] = (register, register * cycle_cnt)
            register += int(op.split()[1])

    for cycle in strength:
        x = strength[cycle][0]
        if (cycle-1) % 40 in [x - 1, x, x + 1]:
            screen[(cycle - 1) // 40][(cycle - 1) % 40] = "|"

    # A
    print(sum([v[1] for k, v in strength.items() if int(k) in [20, 60, 100, 140, 180, 220]]))
    # B
    for line in screen:
        print("".join(line))



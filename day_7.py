# Day 7

DISK_SPACE = 70000000
UNUSED_SPACE = 30000000
MAX_DIR_SIZE = 100000


if __name__ == "__main__":
    data = open("_input/07.txt").read().splitlines()

    tree: dict = {"_": 0}
    current_dir = ["_"]

    for cmd in data:
        cmd = cmd.split()
        if cmd[1] == "ls":
            continue

        if cmd[1] == "cd":
            if cmd[2] in ["/", ".."]:
                current_dir = ["_"] if cmd[2] == "/" else current_dir[:-1]
            else:
                current_dir.append(cmd[2])
        else:
            if cmd[0] == "dir":
                tree[f"{'/'.join(current_dir)}/{cmd[1]}"] = 0  # folder
            else:
                for i in range(len(current_dir)):
                    tree["/".join(current_dir[:i + 1])] += int(cmd[0])

    result_a = sum([b for b in tree.values() if b <= MAX_DIR_SIZE])
    result_b = min(size for size in tree.values() if size >= UNUSED_SPACE - (DISK_SPACE - tree["_"]))
    print(f"A) {result_a} B) {result_b}")

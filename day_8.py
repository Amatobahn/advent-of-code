# Day 8


def view_dist(curr_tree, view):
    for idx, _tree in enumerate(view):
        if _tree >= curr_tree:
            return idx + 1
    return len(view)


if __name__ == "__main__":
    forest = [[int(val) for val in row] for row in open("_input/08.txt").read().splitlines()]
    forest_b = list(zip(*forest))

    total_a = total_b = 0

    for i in range(len(forest[0])):
        for j in range(len(forest)):
            tree = forest[i][j]
            if all(x < tree for x in forest[i][0:j]) or all(x < tree for x in forest[i][j+1:]) or \
               all(x < tree for x in forest_b[j][0:i]) or all(x < tree for x in forest_b[j][i+1:]):
                total_a += 1

            ss_ab = view_dist(tree, forest[i][0:j][::-1]) * view_dist(tree, forest[i][j+1:])
            ss_cd = view_dist(tree, forest_b[j][0:i][::-1]) * view_dist(tree, forest_b[j][i+1:])
            score = ss_ab * ss_cd
            if score > total_b:
                total_b = score

    print(f"A) {total_a} B) {total_b}")

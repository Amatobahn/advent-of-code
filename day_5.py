# Day 5 - The Maxscript Crates (Crate base start at 1)
from itertools import groupby

if __name__ == "__main__":
    data = open("_input/05.txt").read().splitlines()
    crate_data = [line[1::2] for line in data[:8]]
    proc_data = [line.split()[1::2] for line in data[10:]]

    crate_data = []
    col_data = []
    col_data_9k1 = []
    for line in data[:8]:
        value = line[1::2]
        crate_data.append([v for v in value[::2]])

    # Convert to column
    for i in range(len(crate_data[0])):
        col_data.append([])
        col_data_9k1.append([])
        for row in crate_data[::-1]:
            if row[i] != " ":
                col_data[i].append(row[i])
                col_data_9k1[i].append(row[i])

    # Run procedure
    for proc in proc_data:
        iteration = int(proc[0])
        take = int(proc[1]) - 1
        put = int(proc[2]) - 1
        for i in range(iteration):  # step 1: Iterations
            crate = col_data[take].pop(-1)  # Take
            col_data[put].append(crate)  # Set

        crates = [col_data_9k1[take].pop(-1) for i in range(iteration)]
        col_data_9k1[put].extend(crates[::-1])

    print([col_data_9k1[i][-1] for i in range(len(col_data))])
    print(col_data)


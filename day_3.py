# Day 3


def get_priority(char) -> int:
    return (ord(char) - ord("a")) + 1 if not char.isupper() else (ord(char) - ord("A")) + 27


if __name__ == "__main__":
    data = open("_input/03.txt").read().splitlines()
    data_groups = [data[i:i+3] for i in range(0, len(data), 3)]
    priority_sums = {
        "A)": sum([get_priority(list(set(sack[:len(sack)//2]) & set(sack[len(sack)//2:]))[0]) for sack in data]),
        "B)": sum([get_priority(list(set(group[0]) & set(group[1]) & set(group[2]))[0]) for group in data_groups])
    }

    print(priority_sums)

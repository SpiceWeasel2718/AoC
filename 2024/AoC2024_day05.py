def part1(input_text: str):
    from collections import defaultdict

    rules_text, updates_text = input_text.split("\n\n")

    rules = defaultdict(list)

    for line in rules_text.splitlines():
        i1, i2 = line.split("|")
        rules[i1].append(i2)

    s = 0

    for line in updates_text.splitlines():
        update = line.split(",")
        update_dict = {page: i for i, page in enumerate(update)}
        for page in update:
            good_page = True

            if page in rules:
                for later_page in rules[page]:
                    if (
                        later_page in update_dict
                        and update_dict[later_page] < update_dict[page]
                    ):
                        good_page = False
                        break
            if not good_page:
                break
        else:
            s += int(update[len(update) // 2])

    return s


def part2(input_text: str):
    from collections import defaultdict
    from functools import cmp_to_key

    rules_text, updates_text = input_text.split("\n\n")

    rules = defaultdict(list)

    for line in rules_text.splitlines():
        i1, i2 = line.split("|")
        rules[i1].append(i2)

    bad_updates = []

    for line in updates_text.splitlines():
        update = line.split(",")
        update_dict = {page: i for i, page in enumerate(update)}
        for page in update:
            good_page = True

            if page in rules:
                for later_page in rules[page]:
                    if (
                        later_page in update_dict
                        and update_dict[later_page] < update_dict[page]
                    ):
                        good_page = False
                        break
            if not good_page:
                bad_updates.append(update)
                break

    def cmp(a, b):
        if a in rules and b in rules[a]:
            return -1
        elif b in rules and a in rules[b]:
            return 1
        else:
            return 0

    s = 0

    for update in bad_updates:
        update.sort(key=cmp_to_key(cmp))
        s += int(update[len(update) // 2])

    return s


if __name__ == "__main__":
    from pathlib import Path

    current_file = Path(__file__)
    input_file = (
        current_file.parent / "input_files" / (current_file.stem + "_input.txt")
    )

    with open(input_file) as fp:
        input_text = fp.read()

    print("Part 1:")
    print(p1 := part1(input_text))
    print("Part 2:")
    print(part2(input_text))

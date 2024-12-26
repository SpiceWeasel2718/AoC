def part1(input_text: str):
    track = {}

    for row, line in enumerate(input_text.splitlines()):
        for col, c in enumerate(line):
            if c != "#":
                pos = row + col * 1j
                track[pos] = 0
                if c == "S":
                    start_pos = pos
                if c == "E":
                    end_pos = pos

    path = []
    current_pos = start_pos
    t = 0

    while end_pos not in path:
        path.append(current_pos)
        track[current_pos] = t
        t += 1

        for d in [1, 1j, -1, -1j]:
            nbr = current_pos + d
            if nbr in track and nbr not in path[-2:]:
                current_pos = nbr
                break

    count = 0

    for pos in path[:-102]:
        for d in [2, 1 + 1j, 2j, -1 + 1j, -2, 1 - 1j, -2j, -1 - 1j]:
            cheat = pos + d
            if cheat in track and track[pos] + 102 <= track[cheat]:
                count += 1

    return count


def part2(input_text: str):
    track = {}

    for row, line in enumerate(input_text.splitlines()):
        for col, c in enumerate(line):
            if c != "#":
                pos = row + col * 1j
                track[pos] = 0
                if c == "S":
                    start_pos = pos
                if c == "E":
                    end_pos = pos

    path = []
    current_pos = start_pos
    t = 0

    while end_pos not in path:
        path.append(current_pos)
        track[current_pos] = t
        t += 1

        for d in [1, 1j, -1, -1j]:
            nbr = current_pos + d
            if nbr in track and nbr not in path[-2:]:
                current_pos = nbr
                break

    dist_sets = {}
    seen = {0j}
    next_set = {1, 1j, -1, -1j}

    for dist in range(2, 21):
        current_set, next_set = next_set, set()
        for pos in current_set:
            seen.add(pos)
            for d in [1, 1j, -1, -1j]:
                check_pos = pos + d
                if check_pos not in seen:
                    next_set.add(check_pos)

        dist_sets[dist] = next_set

    count = 0

    for pos in path[:-102]:
        for dist in dist_sets:
            for d in dist_sets[dist]:
                cheat = pos + d
                if cheat in track and track[pos] + 100 + dist <= track[cheat]:
                    count += 1

    return count


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

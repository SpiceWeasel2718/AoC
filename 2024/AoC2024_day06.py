def part1(input_text: str):
    lines = input_text.splitlines()
    obstacles = set()

    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c == "#":
                obstacles.add(row + col * 1j)
            elif c == "^":
                guard_pos = row + col * 1j

    max_row = len(lines) - 1
    max_col = len(lines[0]) - 1

    def in_map(pos):
        return 0 <= pos.real <= max_row and 0 <= pos.imag <= max_col

    route = set()
    v = -1

    while in_map(guard_pos):
        route.add(guard_pos)
        while guard_pos + v in obstacles:
            v *= -1j
        guard_pos += v

    return len(route)


def part2(input_text: str):
    lines = input_text.splitlines()
    obstacles = set()

    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c == "#":
                obstacles.add(row + col * 1j)
            elif c == "^":
                guard_pos = row + col * 1j

    max_row = len(lines) - 1
    max_col = len(lines[0]) - 1

    def in_map(pos):
        return 0 <= pos.real <= max_row and 0 <= pos.imag <= max_col

    valid_placements = set()
    v = -1

    guard_start = guard_pos
    v_start = v

    while in_map(guard_pos):
        if guard_pos + v in obstacles:
            v *= -1j
        else:
            guard_pos += v

            if guard_pos not in valid_placements:
                test_obstacles = obstacles | {guard_pos}
                test_pos, test_v = guard_start, v_start
                path = set()
                while in_map(test_pos):
                    if (test_pos, test_v) in path:
                        valid_placements.add(guard_pos)
                        break
                    else:
                        path.add((test_pos, test_v))
                    if test_pos + test_v in test_obstacles:
                        test_v *= -1j
                    else:
                        test_pos += test_v

    return len(valid_placements)


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

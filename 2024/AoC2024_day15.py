def part1(input_text: str):
    warehouse_text, route_text = input_text.split("\n\n")

    warehouse = {}
    wall = set()

    for row, line in enumerate(warehouse_text.splitlines()):
        for col, c in enumerate(line):
            pos = row + col * 1j
            if c == ".":
                warehouse[pos] = 0
            elif c == "O":
                warehouse[pos] = 1
            elif c == "#":
                wall.add(pos)
                warehouse[pos] = 2
            elif c == "@":
                warehouse[pos] = 0
                robot_pos = pos

    moves = {"v": 1, ">": 1j, "^": -1, "<": -1j}

    for m in route_text:
        if m not in moves:
            continue
        else:
            v = moves[m]

        test_pos = robot_pos + v

        while warehouse[test_pos] == 1:
            test_pos += v

        if warehouse[test_pos] == 0:
            warehouse[test_pos] = 1
            warehouse[robot_pos + v] = 0
            robot_pos += v

    s = 0

    for pos in warehouse:
        if warehouse[pos] == 1:
            s += 100 * pos.real + pos.imag

    return int(s)


def part2(input_text: str):
    from collections import deque

    warehouse_text, route_text = input_text.split("\n\n")

    warehouse = {}

    for row, line in enumerate(warehouse_text.splitlines()):
        for col, c in enumerate(line):
            pos = row + col * 2j
            if c == ".":
                warehouse[pos] = "."
                warehouse[pos + 1j] = "."
            elif c == "O":
                warehouse[pos] = pos + 1j
                warehouse[pos + 1j] = pos
            elif c == "#":
                warehouse[pos] = "#"
                warehouse[pos + 1j] = "#"
            elif c == "@":
                warehouse[pos] = "."
                warehouse[pos + 1j] = "."
                robot_pos = pos

    moves = {"v": 1, ">": 1j, "^": -1, "<": -1j}

    for m in route_text:
        if m not in moves:
            continue
        else:
            v = moves[m]

        queue = deque()
        queue.append(robot_pos + v)
        checked_crates = set()
        shifted_crates = {}

        while queue:
            test_pos = queue.pop()
            if warehouse[test_pos] == "#":
                break
            elif warehouse[test_pos] != ".":
                if warehouse[test_pos] not in checked_crates:
                    queue.appendleft(warehouse[test_pos])
                queue.appendleft(test_pos + v)
                checked_crates.add(test_pos)
                shifted_crates[test_pos + v] = warehouse[test_pos] + v
        else:
            robot_pos += v
            for pos in checked_crates:
                warehouse.update(shifted_crates)
            for pos in checked_crates:
                if pos not in shifted_crates:
                    warehouse[pos] = "."

    s = 0

    for pos in warehouse:
        if isinstance(warehouse[pos], complex) and pos.imag < warehouse[pos].imag:
            s += 100 * pos.real + pos.imag

    return int(s)


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

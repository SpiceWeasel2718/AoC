def part1(input_text: str):
    from collections import defaultdict
    from itertools import combinations

    lines = input_text.splitlines()
    antennas = defaultdict(list)

    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c != ".":
                antennas[c].append(row + col * 1j)

    max_row = len(lines) - 1
    max_col = len(lines[0]) - 1

    def in_map(pos):
        return 0 <= pos.real <= max_row and 0 <= pos.imag <= max_col

    antinodes = set()

    for positions in antennas.values():
        for p1, p2 in combinations(positions, 2):
            v = p2 - p1
            if in_map(p2 + v):
                antinodes.add(p2 + v)
            if in_map(p1 - v):
                antinodes.add(p1 - v)

    return len(antinodes)


def part2(input_text: str):
    from collections import defaultdict
    from itertools import combinations

    lines = input_text.splitlines()
    antennas = defaultdict(list)

    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c != ".":
                antennas[c].append(row + col * 1j)

    max_row = len(lines) - 1
    max_col = len(lines[0]) - 1

    def in_map(pos):
        return 0 <= pos.real <= max_row and 0 <= pos.imag <= max_col

    antinodes = set()

    for positions in antennas.values():
        for p1, p2 in combinations(positions, 2):
            v = p2 - p1
            pos = p2
            while in_map(pos):
                antinodes.add(pos)
                pos += v
            pos = p1
            while in_map(pos):
                antinodes.add(pos)
                pos -= v

    return len(antinodes)


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

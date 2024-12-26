def part1(input_text: str):
    from collections import defaultdict

    word_search = defaultdict(str)
    word_starts = []
    count = 0

    for row, line in enumerate(input_text.splitlines()):
        for col, letter in enumerate(line):
            pos = row + col * 1j
            word_search[pos] = letter
            if letter == "X":
                word_starts.append(pos)

    directions = [1, 1 + 1j, 1j, -1 + 1j, -1, -1 - 1j, -1j, 1 - 1j]

    for start in word_starts:
        for v in directions:
            pos = start
            for letter in "MAS":
                pos += v
                if word_search[pos] != letter:
                    break
            else:
                count += 1

    return count


def part2(input_text: str):
    from collections import defaultdict

    word_search = defaultdict(str)
    a_pos = []
    count = 0

    for row, line in enumerate(input_text.splitlines()):
        for col, letter in enumerate(line):
            pos = row + col * 1j
            word_search[pos] = letter
            if letter == "A":
                a_pos.append(pos)

    for center in a_pos:
        strokes = [
            [word_search[center - 1 + 1j], word_search[center + 1 - 1j]],
            [word_search[center + 1 + 1j], word_search[center - 1 - 1j]],
        ]
        for stroke in strokes:
            if "M" not in stroke or "S" not in stroke:
                break
        else:
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

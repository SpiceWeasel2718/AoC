def part1(input_text: str):
    locks, keys = [], []

    for item in input_text.split("\n\n"):
        heights = [0] * 5
        if item.startswith("#"):
            for line in item.splitlines()[1:]:
                for i, c in enumerate(line):
                    if c == "#":
                        heights[i] += 1
            locks.append(heights)
        else:
            for line in reversed(item.splitlines()[:-1]):
                for i, c in enumerate(line):
                    if c == "#":
                        heights[i] += 1
            keys.append(heights)

    count = 0

    for lock in locks:
        for key in keys:
            count += all(lh + kh <= 5 for lh, kh in zip(lock, key))

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
    print(part1(input_text))

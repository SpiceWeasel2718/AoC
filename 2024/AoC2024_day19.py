def part1(input_text: str):
    from functools import cache

    patterns_text, designs_text = input_text.split("\n\n")

    patterns = set(patterns_text.split(", "))
    designs = designs_text.splitlines()

    max_pattern_len = max(len(p) for p in patterns)

    @cache
    def valid_design(design):
        if not design:
            return True

        check_len = min(max_pattern_len, len(design))

        for length in range(check_len, 0, -1):
            if design[:length] in patterns and valid_design(design[length:]):
                return True
        else:
            return False

    return sum(valid_design(d) for d in designs)


def part2(input_text: str):
    from functools import cache

    patterns_text, designs_text = input_text.split("\n\n")

    patterns = set(patterns_text.split(", "))
    designs = designs_text.splitlines()

    max_pattern_len = max(len(p) for p in patterns)

    @cache
    def count_arrangements(design):
        if not design:
            return 1

        check_len = min(max_pattern_len, len(design))
        count = 0

        for length in range(check_len, 0, -1):
            if design[:length] in patterns:
                count += count_arrangements(design[length:])

        return count

    return sum(count_arrangements(d) for d in designs)


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

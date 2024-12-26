def part1(input_text: str):
    stones = [int(n) for n in input_text.strip().split()]

    for __ in range(25):
        prev_stones = stones
        stones = []

        for stone in prev_stones:
            if stone == 0:
                stones.append(1)
            else:
                stone_str = str(stone)
                n_digits = len(stone_str)
                if n_digits % 2 == 0:
                    stones.append(int(stone_str[: n_digits // 2]))
                    stones.append(int(stone_str[n_digits // 2 :]))
                else:
                    stones.append(stone * 2024)

    return len(stones)


def part2(input_text: str):
    from functools import cache

    stones = [int(n) for n in input_text.strip().split()]

    rules_cache = {0: [1]}

    @cache
    def count_stones(stone, depth):
        if depth == 0:
            return 1
        if stone not in rules_cache:
            stone_str = str(stone)
            n_digits = len(stone_str)
            if n_digits % 2 == 0:
                rules_cache[stone] = [
                    int(stone_str[: n_digits // 2]),
                    int(stone_str[n_digits // 2 :]),
                ]
            else:
                rules_cache[stone] = [stone * 2024]

        return sum(count_stones(s, depth - 1) for s in rules_cache[stone])

    return sum(count_stones(s, 75) for s in stones)


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

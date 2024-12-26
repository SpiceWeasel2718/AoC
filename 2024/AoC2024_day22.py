def part1(input_text: str):
    PRUNE_VALUE = 16777216

    initial_numbers = []

    for line in input_text.splitlines():
        initial_numbers.append(int(line))

    def next_secret(n):
        n = ((n * 64) ^ n) % PRUNE_VALUE
        n = ((n >> 5) ^ n) % PRUNE_VALUE
        return ((n * 2048) ^ n) % PRUNE_VALUE

    s = 0

    for n in initial_numbers:
        for __ in range(2000):
            n = next_secret(n)

        s += n

    return s


def part2(input_text: str):
    from collections import Counter, deque

    PRUNE_VALUE = 16777216

    initial_numbers = []

    for line in input_text.splitlines():
        initial_numbers.append(int(line))

    def next_secret(n):
        n = ((n << 6) ^ n) % PRUNE_VALUE
        n = ((n >> 5) ^ n) % PRUNE_VALUE
        return ((n << 11) ^ n) % PRUNE_VALUE

    sales = Counter()

    for n in initial_numbers:
        last_changes = deque(maxlen=4)
        change_sequences = {}
        price = n % 10

        for __ in range(2000):
            n = next_secret(n)
            prev_price, price = price, n % 10
            last_changes.append(price - prev_price)
            if (
                len(last_changes) == 4
                and (k := tuple(last_changes)) not in change_sequences
            ):
                change_sequences[k] = price

        sales += change_sequences

    return max(sales.values())


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

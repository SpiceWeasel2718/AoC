def part1(input_text: str):
    def test_eq(target, val, operands):
        if val > target:
            return False
        elif not operands:
            return val == target
        else:
            operand = operands.pop()
            return test_eq(target, val * operand, operands.copy()) or test_eq(
                target, val + operand, operands.copy()
            )

    s = 0

    for line in input_text.splitlines():
        target_text, operands_text = line.split(": ")
        target, operands = (
            int(target_text),
            [int(n) for n in reversed(operands_text.split())],
        )

        val = operands.pop()

        if test_eq(target, val, operands):
            s += target

    return s


def part2(input_text: str):
    def test_eq(target, val, operands):
        if val > target:
            return False
        elif not operands:
            return val == target
        else:
            operand = operands.pop()
            return (
                test_eq(target, val * operand, operands.copy())
                or test_eq(target, val + operand, operands.copy())
                or test_eq(target, int(f"{val}{operand}"), operands.copy())
            )

    s = 0

    for line in input_text.splitlines():
        target_text, operands_text = line.split(": ")
        target, operands = (
            int(target_text),
            [int(n) for n in reversed(operands_text.split())],
        )

        val = operands.pop()

        if test_eq(target, val, operands):
            s += target

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

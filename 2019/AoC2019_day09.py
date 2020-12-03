def part1(input_text):
    from intcode import IntComp

    computer = IntComp(input_text[0])
    computer.append_inputs(1)
    return computer.execute()[-1]


def part2(input_text):
    from intcode import IntComp

    computer = IntComp(input_text[0])
    computer.append_inputs(2)
    return computer.execute()[-1]


if __name__ == '__main__':
    from pathlib import Path
    with open(next(Path().glob('**/AoC2019_day09_input.txt'))) as f:
        input_text = f.read().splitlines()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
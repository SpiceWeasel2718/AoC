def part1(input_text):
    entries = [int(n) for n in input_text.splitlines()]
    entries.sort()

    bottom_gen = iter(entries)
    bottom = next(bottom_gen)

    top_gen = iter(entries[::-1])
    top = next(top_gen)

    while bottom < top:
        val = bottom + top
        if val < 2020:
            bottom = next(bottom_gen)
        elif val > 2020:
            top = next(top_gen)
        else:
            return bottom * top


def part2(input_text):
    entries = [int(n) for n in input_text.splitlines()]
    entries.sort()

    for third in entries:
        target = 2020 - third
        
        bottom_gen = iter(entries)
        bottom = next(bottom_gen)

        top_gen = iter(entries[::-1])
        top = next(top_gen)

        while bottom < top:
            val = bottom + top
            if val < target:
                bottom = next(bottom_gen)
            elif val > target:
                top = next(top_gen)
            elif bottom != third:
                    return bottom * top * third


if __name__ == '__main__':
    from pathlib import Path
    with open(Path('./2020/input_files/AoC2020_day01_input.txt')) as f:
        input_text = f.read()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    print(f'part1 took at least {min(p1_timer.repeat(number=1000)) :.5f} seconds')
    print(f'part2 took at least {min(p2_timer.repeat(number=1000)) :.5f} seconds')
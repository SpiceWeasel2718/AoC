def part1(input_text):
    highest = 0

    for seat in input_text.splitlines():
        n = 0

        for c in seat[:7]:
            n <<= 1
            n += (c == 'B')

        for c in seat[7:]:
            n <<= 1
            n += (c == 'R')

        highest = max(n, highest)
    
    return highest


def part2(input_text, result):
    for seat in input_text.splitlines():
        n = 0

        for c in seat[:7]:
            n <<= 1
            n += (c == 'B')

        for c in seat[7:]:
            n <<= 1
            n += (c == 'R')

        result ^= n

    return result


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day05_input.txt') as f:
        input_text = f.read()

    
    print('part 1:', p1 := part1(input_text))
    print('part 2:', part2(input_text, p1))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text, p1)', globals=globals())
    # print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    # print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
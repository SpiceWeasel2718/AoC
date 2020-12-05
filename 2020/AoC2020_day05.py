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


def part2(input_text):
    unoccupied = set(range(1024))

    for seat in input_text.splitlines():
        n = 0

        for c in seat[:7]:
            n <<= 1
            n += (c == 'B')

        for c in seat[7:]:
            n <<= 1
            n += (c == 'R')

        unoccupied.remove(n)

    for seat_num in unoccupied:
        if not seat_num-1 in unoccupied and not seat_num+1 in unoccupied:
            return seat_num


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day05_input.txt') as f:
        input_text = f.read()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    # print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    # print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
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

    time_execution = 1

    if time_execution:
        import timeit
        for part in ['part1', 'part2']:
            timer = timeit.Timer(f'{part}(input_text)', globals=globals())
            n, time = timer.autorange()
            print(f'{part} took {time/n:.5f} seconds on average when run {n} times')
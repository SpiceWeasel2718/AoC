def part1(input_text):
    start = [int(n) for n in input_text.rstrip().split(',')]
    spoken = {}
    
    for turn, last in enumerate(start[:-1], 1):
        spoken[last] = turn

    last = start[-1]
    
    for turn in range(len(start), 2020):
        if last in spoken:
            n = turn - spoken[last]
            spoken[last] = turn
            last = n
        else:
            spoken[last] = turn
            last = 0

    return last


def part2(input_text):
    start = [int(n) for n in input_text.rstrip().split(',')]
    spoken = {}
    
    for turn, last in enumerate(start[:-1], 1):
        spoken[last] = turn

    last = start[-1]
    
    for turn in range(len(start), 30000000):
        if last in spoken:
            n = turn - spoken[last]
            spoken[last] = turn
            last = n
        else:
            spoken[last] = turn
            last = 0

    return last


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day15_input.txt') as f:
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
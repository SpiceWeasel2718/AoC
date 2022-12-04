def part1(input_text):
    count = 0
    
    for line in input_text.splitlines():
        e1, e2 = line.split(',')
        min1, max1 = [int(n) for n in e1.split('-')]
        min2, max2 = [int(n) for n in e2.split('-')]

        if (min1 <= min2 and max1 >= max2) or (min2 <= min1 and max2 >= max1):
            count += 1
    
    return count


def part2(input_text):
    count = 0
    
    for line in input_text.splitlines():
        e1, e2 = line.split(',')
        min1, max1 = [int(n) for n in e1.split('-')]
        min2, max2 = [int(n) for n in e2.split('-')]

        if not (max1 < min2 or max2 < min1):
            count += 1
    
    return count


if __name__ == '__main__':
    with open('./input_files/AoC2022_day04_input.txt') as f:
        input_text = f.read()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    time_execution = 0

    if time_execution:
        import timeit
        for part in ['part1', 'part2']:
            timer = timeit.Timer(f'{part}(input_text)', globals=globals())
            n, time = timer.autorange()
            print(f'{part} took {time/n:.5f} seconds on average when run {n} times')
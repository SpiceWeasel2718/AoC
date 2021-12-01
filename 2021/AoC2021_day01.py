def part1(input_text):
    depths = [int(n) for n in input_text.split()]
    
    return sum((a < b) for a, b in zip(depths, depths[1:]))


def part2(input_text):
    depths = [int(n) for n in input_text.split()]
    
    return sum((a < b) for a, b in zip(depths, depths[3:]))


if __name__ == '__main__':
    with open('./input_files/AoC2021_day01_input.txt') as f:
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
def part1(input_text):
    depth = 0
    horiz = 0

    for line in input_text.splitlines():
        d, n = line.split()

        if d == "down":
            depth += int(n)
        elif d == "up":
            depth -= int(n)
        else:
            horiz += int(n)
    
    return horiz * depth


def part2(input_text):
    depth = 0
    horiz = 0
    aim = 0

    for line in input_text.splitlines():
        d, n = line.split()

        if d == "down":
            aim += int(n)
        elif d == "up":
            aim -= int(n)
        else:
            horiz += int(n)
            depth += aim * int(n)
    
    return horiz * depth


if __name__ == '__main__':
    with open('./input_files/AoC2021_day02_input.txt') as f:
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
def part1(input_text: str):
    priorities = {}
    
    for i in range(65, 91):
        priorities[chr(i)] = i - 38
    for i in range(97, 123):
        priorities[chr(i)] = i - 96

    total = 0

    for line in input_text.splitlines():
        l = len(line) // 2
        s = set(line[:l]) & set(line[l:])
        total += priorities[s.pop()]

    return total


def part2(input_text: str):
    priorities = {}
    
    for i in range(65, 91):
        priorities[chr(i)] = i - 38
    for i in range(97, 123):
        priorities[chr(i)] = i - 96

    total = 0

    lines = input_text.splitlines()

    for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]):
        s = set(l1) & set(l2) & set(l3)
        total += priorities[s.pop()]

    return total


if __name__ == '__main__':
    with open('2022/input_files/AoC2022_day03_input.txt') as f:
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
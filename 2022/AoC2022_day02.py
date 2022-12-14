def part1(input_text: str):
    scores = {
        'X': 1,
        'Y': 2,
        'Z': 3,
        'A': 1,
        'B': 2,
        'C': 3,
    }

    s = 0

    for line in input_text.splitlines():
        p1, p2 = [c for c in line.split()]

        s += scores[p2]

        if scores[p2] == scores[p1]:
            s += 3
        elif scores[p2] == (scores[p1] % 3) + 1:
            s += 6
    
    return s


def part2(input_text: str):
    scores = {
        'A': 1,
        'B': 2,
        'C': 3,
    }

    endings = {
        'X': lambda p1: (p1 + 1) % 3 + 1,
        'Y': lambda p1: p1 + 3,
        'Z': lambda p1: (p1 % 3) + 7,
    }
    
    s = 0

    for line in input_text.splitlines():
        p1, p2 = [c for c in line.split()]
        s += endings[p2](scores[p1])

    return s


if __name__ == '__main__':
    with open('2022/input_files/AoC2022_day02_input.txt') as f:
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
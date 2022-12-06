def part1(input_text):
    from collections import deque

    stream = input_text[:-1]
    last4 = deque(maxlen=4)

    for n, c in enumerate(stream, 1):
        last4.append(c)

        if len(set(last4)) == 4:
            return n


def part2(input_text):
    from collections import deque

    stream = input_text[:-1]
    last14 = deque(maxlen=14)

    for n, c in enumerate(stream, 1):
        last14.append(c)

        if len(set(last14)) == 14:
            return n


if __name__ == '__main__':
    with open('./input_files/AoC2022_day06_input.txt') as f:
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
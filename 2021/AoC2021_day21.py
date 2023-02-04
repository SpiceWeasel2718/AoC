def part1(input_text):
    start_pos = []
    
    for line in input_text.splitlines():
        __, pos = line.split(': ')
        start_pos.append(int(pos)-1)
    
    p1, p2 = start_pos

    p1 = (p1 + 6) % 10
    s1 = p1 + 1

    p2 = (p2 + 5) % 10
    s2 = p2 + 1

    turns = 2

    while True:
        p1 = (p1 + 6 - turns) % 10
        s1 += p1 + 1
        turns += 1

        if s1 >= 1000:
            break

        p2 = (p2 + 6 - turns) % 10
        s2 += p2 + 1
        turns += 1

        if s2 >= 1000:
            break
    
    return 3 * turns * min(s1, s2)


def part2(input_text):
    start_pos = []
    
    for line in input_text.splitlines():
        __, pos = line.split(': ')
        start_pos.append(int(pos)-1)

        


if __name__ == '__main__':
    with open('./input_files/AoC2021_day21_input.txt') as f:
        input_text = f.read()

    input_text = """Player 1 starting position: 4
Player 2 starting position: 8"""

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    time_execution = 0

    if time_execution:
        import timeit
        for part in ['part1', 'part2']:
            timer = timeit.Timer(f'{part}(input_text)', globals=globals())
            n, time = timer.autorange()
            print(f'{part} took {time/n:.5f} seconds on average when run {n} times')
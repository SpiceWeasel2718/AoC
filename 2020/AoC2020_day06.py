def part1(input_text):
    count = 0

    for group in input_text.split('\n\n'):
        answers = set(group)
        answers.discard('\n')
        count += len(answers)
    
    return count


def part2(input_text):
    count = 0

    for group in input_text.split('\n\n'):
        answers = set('abcdefghijklmnopqrstuvwxyz')
        for line in group.splitlines():
            answers &= set(line)
        count += len(answers)
    
    return count


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day06_input.txt') as f:
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
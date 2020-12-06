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

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
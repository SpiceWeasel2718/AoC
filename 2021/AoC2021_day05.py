def part1(input_text):
    from collections import defaultdict

    seen = defaultdict(int)

    for line in input_text.splitlines():
        start, end = [complex(*[int(n) for n in point.split(',')]) for point in line.split(' -> ')]
        diff = end - start

        if diff.real == 0 or diff.imag == 0:
            steps = int(abs(diff))
            v = diff / steps
            current = start
            
            for __ in range(steps+1):
                seen[current] += 1
                current += v
    
    return len([v for v in seen.values() if v > 1])


def part2(input_text):
    from collections import defaultdict
    
    seen = defaultdict(int)

    for line in input_text.splitlines():
        start, end = [complex(*[int(n) for n in point.split(',')]) for point in line.split(' -> ')]
        diff = end - start

        if diff.real == 0 or diff.imag == 0:
            steps = int(abs(diff))
        else:
            steps = int(abs(diff.real))
        
        v = diff / steps
        current = start
        
        for __ in range(steps+1):
            seen[current] += 1
            current += v
        
    return len([v for v in seen.values() if v > 1])


if __name__ == '__main__':
    with open('./input_files/AoC2021_day05_input.txt') as f:
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
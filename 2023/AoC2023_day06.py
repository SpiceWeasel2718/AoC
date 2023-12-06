def part1(input_text: str):
    time_text, dist_text = input_text.splitlines()
    times = [int(t) for t in (time_text.split())[1:]]
    distances = [int(d) for d in (dist_text.split())[1:]]

    prod = 1

    for time, dist in zip(times, distances):
        t = 1
        while t * (time - t) <= dist:
            t += 1
        
        prod *= (time - 2 * t + 1)
    
    return prod


def part2(input_text: str):
    time_text, dist_text = input_text.splitlines()
    time = int(''.join((time_text.split())[1:]))
    dist = int(''.join((dist_text.split())[1:]))
    
    t = 1
    while t * (time - t) <= dist:
        t += 1 # could do some sort of binary search or something but meh
    
    return time - 2 * t + 1


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2023_day06_input.txt') as f:
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
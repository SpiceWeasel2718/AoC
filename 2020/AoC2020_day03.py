import math

def part1(input_text):
    slope = input_text.splitlines()
    
    width = len(slope[0])
    pos = 0
    count = 0

    for line in slope[1:]:
        pos = (pos + 3) % width
        count += (line[pos] == '#')
    
    return count


def part2(input_text):
    slope = input_text.splitlines()
    
    width = len(slope[0])
    pos = [0] * 5
    intervals = [1, 3, 5, 7]
    counts = [0] * 5

    for j, line in enumerate(slope[1:]):
        for i in range(4):
            pos[i] = (pos[i] + intervals[i]) % width
            counts[i] += (line[pos[i]] == '#')
        
        if j % 2 == 1:
            pos[4] = (pos[4] + 1) % width
            counts[4] += (line[pos[4]] == '#')
        
    return math.prod(counts)


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day03_input.txt') as f:
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
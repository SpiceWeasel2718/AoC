from collections import deque

def part1(input_text):
    adapters = sorted([int(n) for n in input_text.splitlines()])
    
    counts = {1: 0, 2: 0, 3: 1}
    last = 0

    for ad in adapters:
        counts[ad-last] += 1
        last = ad
        
    return counts[1] * counts[3]


def part2(input_text):
    adapters = sorted([int(n) for n in input_text.splitlines()])

    ways_to_reach = {k: 0 for k in adapters}
    ways_to_reach[0] = 1
    queue = deque([0], 3)

    for ad in adapters:
        bound = ad - 3
        for prev_ad in queue:
            if bound <= prev_ad:
                ways_to_reach[ad] += ways_to_reach[prev_ad]
            else:
                break
        queue.appendleft(ad)
    
    return ways_to_reach[ad]


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day10_input.txt') as f:
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
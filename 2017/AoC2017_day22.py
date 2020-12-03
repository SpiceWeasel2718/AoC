import collections

def part1(input_text):
    grid = collections.defaultdict(int)
    string_values = {'.': 0, '#': 1}

    for y, line in enumerate(input_text):
        grid.update({(x, y): string_values[c] for x, c in enumerate(line)})
    
    pos = (len(input_text[0]) // 2, len(input_text) // 2)
    direction = (0, -1)
    count = 0

    for __ in range(10000):
        direction = (-direction[1], direction[0]) if grid[pos] else (direction[1], -direction[0])
        grid[pos] = (grid[pos] + 1) % 2
        count += grid[pos]
        pos = (pos[0] + direction[0], pos[1] + direction[1])
    
    return count


def part2(input_text):
    grid = collections.defaultdict(int)
    string_values = {'.': 0, '#': 2}

    for y, line in enumerate(input_text):
        grid.update({(x, y): string_values[c] for x, c in enumerate(line)})
    
    pos = (len(input_text[0]) // 2, len(input_text) // 2)
    direction = (0, -1)
    count = 0

    for __ in range(10000000):
        state = grid[pos]
        if state == 0:
            direction = (direction[1], -direction[0])
        elif state == 1:
            count += 1
        elif state == 2:
            direction = (-direction[1], direction[0])
        elif state == 3:
            direction = (-direction[0], -direction[1])

        grid[pos] = (state + 1) % 4
        pos = (pos[0] + direction[0], pos[1] + direction[1])
    
    return count


if __name__ == '__main__':
    from pathlib import Path
    with open(next(Path().glob('**/AoC2017_day22_input.txt'))) as f:
        input_text = f.read().splitlines()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    #print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    #print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
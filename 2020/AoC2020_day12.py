import numpy as np
from itertools import cycle

def part1(input_text):
    headings = cycle([
        np.array([1, 0]),
        np.array([0, 1]),
        np.array([-1, 0]),
        np.array([0, -1]),
    ])
    directions = {
        'E': np.array([1, 0]),
        'N': np.array([0, 1]),
        'W': np.array([-1, 0]),
        'S': np.array([0, -1]),
    }
    angles = {90: 1, 180: 2, 270: 3}
    hands = {'L': 1, 'R': -1}

    heading = next(headings)
    pos = np.array([0, 0])
    
    for instruction in input_text.splitlines():
        c, n = instruction[0], int(instruction[1:])

        if c in directions:
            pos += n * directions[c]
        elif c == 'F':
            pos += n * heading
        else:
            for __ in range((hands[c] * angles[n]) % 4):
                heading = next(headings)
    
    return abs(pos[0]) + abs(pos[1])


def part2(input_text):
    directions = {
        'E': np.array([1, 0]),
        'N': np.array([0, 1]),
        'W': np.array([-1, 0]),
        'S': np.array([0, -1]),
    }
    angles = {
        ('L', 90): 1, 
        ('L', 270): -1, 
        ('R', 90): -1, 
        ('R', 270): 1,
    }

    pos = np.array([0, 0])
    waypoint = np.array([10, 1])
    
    for instruction in input_text.splitlines():
        c, n = instruction[0], int(instruction[1:])

        if c in directions:
            waypoint += n * directions[c]
        elif c == 'F':
            pos += n * waypoint
        elif n == 180:
            waypoint *= -1
        else:
            x, y = waypoint
            waypoint = angles[(c, n)] * np.array([-y, x])
    
    return abs(pos[0]) + abs(pos[1])


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day12_input.txt') as f:
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
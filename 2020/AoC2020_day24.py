import re
from collections import defaultdict


def part1(input_text):
    directions = {
        'e': 2, 
        'w': -2, 
        'ne': 1 + 1j, 
        'se': 1 - 1j, 
        'nw': -1 + 1j, 
        'sw': -1 - 1j, 
    }
    floor = defaultdict(bool)

    for line in input_text.splitlines():
        tile = 0
        for direction in re.finditer('e|w|\w\w', line):
            tile += directions[direction.group()]
        floor[tile] = not floor[tile]
    
    return sum(floor.values())


def part2(input_text):
    directions = {
        'e': 2, 
        'w': -2, 
        'ne': 1 + 1j, 
        'se': 1 - 1j, 
        'nw': -1 + 1j, 
        'sw': -1 - 1j, 
    }
    floor = defaultdict(bool)

    for line in input_text.splitlines():
        tile = 0
        for direction in re.finditer('e|w|\w\w', line):
            tile += directions[direction.group()]
        floor[tile] = not floor[tile]
    
    for tile, color in list(floor.items()):
        if color:
            for nbr in [tile + nbr for nbr in directions.values()]:
                floor.setdefault(nbr, False)
    
    for __ in range(100):
        old_floor = floor.copy()

        for tile in list(floor):
            neighbors = [tile + nbr for nbr in directions.values()]
            black_nbrs = sum(old_floor[nbr] for nbr in neighbors)

            if old_floor[tile]:
                floor[tile] = (0 < black_nbrs < 3)
            else:
                floor[tile] = (black_nbrs == 2)
            
            if floor[tile]:
                for nbr in neighbors:
                    floor.setdefault(nbr, False)

    return sum(floor.values())


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day24_input.txt') as f:
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
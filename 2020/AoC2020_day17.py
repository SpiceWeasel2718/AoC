from collections import defaultdict
from itertools import product

def part1(input_text):
    grid = defaultdict(bool)

    for x, line in enumerate(input_text.splitlines()):
        for y, char in enumerate(line):
            if char == '#':
                grid[(x, y, 0)] = True
                for nbr in product([x-1, x, x+1], [y-1, y, y+1], [-1, 0, 1]):
                    grid.setdefault(nbr, False)
            else:
                grid[(x, y, 0)] = False

    neighborhoods = {}

    for __ in range(6):
        old_grid = grid.copy()
        grid = defaultdict(bool)
        keys = list(old_grid.keys())

        for pos in keys:
            if pos not in neighborhoods:
                x, y, z = pos
                neighborhoods[pos] = list(product([x-1, x, x+1], [y-1, y, y+1], [z-1, z, z+1]))

            s = sum(old_grid[nbr] for nbr in neighborhoods[pos])
            
            if old_grid[pos]:
                grid[pos] = (3 <= s <= 4)
            else:
                if s == 3:
                    grid[pos] = True
                    for nbr in neighborhoods[pos]:
                        grid.setdefault(nbr, False)
                else:
                    grid[pos] = False
        
    return sum(grid.values())


def part2(input_text):
    grid = defaultdict(bool)

    for x, line in enumerate(input_text.splitlines()):
        for y, char in enumerate(line):
            if char == '#':
                grid[(x, y, 0, 0)] = True
                for nbr in product([x-1, x, x+1], [y-1, y, y+1], [-1, 0, 1], [-1, 0, 1]):
                    grid.setdefault(nbr, False)
            else:
                grid[(x, y, 0, 0)] = False

    neighborhoods = {}

    for __ in range(6):
        old_grid = grid.copy()
        grid = defaultdict(bool)
        keys = list(old_grid.keys())

        for pos in keys:
            if pos not in neighborhoods:
                x, y, z, w = pos
                neighborhoods[pos] = list(product([x-1, x, x+1], [y-1, y, y+1], [z-1, z, z+1], [w-1, w, w+1]))

            s = sum(old_grid[nbr] for nbr in neighborhoods[pos])
            
            if old_grid[pos]:
                grid[pos] = (3 <= s <= 4)
            else:
                if s == 3:
                    grid[pos] = True
                    for nbr in neighborhoods[pos]:
                        grid.setdefault(nbr, False)
                else:
                    grid[pos] = False
        
    return sum(grid.values())


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day17_input.txt') as f:
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
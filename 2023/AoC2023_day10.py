def part1(input_text: str):
    pipes = {
        '|': {-1: -1, 1: 1},
        '-': {1j: 1j, -1j: -1j},
        'L': {1: 1j, -1j: -1},
        'J': {1j: -1, 1: -1j},
        '7': {1j: 1, -1: -1j},
        'F': {-1: 1j, -1j: 1},
    }
    tiles = {}

    for a, line in enumerate(input_text.splitlines()):
        for b, c in enumerate(line):
            tiles[a + b*1j] = c
            if c == 'S':
                start = a + b*1j

    if tiles[start+1] in ['|', 'L', 'J']:
        v = 1
    elif tiles[start-1] in ['|', '7', 'F']:
        v = -1
    else:
        v = 1j
    
    current = start + v
    steps = 1

    while current != start:
        v = pipes[tiles[current]][v]
        current += v
        steps += 1
    
    return (steps + 1) // 2


def part2(input_text: str):
    pipes = {
        '|': {-1: -1, 1: 1},
        '-': {1j: 1j, -1j: -1j},
        'L': {1: 1j, -1j: -1},
        'J': {1j: -1, 1: -1j},
        '7': {1j: 1, -1: -1j},
        'F': {-1: 1j, -1j: 1},
    }
    tiles = {}

    for a, line in enumerate(input_text.splitlines()):
        for b, c in enumerate(line):
            tiles[a + b*1j] = c
            if c == 'S':
                start = a + b*1j

    if tiles[start+1] in ['|', 'L', 'J']:
        v = 1
    elif tiles[start-1] in ['|', '7', 'F']:
        v = -1
    else:
        v = 1j
    
    current = start + v
    path = [start]
    v_list = [v]

    while current != start:
        path.append(current)
        v = pipes[tiles[current]][v]
        v_list.append(v)
        current += v
    
    path_set = set(path)

    # While traversing the loop, the interior will always be on your left 
    # with the outside on your right or vice versa. We need to determine 
    # which case we're working with, so we draw a line from the edge until 
    # it intersects the loop. This will tell us which side is the outside.
    out_check = start.real

    while out_check not in path_set:
        out_check += 1j

    ind = path.index(out_check)

    if path[ind-1] == out_check-1:
        rot = 1j
    elif path[ind-1] == out_check+1j:
        rot = 1j if path[ind+1] == out_check+1 else -1j
    else:
        rot = -1j

    # If we grab all the tiles of the interior that are adjacent to a tile 
    # of the loop, we can then expand that set to get the full interior. 
    interior = set()

    for i, pos, v in zip(range(len(path)), path, v_list):
        orth = rot * v
        if pos + orth == path[i-1]:
            continue
        adj = {pos+orth, pos+orth-v, pos-v}
        interior |= adj - path_set

    nbrs = [-1, 1j, 1, -1j]
    checking = list(interior)
    to_check = []
    seen = set()
    seen |= path_set

    while checking:
        seen.update(checking)

        for pos in checking:
            for d in nbrs:
                p = pos + d
                if p not in seen:
                    to_check.append(p)
        
        checking = to_check
        to_check = []
    
    return len(seen) - len(path_set)


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2023_day10_input.txt') as f:
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
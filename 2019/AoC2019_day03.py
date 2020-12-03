def add_vectors(v1, v2):
    return tuple(v1[i] + v2[i] for i in range(2))


def part1(input_text):
    wire1 = input_text[0].split(',')
    wire2 = input_text[1].split(',')
    
    path1 = set()
    path2 = set()
    pos = (0,0)
    directions = {
        'R': (1,0),
        'D': (0,-1),
        'L': (-1,0),
        'U': (0,1)
    }
    
    for move in wire1:
        dist = int(move[1:])
        direction = directions[move[0]]
        for _ in range(dist):
            pos = add_vectors(pos, direction)
            path1.add(pos)
    pos = (0,0)
    for move in wire2:
        dist = int(move[1:])
        direction = directions[move[0]]
        for _ in range(dist):
            pos = add_vectors(pos, direction)
            path2.add(pos)
    
    min_dist = 10000
    for cross in path1.intersection(path2):
        min_dist = min(min_dist, abs(cross[0]) + abs(cross[1]))
    
    return min_dist


def part2(input_text):
    wire1 = input_text[0].split(',')
    wire2 = input_text[1].split(',')
    
    path1 = {}
    path2 = {}
    pos = (0,0)
    steps = 0
    directions = {
        'R': (1,0),
        'D': (0,-1),
        'L': (-1,0),
        'U': (0,1)
    }
    
    for move in wire1:
        dist = int(move[1:])
        direction = directions[move[0]]
        for _ in range(dist):
            steps += 1
            pos = add_vectors(pos, direction)
            path1.setdefault(pos, steps)

    pos = (0,0)
    steps = 0

    for move in wire2:
        dist = int(move[1:])
        direction = directions[move[0]]
        for _ in range(dist):
            steps += 1
            pos = add_vectors(pos, direction)
            path2.setdefault(pos, steps)
    
    min_steps = 10000
    for node in path1:
        if node not in path2:
            continue
        else:
            min_steps = min(min_steps, path1[node] + path2[node])
    
    return min_steps


if __name__ == "__main__":
    from pathlib import Path
    with open(next(Path().glob('**/AoC2019_day03_input.txt'))) as f:
        input_text = f.read().split('\n')

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
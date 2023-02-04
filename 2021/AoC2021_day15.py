def part1(input_text):
    from math import inf
    from functools import total_ordering
    
    cave = {}

    for a, line in enumerate(input_text.splitlines()):
        for b, c in enumerate(line):
            cave[complex(a, b)] = int(c)
    
    cave_exit = complex(a, b)
    
    directions = [1, 1j, -1, -1j]

    @total_ordering
    class Node:
        def __init__(self, pos):
            self.pos = pos
            self.risk = inf
            self.nbrs = {pos+d for d in directions if pos+d in cave}
        
        def __eq__(self, other):
            return self.risk == other

        def __lt__(self, other):
            return self.risk < other

    node_map = {pos: Node(pos) for pos in cave}
    node_map[0].risk = 0
    seen = set()
    accessible = {0}

    while cave_exit not in seen:
        node = min(node_map[pos] for pos in accessible)

        for nbr in node.nbrs:
            if nbr not in seen:
                new_risk = node.risk + cave[nbr]
                node_map[nbr].risk = min(node_map[nbr].risk, new_risk)
                accessible.add(nbr)
        
        seen.add(node.pos)
        accessible.remove(node.pos)
    
    return node_map[cave_exit].risk
        

def part2(input_text):
    from math import inf
    from functools import total_ordering
    
    cave = {}

    for a, line in enumerate(input_text.splitlines()):
        for b, c in enumerate(line):
            cave[complex(a, b)] = int(c)
    
    vert, horiz = a+1, b+1
    base_cave = list(cave.keys())

    for v in range(5):
        for h in range(5):
            if v == 0 and h == 0:
                continue
            for pos in base_cave:
                r = cave[pos]+v+h
                cave[pos + v*vert + h*horiz*1j] = (r % 10) + r // 10
    
    cave_exit = complex(5*vert-1, 5*horiz-1)
    
    directions = [1, 1j, -1, -1j]

    @total_ordering
    class Node:
        def __init__(self, pos):
            self.pos = pos
            self.risk = inf
            self.nbrs = {pos+d for d in directions if pos+d in cave}
        
        def __eq__(self, other):
            return self.risk == other

        def __lt__(self, other):
            return self.risk < other

    node_map = {pos: Node(pos) for pos in cave}
    node_map[0].risk = 0
    seen = set()
    accessible = {0}

    while cave_exit not in seen:
        node = min(node_map[pos] for pos in accessible)

        for nbr in node.nbrs:
            if nbr not in seen:
                new_risk = node.risk + cave[nbr]
                node_map[nbr].risk = min(node_map[nbr].risk, new_risk)
                accessible.add(nbr)
        
        seen.add(node.pos)
        accessible.remove(node.pos)
    
    return node_map[cave_exit].risk


if __name__ == '__main__':
    with open('./input_files/AoC2021_day15_input.txt') as f:
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
import collections
from intcode import IntComp
import concurrent.futures

def map_area(computer):
        layout = collections.defaultdict(lambda: -1)
        pos = (0, 0)
        direction = (1, 0)
        inputs = {(0, 1): 1, (0, -1): 2, (1, 0): 3, (-1, 0): 4}
        layout[pos] = 1

        while True:
            computer.append_inputs(inputs[direction])
            computer.waiting_on_input.wait()
            reply = computer.outputs.pop()
            target = (pos[0] + direction[0], pos[1] + direction[1])
            layout[target] = reply

            if reply == 0:
                direction = (direction[1], -direction[0])
            else:
                if target == (0, 0):
                    break
                pos = target
                direction = (-direction[1], direction[0])
        
        computer.halt()
        return layout


def map_to_string(layout):
    maxx = 0
    maxy = 0
    minx = 0
    miny = 0
    for x, y in layout:
        maxx = max(x, maxx)
        maxy = max(y, maxy)
        minx = min(x, minx)
        miny = min(y, miny)
    
    conversions = {-1: ' ', 0: '#', 1: '.', 2: 'O'}
    rows = []
    for y in range(maxy, miny-1, -1):
        row = []
        for x in range(minx, maxx+1):
            if x== 0 and y == 0:
                row.append('X')
            else:
                row.append(conversions[layout[(x, y)]])
        rows.append(''.join(row))

    return '\n'.join(rows)


def part1(input_text):
    computer = IntComp(input_text[0])

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(computer.execute)
        layout = executor.submit(map_area, computer).result()
    
    def get_nbrs(pos):
        return [(pos[0]+v[0], pos[1]+v[1]) for v in [(1, 0), (0, 1), (-1, 0), (0, -1)]]

    pos = (0, 0)
    steps = 0
    paths = collections.deque()
    paths.append((pos, steps))
    seen = set()
    seen.add(pos)

    while layout[pos] != 2:
        pos, steps = paths.popleft()
        seen.add(pos)
        
        for nbr in [nbr for nbr in get_nbrs(pos) if layout[nbr] > 0 and nbr not in seen]:
            paths.appendleft((nbr, steps+1))
    
    return steps


def part2(input_text):
    computer = IntComp(input_text[0])

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(computer.execute)
        layout = executor.submit(map_area, computer).result()
    
    for coords, value in layout.items():
        if value == 2:
            goal = coords
            break
    
    def get_nbrs(pos):
        return [(pos[0]+v[0], pos[1]+v[1]) for v in [(1, 0), (0, 1), (-1, 0), (0, -1)]]

    unseen = set([coords for coords in layout if layout[coords] == 1])
    queue = collections.deque()
    queue.append((goal, 0))
    max_steps = 0

    while len(queue) > 0:
        pos, steps = queue.popleft()
        max_steps = max(max_steps, steps)
        valid_nbrs = [nbr for nbr in get_nbrs(pos) if layout[nbr] == 1 and nbr in unseen]
        for nbr in valid_nbrs:
            queue.append((nbr, steps+1))
            unseen.remove(nbr)

    return max_steps


if __name__ == '__main__':
    from pathlib import Path
    with open(next(Path().glob('**/AoC2019_day15_input.txt'))) as f:
        input_text = f.read().splitlines()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
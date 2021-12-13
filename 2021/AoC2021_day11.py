def part1(input_text):
    from collections import deque

    lines = input_text.splitlines()
    octopi = {}

    for a, line in enumerate(lines):
        for b, n in enumerate(line):
            octopi[complex(a, b)] = int(n)

    nbrs = {o: set() for o in octopi}
    directions = [1, 1+1j, 1j, -1+1j, -1, -1-1j, -1j, 1-1j]
    
    for o in octopi:
        for d in directions:
            if (nbr := o + d) in octopi:
                nbrs[o].add(nbr)

    num_flashes = 0
    flashed = set()
    queue = deque()

    for __ in range(100):
        flashed.clear()

        for o in octopi:
            octopi[o] += 1

            if octopi[o] > 9:
                queue.append(o)
                flashed.add(o)
        
        while queue:
            o = queue.pop()

            for nbr in nbrs[o]:
                octopi[nbr] += 1
                if octopi[nbr] > 9 and nbr not in flashed:
                    queue.append(nbr)
                    flashed.add(nbr)

        for o in flashed:
            octopi[o] = 0
        
        num_flashes += len(flashed)
        
    return num_flashes
                    

def part2(input_text):
    from collections import deque

    lines = input_text.splitlines()
    octopi = {}

    for a, line in enumerate(lines):
        for b, n in enumerate(line):
            octopi[complex(a, b)] = int(n)
    
    nbrs = {o: set() for o in octopi}
    directions = [1, 1+1j, 1j, -1+1j, -1, -1-1j, -1j, 1-1j]
    
    for o in octopi:
        for d in directions:
            if (nbr := o + d) in octopi:
                nbrs[o].add(nbr)

    steps = 0
    n_octopi = len(octopi)
    flashed = set()
    queue = deque()

    while len(flashed) < n_octopi:
        steps += 1
        flashed.clear()

        for o in octopi:
            octopi[o] += 1

            if octopi[o] > 9:
                queue.append(o)
                flashed.add(o)
        
        while queue:
            o = queue.pop()

            for nbr in nbrs[o]:
                octopi[nbr] += 1
                if octopi[nbr] > 9 and nbr not in flashed:
                    queue.append(nbr)
                    flashed.add(nbr)

        for o in flashed:
            octopi[o] = 0
        
    return steps


if __name__ == '__main__':
    with open('./input_files/AoC2021_day11_input.txt') as f:
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
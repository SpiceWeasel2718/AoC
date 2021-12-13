def part1(input_text):
    heights = {n : set() for n in range(10)}

    for a, line in enumerate(input_text.splitlines()):
        for b, char in enumerate(line):
            heights[int(char)].add(complex(a, b))
    
    nbrs = [1, 1j, -1, -1j]

    for h in range(7, -1, -1):
        for point in heights[h]:
            to_remove = {point + nbr for nbr in nbrs}
            for h2 in range(h+1, 9):
                heights[h2] -= to_remove
    
    return sum(risk * len(heights[risk-1]) for risk in range(1, 10))
            

def part2(input_text):
    from collections import deque

    terrain = set()

    for a, line in enumerate(input_text.splitlines()):
        for b, char in enumerate(line):
            if int(char) < 9:
                terrain.add(complex(a, b))
    
    nbrs = [1, 1j, -1, -1j]
    basin_sizes = []
    queue = deque()
    
    while terrain:
        queue.append(terrain.pop())
        size = 1

        while queue:
            current = queue.pop()

            for nbr in nbrs:
                if (test := current + nbr) in terrain:
                    queue.append(test)
                    terrain.remove(test)
                    size += 1
        
        basin_sizes.append(size)

    n = 1
    
    for s in sorted(basin_sizes)[-3:]:
        n *= s
    
    return n


if __name__ == '__main__':
    with open('./input_files/AoC2021_day09_input.txt') as f:
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
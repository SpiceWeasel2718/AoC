def part1(input_text):
    height_map = {}
    
    for re, line in enumerate(input_text.splitlines()):
        for im, c in enumerate(line):
            pos = re + im*1j
            match c:
                case 'S':
                    start = pos
                    height_map[pos] = ord('a')
                case 'E':
                    end = pos
                    height_map[pos] = ord('z')
                case _:
                    height_map[pos] = ord(c)
    
    eff_inf = len(height_map)
    distances = {pos : eff_inf for pos in height_map}
    distances[start] = 0
    unvisited = set(height_map)
    pos = start
    
    while end in unvisited:
        pos = min(unvisited, key=lambda p : distances[p])
        
        for d in [1, -1, 1j, -1j]:
            if (nbr := pos + d) in unvisited and height_map[nbr]-height_map[pos] <= 1:
                distances[nbr] = min(distances[pos] + 1, distances[nbr])
        
        unvisited.remove(pos)
        
    return distances[end]


def part2(input_text):
    height_map = {}
    
    for re, line in enumerate(input_text.splitlines()):
        for im, c in enumerate(line):
            pos = re + im*1j
            match c:
                case 'S':
                    start = pos
                    height_map[pos] = ord('a')
                case 'E':
                    end = pos
                    height_map[pos] = ord('z')
                case _:
                    height_map[pos] = ord(c)
    
    eff_inf = len(height_map)
    distances = {pos : eff_inf for pos in height_map}
    distances[end] = 0
    unvisited = set(height_map)
    a_set = {pos for pos in height_map if height_map[pos] == ord('a')}
    pos = end
    
    while unvisited:
        pos = min(unvisited, key=lambda p : distances[p])
        
        for d in [1, -1, 1j, -1j]:
            if (nbr := pos + d) in unvisited and height_map[nbr]-height_map[pos] >= -1:
                distances[nbr] = min(distances[pos] + 1, distances[nbr])
        
        unvisited.remove(pos)

    return min(distances[a] for a in a_set)


if __name__ == '__main__':
    with open('./input_files/AoC2022_day12_input.txt') as f:
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
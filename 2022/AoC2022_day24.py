def part1(input_text: str):
    from math import lcm, inf
    from collections import defaultdict
    
    blizzards = []
    safe_times = {}
    lines = input_text.splitlines()
    x_max = len(lines[0]) - 3
    y_max = len(lines) - 3
    directions = {'>': 1, 'v': -1j, '<': -1, '^': 1j}
    
    for b, line in enumerate(lines, start=-1):
        for a, c in enumerate(line, start=-1):
            if c == '#':
                continue
            
            pos = a - b*1j
            safe_times[pos] = set()
            
            if c == '.':
                if b == -1:
                    start = pos
                elif b == y_max + 1:
                    end = pos
                safe_times[pos].add(0)
            else:
                blizzards.append((pos, directions[c]))

    cycle = lcm(x_max + 1, y_max + 1)
    
    for t in range(1, cycle):
        new_blizzards = []
        occupied = set()
        
        for bliz, d in blizzards:
            new_pos = bliz + d
            r, i = new_pos.real, new_pos.imag
            
            match d:
                case 1:
                    if r == x_max + 1:
                        new_pos = i*1j
                case -1:
                    if r == -1:
                        new_pos = x_max + i*1j
                case 1j:
                    if i == 1:
                        new_pos = r - y_max*1j
                case -1j:
                    if i == -y_max - 1:
                        new_pos = r
            
            new_blizzards.append((new_pos, d))
            occupied.add(new_pos)
        
        blizzards = new_blizzards
        
        for pos in safe_times:
            if pos not in occupied:
                safe_times[pos].add(t)
    
    
    unvisited = defaultdict(lambda : inf)
    visited = {(start, 0) : 0}
    
    current_pos = start
    time = 0
    nbrs = [1, -1j, -1, 1j, 0]
    
    while current_pos != end:
        time += 1
        
        for nbr in [current_pos + d for d in nbrs]:
            if nbr not in visited and nbr in safe_times and (t_mod := time % cycle) in safe_times[nbr]:
                new_state = (nbr, t_mod)
                unvisited[new_state] = min(unvisited[new_state], time)

        state = min(unvisited, key=lambda s : unvisited[s] + abs(s[0] - end))
        current_pos, __ = state
        time = unvisited[state]
        visited[state] = time
        del unvisited[state]
    
    return time
    
    
def part2(input_text: str):
    from math import lcm, inf
    from collections import defaultdict
    
    blizzards = []
    safe_times = {}
    lines = input_text.splitlines()
    x_max = len(lines[0]) - 3
    y_max = len(lines) - 3
    directions = {'>': 1, 'v': -1j, '<': -1, '^': 1j}
    
    for b, line in enumerate(lines, start=-1):
        for a, c in enumerate(line, start=-1):
            if c == '#':
                continue
            
            pos = a - b*1j
            safe_times[pos] = set()
            
            if c == '.':
                if b == -1:
                    start = pos
                elif b == y_max + 1:
                    end = pos
                safe_times[pos].add(0)
            else:
                blizzards.append((pos, directions[c]))

    cycle = lcm(x_max + 1, y_max + 1)
    
    for t in range(1, cycle):
        new_blizzards = []
        occupied = set()
        
        for bliz, d in blizzards:
            new_pos = bliz + d
            r, i = new_pos.real, new_pos.imag
            
            match d:
                case 1:
                    if r == x_max + 1:
                        new_pos = i*1j
                case -1:
                    if r == -1:
                        new_pos = x_max + i*1j
                case 1j:
                    if i == 1:
                        new_pos = r - y_max*1j
                case -1j:
                    if i == -y_max - 1:
                        new_pos = r
            
            new_blizzards.append((new_pos, d))
            occupied.add(new_pos)
        
        blizzards = new_blizzards
        
        for pos in safe_times:
            if pos not in occupied:
                safe_times[pos].add(t)
    
    
    unvisited = defaultdict(lambda : inf)
    visited = {(start, 0) : 0}
    
    current_pos = start
    time = 0
    nbrs = [1, -1j, -1, 1j, 0]
    
    while current_pos != end:
        time += 1
        
        for nbr in [current_pos + d for d in nbrs]:
            if nbr not in visited and nbr in safe_times and (t_mod := time % cycle) in safe_times[nbr]:
                new_state = (nbr, t_mod)
                unvisited[new_state] = min(unvisited[new_state], time)

        state = min(unvisited, key=lambda s : unvisited[s] + abs(s[0] - end))
        current_pos, __ = state
        time = unvisited[state]
        visited[state] = time
        del unvisited[state]
    
    unvisited = defaultdict(lambda : inf)
    visited = {(end, time % cycle) : time}
    
    while current_pos != start:
        time += 1
        
        for nbr in [current_pos + d for d in nbrs]:
            if nbr not in visited and nbr in safe_times and (t_mod := time % cycle) in safe_times[nbr]:
                new_state = (nbr, t_mod)
                unvisited[new_state] = min(unvisited[new_state], time)

        state = min(unvisited, key=lambda s : unvisited[s] + abs(s[0] - start))
        current_pos, __ = state
        time = unvisited[state]
        visited[state] = time
        del unvisited[state]
    
    unvisited = defaultdict(lambda : inf)
    visited = {(start, time % cycle) : time}
    
    while current_pos != end:
        time += 1
        
        for nbr in [current_pos + d for d in nbrs]:
            if nbr not in visited and nbr in safe_times and (t_mod := time % cycle) in safe_times[nbr]:
                new_state = (nbr, t_mod)
                unvisited[new_state] = min(unvisited[new_state], time)

        state = min(unvisited, key=lambda s : unvisited[s] + abs(s[0] - end))
        current_pos, __ = state
        time = unvisited[state]
        visited[state] = time
        del unvisited[state]
    
    return time


if __name__ == '__main__':
    with open('2022/input_files/AoC2022_day24_input.txt') as f:
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

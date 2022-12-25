def part1(input_text: str):
    import re
    
    board = {}
    loop = {}
    n_cols = 0
    
    for a, line in enumerate(input_text.splitlines(), 1):
        if not line:
            continue
        
        if not line[0].isnumeric():
            l = 0
            
            for b, c in enumerate(line, 1):
                if c == '.':
                    board[a + b*1j] = False
                elif c == '#':
                    board[a + b*1j] = True
                else:
                    l += 1
            
            n_cols = max(n_cols, b)
            r = b + 1
            loop[a + l*1j] = a + (r-1)*1j
            loop[a + r*1j] = a + (l+1)*1j
        else:
            path = line
    
    for i in range(1, n_cols+1):
        min_val = min(z.real for z in board if z.imag == i)
        max_val = max(z.real for z in board if z.imag == i)
        loop[min_val - 1 + i*1j] = max_val + i*1j
        loop[max_val + 1 + i*1j] = min_val + i*1j
    
    distances = [int(n) for n in re.findall(r'\d+', path)]
    turns = [n for n in map(lambda rl : -1j if rl == 'R' else 1j, re.findall(r'\D', path))]
    turns_iter = iter(turns)
    
    pos = 1 + min(z.imag for z in board if z.real == 1)*1j
    facing = 1j
    
    for dist in distances:
        for __ in range(dist):
            new_pos = pos + facing
            if new_pos not in board:
                new_pos = loop[new_pos]
            
            if board[new_pos]:
                break
            else:
                pos = new_pos
        
        try:
            facing *= next(turns_iter)
        except StopIteration:
            pass
    
    facing_factor = {
        1j: 0,
        1: 1,
        -1j: 2,
        -1: 3,
    }
    
    return 1000 * int(pos.real) + 4 * int(pos.imag) + facing_factor[facing]
            

def part2(input_text: str):
    import re
    
    input_lines = input_text.splitlines()
    board = {}
    
    for a, line in enumerate(input_lines[:-2], 1):
        for b, c in enumerate(line, 1):
            if c == '.':
                board[a + b*1j] = False
            elif c == '#':
                board[a + b*1j] = True

    path = input_lines[-1]
    distances = [int(n) for n in re.findall(r'\d+', path)]
    turns_iter = iter(map(lambda rl : -1j if rl == 'R' else 1j, re.findall(r'\D', path)))
    
    bdry = {}
    edges = []
    edge_length = 50
    d = edge_length - 1
    corners = [d+d*1j, d*1j, 0, d]
    
    for a in range(1, 5*edge_length, edge_length):
        for b in range(1, 5*edge_length, edge_length):
            z = a + b*1j
            if z not in board:
                continue
            
            normal = 1j
            
            for c in [z + w for w in corners]:
                if c + normal not in board:
                    pair = c + normal + normal*-1j
                    if pair in board:
                        pair_normal = normal*1j
                        dc = pair_normal
                        dp = normal
                        for i in range(edge_length):
                            e1 = c + i*dc
                            e2 = pair + i*dp
                            bdry[(e1 + normal, normal)] = (e2, -pair_normal)
                            bdry[(e2 + pair_normal, pair_normal)] = (e1, -normal)
                    else:
                        edges.append((c, normal))
                normal *= 1j
    
    while edges:
        new_edges = []
        
        for c, normal in edges:
            if c + normal in bdry:
                continue
            
            pair = None
            zn = normal*-1j
            z = c + zn
            
            if z in board:
                wn = normal
                w = z + wn
                if (w, wn) in bdry:
                    pair, v = bdry[(w, wn)]
                    pair_normal = v*1j
            elif (z, zn) in bdry:
                bz, bzn = bdry[(z, zn)]
                wn = bzn*1j
                w = bz + wn
                if w in board:
                    pair = w
                    pair_normal = wn*1j
                elif (w, wn) in bdry:
                    pair, v = bdry[(w, wn)]
                    pair_normal = v*1j
            
            if pair is not None:
                dc = normal*1j
                dp = pair_normal*-1j
                for i in range(edge_length):
                    e1 = c + i*dc
                    e2 = pair + i*dp
                    bdry[(e1 + normal, normal)] = (e2, -pair_normal)
                    bdry[(e2 + pair_normal, pair_normal)] = (e1, -normal)
            else:
                new_edges.append((c, normal))
        
        edges = new_edges
    
    pos = 1 + min(z.imag for z in board if z.real == 1)*1j
    facing = 1j
    
    for dist in distances:
        for __ in range(dist):
            new_pos = pos + facing
            
            if new_pos not in board:
                new_pos, new_facing = bdry[(new_pos, facing)]
                
                if board[new_pos]:
                    break
                else:
                    pos, facing = new_pos, new_facing
            
            if board[new_pos]:
                break
            else:
                pos = new_pos
        
        try:
            facing *= next(turns_iter)
        except StopIteration:
            pass
    
    facing_factor = {
        1j: 0,
        1: 1,
        -1j: 2,
        -1: 3,
    }
    
    return 1000 * int(pos.real) + 4 * int(pos.imag) + facing_factor[facing]


if __name__ == '__main__':
    with open('2022/input_files/AoC2022_day22_input.txt') as f:
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
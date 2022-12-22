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
    
    board = {}
    loop = {}
    
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
            path = line
    
    for i in range(1, 51):
        loop[i + 50*1j] = (151 - i + 1j, 1j)
        loop[100 + i + 0*1j] = (51 - i + 51*1j, 1j)
        
        loop[i + 151*1j] = (151 - i + 100*1j, -1j)
        loop[100 + i + 101*1j] = (51 - i + 150*1j, -1j)
        
        loop[50 + i + 50*1j] = (101 + i*1j, 1)
        loop[100 + i*1j] = (50 + i + 51*1j, 1j)
        
        loop[50 + i + 101*1j] = (50 + (100 + i)*1j, -1)
        loop[51 + (100 + i)*1j] = (50 + i + 100*1j, -1j)
        
        loop[150 + i + 0*1j] = (1 + (50 + i)*1j , 1)
        loop[0 + (50 + i)*1j] = (150 + i + 1j, 1j)
        
        loop[150 + i + 51*1j] = (150 + (50 + i)*1j , -1)
        loop[151 + (50 + i)*1j] = (150 + i + 50*1j, -1j)
        
        loop[201 + i*1j] = (1 + (100 + i)*1j , 1)
        loop[0 + (100 + i)*1j] = (200 + i*1j, -1)
    
    distances = [int(n) for n in re.findall(r'\d+', path)]
    turns_iter = iter(map(lambda rl : -1j if rl == 'R' else 1j, re.findall(r'\D', path)))
    
    pos = 1 + min(z.imag for z in board if z.real == 1)*1j
    facing = 1j
    
    for dist in distances:
        for __ in range(dist):
            new_pos = pos + facing
            
            if new_pos not in board:
                new_pos, new_facing = loop[new_pos]
                
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
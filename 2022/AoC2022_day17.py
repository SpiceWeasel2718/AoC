def part1(input_text: str):
    from itertools import cycle
    
    jets = []
    
    for c in input_text:
        if c == '<':
            jets.append(-1)
        elif c == '>':
            jets.append(1)
    
    rocks = {i+0j for i in range(7)}
    
    block_sets = [
        # minus block
        lambda pos : {pos + i for i in range(4)},
        # plus block
        lambda pos : {pos+1, pos+1j, pos+1+1j, pos+2+1j, pos+1+2j},
        # mirrored L block
        lambda pos : {pos, pos+1, pos+2, pos+2+1j, pos+2+2j},
        # | block
        lambda pos : {pos + i*1j for i in range(4)},
        # square block
        lambda pos : {pos, pos+1, pos+1j, pos+1+1j}
    ]
    
    height = 0
    jets_iter = iter(cycle(jets))
    block_sets_iter = iter(cycle(block_sets))
    
    for __ in range(2022):
        pos = 2 + (height + 4)*1j
        block_set = next(block_sets_iter)
        moving = True
        
        while moving:
            new_pos = pos + next(jets_iter)
            block = block_set(new_pos)
            right = max(p.real for p in block)
            if 0 <= new_pos.real and right <= 6 and all(p not in rocks for p in block):
                pos = new_pos
            
            new_pos = pos - 1j
            block = block_set(new_pos)
            if pos.imag > height + 1 or all(p not in rocks for p in block):
                pos = new_pos
            else:
                moving = False
                block = block_set(pos)
                rocks.update(block)
                height = max(height, max(p.imag for p in block))
    
    return int(height)
    

def part2(input_text: str):
    jets = []
    
    for c in input_text:
        if c == '<':
            jets.append(-1)
        elif c == '>':
            jets.append(1)
    
    n_jets = len(jets)
    
    rocks = {i+0j for i in range(7)}
    
    block_sets = [
        # minus block
        lambda pos : {pos + i for i in range(4)},
        # plus block
        lambda pos : {pos+1, pos+1j, pos+1+1j, pos+2+1j, pos+1+2j},
        # mirrored L block
        lambda pos : {pos, pos+1, pos+2, pos+2+1j, pos+2+2j},
        # | block
        lambda pos : {pos + i*1j for i in range(4)},
        # square block
        lambda pos : {pos, pos+1, pos+1j, pos+1+1j}
    ]
    
    height = 0
    jets_i = 0
    block_sets_i = 0
    history = []
    states = {}
    
    for block_num in range(1000000000000):
        state = (block_sets_i, jets_i)
        history.append(state)
        
        if state not in states:
            states[state] = [(block_num, height)]
        else:
            states[state].append((block_num, height))
            past_n, past_h = states[state][-2]
            if (cycle_len := block_num - past_n) <= past_n:
                if all(s0 == s1 for s0, s1 in zip(history[block_num:past_n:-1], history[past_n::-1])):
                    dh = height - past_h
                    remaining_blocks = 1000000000000 - block_num
                    height += dh * (remaining_blocks // cycle_len)
                    remainder = remaining_blocks % cycle_len
                    if remainder:
                        s = history[past_n + remainder]
                        n, h = states[s][-1]
                        height += h - past_h
                        
                    return int(height)
        
        pos = 2 + (height + 4)*1j
        block_set = block_sets[block_sets_i]
        block_sets_i = (block_sets_i + 1) % 5
        moving = True
        
        while moving:
            new_pos = pos + jets[jets_i]
            jets_i = (jets_i + 1) % n_jets
            block = block_set(new_pos)
            right = max(p.real for p in block)
            if 0 <= new_pos.real and right <= 6 and all(p not in rocks for p in block):
                pos = new_pos
            
            new_pos = pos - 1j
            block = block_set(new_pos)
            if pos.imag > height + 1 or all(p not in rocks for p in block):
                pos = new_pos
            else:
                moving = False
                block = block_set(pos)
                rocks.update(block)
                height = max(height, max(p.imag for p in block))
        

if __name__ == '__main__':
    with open('2022/input_files/AoC2022_day17_input.txt') as f:
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
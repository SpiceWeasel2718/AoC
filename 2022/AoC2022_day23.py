def part1(input_text: str):
    from collections import deque, Counter
    
    elves = {}
    
    for a, line in enumerate(input_text.splitlines()):
        for b, c in enumerate(line):
            if c == '#':
                elf = b - a*1j
                elves[elf] = elf
    
    cardinals = deque([0, 4, 6, 2])
    nbrs = [1j, 1+1j, 1, 1-1j, -1j, -1-1j, -1, -1+1j]
    
    for __ in range(10):
        proposals = Counter()

        for elf in elves:
            current_nbrs = [elf + d for d in nbrs]
            
            if any(nbrs_present := [(nbr in elves) for nbr in current_nbrs]):
                n, ne, e, se, s, sw, w, nw = nbrs_present
                nbrs_in_card = {0: [n, nw, ne],
                                4: [s, sw, se],
                                6: [w, nw, sw],
                                2: [e, ne, se],}
            
                for card in cardinals:
                    if not any(nbrs_in_card[card]):
                        prop = current_nbrs[card]
                        elves[elf] = prop
                        proposals[prop] += 1
                        break
        
        new_elves = {}
        
        for elf, prop in elves.items():
            if proposals[prop] <= 1:
                new_elves[prop] = prop
            else:
                new_elves[elf] = elf
        
        elves = new_elves
        cardinals.rotate(-1)
        
    x_min = min(elf.real for elf in elves)
    x_max = max(elf.real for elf in elves)
    y_min = min(elf.imag for elf in elves)
    y_max = max(elf.imag for elf in elves)
    
    return int((x_max - x_min + 1) * (y_max - y_min + 1) - len(elves))


def part2(input_text: str):
    from collections import deque, Counter
    
    elves = {}
    
    for a, line in enumerate(input_text.splitlines()):
        for b, c in enumerate(line):
            if c == '#':
                elf = b - a*1j
                elves[elf] = elf
    
    cardinals = deque([0, 4, 6, 2])
    nbrs = [1j, 1+1j, 1, 1-1j, -1j, -1-1j, -1, -1+1j]
    moved = True
    count = 0
    
    while moved:
        moved = False
        count += 1
        proposals = Counter()

        for elf in elves:
            current_nbrs = [elf + d for d in nbrs]
            
            if any(nbrs_present := [(nbr in elves) for nbr in current_nbrs]):
                n, ne, e, se, s, sw, w, nw = nbrs_present
                nbrs_in_card = {0: [n, nw, ne],
                                4: [s, sw, se],
                                6: [w, nw, sw],
                                2: [e, ne, se],}
            
                for card in cardinals:
                    if not any(nbrs_in_card[card]):
                        prop = current_nbrs[card]
                        elves[elf] = prop
                        proposals[prop] += 1
                        break
        
        new_elves = {}
        
        for elf, prop in elves.items():
            if elf != prop and proposals[prop] <= 1:
                moved = True
                new_elves[prop] = prop
            else:
                new_elves[elf] = elf
        
        elves = new_elves
        cardinals.rotate(-1)
        
    return count


if __name__ == '__main__':
    with open('2022/input_files/AoC2022_day23_input.txt') as f:
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
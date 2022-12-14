def part1(input_text: str):
    blocked = set()

    for line in input_text.splitlines():
        turns_text = line.split(' -> ')
        turns = []
        for turn_text in turns_text:
            turns.append(complex(*[int(s) for s in turn_text.split(',')]))
        
        for start, end in zip(turns, turns[1:]):
            blocked.add(start)
            
            current = start
            direction = end - start
            direction /= abs(direction)
            
            while current != end:
                current += direction
                blocked.add(current)
    
    bottom = max(z.imag for z in blocked)
        
    sand = 500
    at_rest = 0
    
    while sand.imag < bottom:
        for pos in [sand+1j, sand-1+1j, sand+1+1j]:
            if pos not in blocked:
                sand = pos
                break
        else:
            blocked.add(sand)
            at_rest += 1
            sand = 500
    
    return at_rest
    

def part2(input_text: str):
    blocked = set()

    for line in input_text.splitlines():
        turns_text = line.split(' -> ')
        turns = []
        for turn_text in turns_text:
            turns.append(complex(*[int(s) for s in turn_text.split(',')]))
        
        for start, end in zip(turns, turns[1:]):
            blocked.add(start)
            
            current = start
            direction = end - start
            direction /= abs(direction)
            
            while current != end:
                current += direction
                blocked.add(current)
    
    bottom = max(z.imag for z in blocked) + 1
        
    sand = 500
    at_rest = 0
    
    while 500 not in blocked:
        if sand.imag == bottom:
            blocked.add(sand)
            at_rest += 1
            sand = 500
            continue
            
        for pos in [sand+1j, sand-1+1j, sand+1+1j]:
            if pos not in blocked:
                sand = pos
                break
        else:
            blocked.add(sand)
            at_rest += 1
            sand = 500
            
    return at_rest


if __name__ == '__main__':
    with open('2022/input_files/AoC2022_day14_input.txt') as f:
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
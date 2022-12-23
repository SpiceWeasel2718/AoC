def part1(input_text: str):
    from collections import deque, Counter
    
    elves = {}
    
    for a, line in enumerate(input_text.splitlines()):
        for b, c in enumerate(line):
            if c == '#':
                elves[b - a*1j] = 0
    
    directions = deque([[-1+1j, 1j, 1+1j],
                        [-1-1j, -1j, 1-1j],
                        [-1+1j, -1, -1-1j],
                        [1+1j, 1, 1-1j]])

    nbrs = [1j, 1+1j, 1, 1-1j, -1j, -1-1j, -1, -1+1j]
    
    for __ in range(10):
        proposals = Counter()

        for elf in elves:
            if any(elf + d in elves for d in nbrs):
                for direction in directions:
                    if all(elf + d not in elves for d in direction):
                        d = direction[1]
                        elves[elf] = elf + d
                        proposals[elf + d] += 1
                        break
                else:
                    elves[elf] = elf
            else:
                elves[elf] = elf
        
        new_elves = {}
        
        for elf, prop in elves.items():
            if proposals[prop] <= 1:
                new_elves[prop] = 0
            else:
                new_elves[elf] = 0
        
        elves = new_elves
        directions.rotate(-1)
        
    x_min = min(elf.real for elf in elves)
    x_max = max(elf.real for elf in elves)
    y_min = min(elf.imag for elf in elves)
    y_max = max(elf.imag for elf in elves)
    
    return int((x_max - x_min + 1) * (y_max - y_min + 1) - len(elves))


def part2(input_text: str):
    from collections import deque, defaultdict
    
    elves = {}
    
    for a, line in enumerate(input_text.splitlines()):
        for b, c in enumerate(line):
            if c == '#':
                elves[b - a*1j] = 0
    
    directions = deque([[-1+1j, 1j, 1+1j],
                        [-1-1j, -1j, 1-1j],
                        [-1+1j, -1, -1-1j],
                        [1+1j, 1, 1-1j]])

    nbrs = [1j, 1+1j, 1, 1-1j, -1j, -1-1j, -1, -1+1j]
    
    moved = True
    count = 0
    
    while moved:
        moved = False
        count += 1
        proposals = defaultdict(int)

        for elf in elves:
            if any(elf + d in elves for d in nbrs):
                for direction in directions:
                    if all(elf + d not in elves for d in direction):
                        d = direction[1]
                        elves[elf] = elf + d
                        proposals[elf + d] += 1
                        break
                else:
                    elves[elf] = elf
            else:
                elves[elf] = elf
        
        new_elves = {}
        
        for elf, prop in elves.items():
            if elf != prop and proposals[prop] <= 1:
                new_elves[prop] = 0
                moved = True
            else:
                new_elves[elf] = 0
        
        elves = new_elves
        directions.rotate(-1)
    
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
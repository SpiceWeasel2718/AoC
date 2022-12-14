def part1(input_text: str):
    directions = {
        'R': 1,
        'L': -1,
        'U': 1j,
        'D': -1j,
        }
    
    head = 0
    tail = 0
    memory = set()
    memory.add(0)
    
    for line in input_text.splitlines():
        d, n_steps = line.split()
        direction = directions[d]
        
        for __ in range(int(n_steps)):
            head += direction
            diff = head - tail
            real_dist, imag_dist = abs(diff.real), abs(diff.imag)
            
            if real_dist > 1:
                tail += diff.real / real_dist + diff.imag * 1j
            elif imag_dist > 1:
                tail += diff.real + diff.imag / imag_dist * 1j
            
            memory.add(tail)
    
    return len(memory)


def part2(input_text: str):
    directions = {
        'R': 1,
        'L': -1,
        'U': 1j,
        'D': -1j,
        }
    
    rope = [0] * 10
    memory = set()
    memory.add(0)
    
    for line in input_text.splitlines():
        d, n_steps = line.split()
        direction = directions[d]
        
        for __ in range(int(n_steps)):
            rope[0] += direction
            
            for i in range(1, 10):
                diff = rope[i-1] - rope[i]
                real_dist, imag_dist = abs(diff.real), abs(diff.imag)
                
                if real_dist > 1 or imag_dist > 1:
                    rope[i] += diff.real / real_dist if real_dist else 0
                    rope[i] += diff.imag / imag_dist * 1j if imag_dist else 0
                else:
                    break
            
            memory.add(rope[9])
    
    return len(memory)


if __name__ == '__main__':
    with open('2022/input_files/AoC2022_day09_input.txt') as f:
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
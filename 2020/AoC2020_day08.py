def part1(input_text):
    instructions = [[line[:3], int(line[4:])] for line in input_text.splitlines()]
    
    accumulator = 0
    pos = 0
    seen = set()

    while pos not in seen:
        seen.add(pos)
        
        comm, arg = instructions[pos]
        
        if comm == 'acc':
            accumulator += arg
            pos += 1
        elif comm == 'jmp':
            pos += arg
        else:
            pos += 1

    return accumulator
        

def part2(input_text):
    instructions = [[line[:3], int(line[4:])] for line in input_text.splitlines()]
    
    target = len(instructions)
    
    for inst in instructions:
        if (old_comm := inst[0]) == 'acc':
            continue
        
        inst[0] = 'jmp' if old_comm == 'nop' else 'nop'

        accumulator = 0
        pos = 0
        seen = set()

        while pos not in seen:
            seen.add(pos)
            
            comm, arg = instructions[pos]

            if comm == 'acc':
                accumulator += arg
                pos += 1
            elif comm == 'jmp':
                pos += arg
            else:
                pos += 1
        
            if pos == target:
                return accumulator
        
        inst[0] = old_comm


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day08_input.txt') as f:
        input_text = f.read()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    time_execution = 1

    if time_execution:
        import timeit
        for part in ['part1', 'part2']:
            timer = timeit.Timer(f'{part}(input_text)', globals=globals())
            n, time = timer.autorange()
            print(f'{part} took {time/n:.5f} seconds on average when run {n} times')
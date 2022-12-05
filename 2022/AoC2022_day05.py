def part1(input_text):
    input_lines = input_text.splitlines()

    for i in range(100):
        if input_lines[i].startswith('move'):
            break
    
    stack_lines = input_lines[:i-2]
    instruction_lines = input_lines[i:]
    n_stacks = len(stack_lines[-1]) // 4 + 1

    stacks = {n: [] for n in range(1, n_stacks+1)}

    for line in stack_lines[::-1]:
        for i, c in enumerate(line[1::4]):
            if c != ' ':
                stacks[i+1].append(c)
    
    for line in instruction_lines:
        words = line.split()
        
        n_moving = int(words[1])
        from_stack = int(words[3])
        to_stack = int(words[5])

        for __ in range(n_moving):
            stacks[to_stack].append(stacks[from_stack].pop())
    
    return ''.join(stacks[i+1][-1] for i in range(n_stacks))


def part2(input_text):
    input_lines = input_text.splitlines()

    for i in range(100):
        if input_lines[i].startswith('move'):
            break
    
    stack_lines = input_lines[:i-2]
    instruction_lines = input_lines[i:]
    n_stacks = len(stack_lines[-1]) // 4 + 1

    stacks = {n: [] for n in range(1, n_stacks+1)}

    for line in stack_lines[::-1]:
        for i, c in enumerate(line[1::4]):
            if c != ' ':
                stacks[i+1].append(c)
    
    for line in instruction_lines:
        words = line.split()
        
        n_moving = int(words[1])
        from_stack = int(words[3])
        to_stack = int(words[5])

        stacks[to_stack] += stacks[from_stack][-n_moving:]
        stacks[from_stack] = stacks[from_stack][:-n_moving]
    
    return ''.join(stacks[i+1][-1] for i in range(n_stacks))


if __name__ == '__main__':
    with open('./input_files/AoC2022_day05_input.txt') as f:
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
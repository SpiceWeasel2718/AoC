def part1(input_text: str):
    from collections import defaultdict
    
    init, *state_chunks = input_text.split('\n\n')

    l1, l2 = init.split('\n', 1)
    __, temp = l1.rsplit(maxsplit=1)
    current_state = temp[0]
    __, temp, __ = l2.rsplit(maxsplit=2)
    checksum_step = int(temp)

    states = {}

    for chunk in state_chunks:
        lines = chunk.splitlines()
        state = lines[0][-2]
        instructions = []
        
        for i in [2, 6]:
            instructions.append((
                int(lines[i][-2]), 
                1 if lines[i+1].endswith('right.') else -1,
                lines[i+2][-2]
                ))
        
        states[state] = instructions
    
    tape = defaultdict(int)
    cursor = 0

    for __ in range(checksum_step):
        write_value, cursor_shift, new_state = states[current_state][tape[cursor]]
        tape[cursor] = write_value
        cursor += cursor_shift
        current_state = new_state
    
    return sum(tape.values())

if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2017_day25_input.txt') as f:
        input_text = f.read()
    
    print('part 1:', part1(input_text))

    time_execution = 0

    if time_execution:
        import timeit
        for part in ['part1']:
            timer = timeit.Timer(f'{part}(input_text)', globals=globals())
            n, time = timer.autorange()
            print(f'{part} took {time/n:.5f} seconds on average when run {n} times')
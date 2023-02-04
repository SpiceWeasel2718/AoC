class Processor:
    def __init__(self, instructions):
        self.program = []
        self.registers = {}

        for line in instructions:
            instruction = line.split()
            self.program.append(instruction)

            for arg in instruction[1:]:
                try:
                    self.registers[arg] = int(arg)
                except ValueError:
                    self.registers[arg] = 0
        
        self.program_size = len(self.program)
        self.pos = 0
    

    def execute(self, a=0):
        program = self.program.copy()
        registers = self.registers.copy()
        registers['a'] = a
        program_size = self.program_size
        pos = self.pos

        count = 0

        while 0 <= pos < program_size:
            instruction, *args = program[pos]

            if instruction == 'set':
                registers[args[0]] = registers[args[1]]
            elif instruction == 'sub':
                registers[args[0]] -= registers[args[1]]
            elif instruction == 'mul':
                count += 1
                registers[args[0]] *= registers[args[1]]
            elif instruction == 'jnz':
                if registers[args[0]] != 0:
                    pos += registers[args[1]]
                    continue
            else:
                raise Exception(f'Error: unknown instruction {instruction}, {args}')
            
            pos += 1
        
        if a:
            return registers['h']
        
        return count
    

def part1(input_text: str):
    proc = Processor(input_text)
    return proc.execute()


def part2(input_text: str):
    # By inspection, the value of h on exit is the number of non-prime values 
    # b takes between its start and end (inclusive)
    from math import sqrt, ceil

    start = 109900
    end = 126900
    inc = 17
    h = 0

    for b in range(start, end+1, inc):
        for n in range(2, ceil(sqrt(b))):
            if b % n == 0:
                h += 1
                break
    
    return h


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2017_day23_input.txt') as f:
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
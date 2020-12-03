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
    

def part1(input_text):
    proc = Processor(input_text)
    return proc.execute()


def part2(input_text):
    
    
    
    
    # proc = Processor(input_text)
    # return proc.execute(a=1)


if __name__ == '__main__':
    from pathlib import Path
    with open(next(Path().glob('**/AoC2017_day23_input.txt'))) as f:
        input_text = f.read().splitlines()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    #print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    #print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
class Solution:
    def __init__(self):
        with open("input_files/AoC2017_day08_input.txt") as f:
            self.input_text = f.read().split('\n')

    def part1(self):
        registers = {}
        coeff = {'inc': 1, 'dec': -1}

        for instruction in [line.split(' ') for line in self.input_text]:
            registers.setdefault(instruction[0], 0)
            registers.setdefault(instruction[4], 0)
            
            if eval(str(registers[instruction[4]]) + ' '.join(instruction[5:])):
                registers[instruction[0]] += coeff[instruction[1]] * int(instruction[2])
        
        print(max(registers[k] for k in registers))

        
    def part2(self):
        registers = {}
        coeff = {'inc': 1, 'dec': -1}
        m = 0

        for instruction in [line.split(' ') for line in self.input_text]:
            registers.setdefault(instruction[0], 0)
            registers.setdefault(instruction[4], 0)
            
            if eval(str(registers[instruction[4]]) + ' '.join(instruction[5:])):
                registers[instruction[0]] += coeff[instruction[1]] * int(instruction[2])
                m = max(m, registers[instruction[0]])
        
        print(m)


Solution().part2()
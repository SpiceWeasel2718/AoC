class Solution:
    def __init__(self):
        with open("input_files/AoC2017_day05_input.txt") as f:
            self.input_text = [int(n) for n in f.read().split('\n')]

    def part1(self):
        pos = 0
        steps = 0

        while pos < len(self.input_text):
            next_pos = pos + self.input_text[pos]
            self.input_text[pos] += 1
            pos = next_pos
            steps += 1

            print(f'\rstep {steps}', end='')
        
    def part2(self):
        pos = 0
        steps = 0

        while pos < len(self.input_text):
            next_pos = pos + self.input_text[pos]
            self.input_text[pos] += -1 if self.input_text[pos] >= 3 else 1
            pos = next_pos
            steps += 1

            print(f'\rstep {steps}', end='')


Solution().part2()
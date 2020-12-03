class Solution:
    def __init__(self):
        with open("input_files/AoC2017_day06_input.txt") as f:
            self.input_text = [int(n) for n in f.read().split('\t')]

    def part1(self):
        seen = set(tuple(self.input_text))
        cycles = 0

        while True:
            cycles += 1

            m = max(self.input_text)
            pos = self.input_text.index(m)
            self.input_text[pos] = 0

            for i in range(pos+1, pos+m+1):
                self.input_text[i % 16] += 1
            
            state = tuple(self.input_text)

            if state in seen:
                break
            else:
                seen.add(state)
        
        print(cycles)

        
    def part2(self):
        seen = {tuple(self.input_text): 0}
        cycles = 0

        while True:
            cycles += 1

            m = max(self.input_text)
            pos = self.input_text.index(m)
            self.input_text[pos] = 0

            for i in range(pos+1, pos+m+1):
                self.input_text[i % 16] += 1
            
            state = tuple(self.input_text)

            if state in seen:
                print(cycles - seen[state])
                break
            else:
                seen.update({state: cycles})
        

Solution().part2()
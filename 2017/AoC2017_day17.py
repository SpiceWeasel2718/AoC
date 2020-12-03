class Solution:
    def __init__(self):
        self.input_text = 316

    def part1(self):
        step = self.input_text
        buffer = [0]
        pos = 0

        for i in range(1, 2018):
            pos = ((pos + step) % len(buffer)) + 1
            buffer.insert(pos, i)
        
        print(buffer[(pos+1) % len(buffer)])
        
    def part2(self):
        step = self.input_text
        val = 0
        pos = 0

        for i in range(1, 50000000):
            pos = ((pos + step) % i) + 1
            if pos == 1:
                val = i
        
        print(val)
            

Solution().part2()
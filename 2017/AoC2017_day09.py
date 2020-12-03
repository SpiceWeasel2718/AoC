class Solution:
    def __init__(self):
        with open("input_files/AoC2017_day09_input.txt") as f:
            self.input_text = f.read()

    def part1(self):
        score = 0
        scope = 0
        skip = False
        garbage = False

        for c in self.input_text:
            if skip:
                skip = False
                continue
            
            if not garbage:
                if c == '{':
                    scope += 1
                elif c == '}':
                    score += scope
                    scope -= 1
                elif c == '<':
                    garbage = True
            else:
                if c == '>':
                    garbage = False
                elif c== '!':
                    skip = True
        
        print(score)

        
    def part2(self):
        score = 0
        skip = False
        garbage = False

        for c in self.input_text:
            if skip:
                skip = False
                continue
            
            if not garbage:
                if c == '<':
                    garbage = True
            else:
                if c == '>':
                    garbage = False
                elif c== '!':
                    skip = True
                else:
                    score += 1
        
        print(score)


Solution().part2()
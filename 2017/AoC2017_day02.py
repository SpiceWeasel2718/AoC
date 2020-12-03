class Solution:
    def __init__(self):
        with open("input_files/AoC2017_day02_input.txt") as f:
            self.input_text = f.read().split('\n')

    def part1(self):
        spreadsheet = [[int(n) for n in line.split('\t')] for line in self.input_text]

        total = 0

        for row in spreadsheet:
            total += max(row) - min(row)
        
        print(total)


    def part2(self):
        from itertools import permutations
        
        spreadsheet = [[int(n) for n in line.split('\t')] for line in self.input_text]

        total = 0

        for row in spreadsheet:
            for pair in permutations(row, 2):
                if pair[0] % pair[1] == 0:
                    total += pair[0] // pair[1]
                    break
        
        print(total)


Solution().part1()


    
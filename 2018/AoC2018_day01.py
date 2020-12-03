class Solution:
    def __init__(self):
        with open("input_files/AoC2018_day01_input.txt") as f:
            self.input_text = f.read().split('\n')

    def part1(self):
        print(sum(int(line) for line in self.input_text))


    def part2(self):
        changes = tuple(int(line) for line in self.input_text)
        seen = set()
        total = 0

        while total not in seen:
            for change in changes:
                seen.add(total)
                total += change
                if total in seen:
                    break
        
        print(total)

Solution().part2()
class Solution:
    def __init__(self):
        with open("input_files/AoC2017_day01_input.txt") as f:
            self.input_text = f.read()

    def part1(self):
        total = 0

        for i, c in enumerate(self.input_text[:-1]):
            if c == self.input_text[i+1]:
                total += int(c)

        if self.input_text[-1] == self.input_text[0]:
            total += int(self.input_text[-1])

        print(total)


    def part2(self):
        l = len(self.input_text)
        l2 = l//2
        total = 0

        for i, c in enumerate(self.input_text):
            if c == self.input_text[(i+l2) % l]:
                total += int(c)

        print(total)


Solution().part1()
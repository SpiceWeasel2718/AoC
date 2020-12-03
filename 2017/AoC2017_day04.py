class Solution:
    def __init__(self):
        with open("input_files/AoC2017_day04_input.txt") as f:
            self.input_text = f.read().split('\n')

    def part1(self):
        count = 0

        for words in [line.split(' ') for line in self.input_text]:
            if len(set(words)) == len(words):
                count += 1
        
        print(count)

    def part2(self):
        from collections import Counter
        count = 0

        for words in [line.split(' ') for line in self.input_text]:
            if not len(set(words)) == len(words):
                continue
            
            words_set = set()

            for word in words:
                temp = ''.join(sorted(word))
                if temp in words_set:
                    break
                words_set.add(temp)
            else:
                count += 1
            
        print(count)


Solution().part2()
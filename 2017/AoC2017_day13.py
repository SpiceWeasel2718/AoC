class Solution:
    def __init__(self):
        with open("input_files/AoC2017_day13_input.txt") as f:
            self.input_text = f.read().split('\n')

    def part1(self):
        firewall = {}

        for line in (l.split(': ') for l in self.input_text):
            firewall.update({int(line[0]): int(line[1])})

        severity = 0

        for layer in range(93):
            if layer in firewall and layer % (2*firewall[layer]-2) == 0:
                severity += layer * firewall[layer]

        print(severity)
        

    def part2(self):
        firewall = {}

        for line in (l.split(': ') for l in self.input_text):
            firewall.update({int(line[0]): 2*int(line[1])-2})

        delay = 0

        while True:
            for layer in firewall:
                if not (layer + delay) % firewall[layer]:
                    break
            else:
                break

            delay += 1
        
        print(delay)
        

Solution().part2()
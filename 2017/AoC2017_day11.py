class Solution:
    def __init__(self):
        with open("input_files/AoC2017_day11_input.txt") as f:
            self.input_text = f.read()

    def part1(self):
        directions = { # represent tiles by points on the plane
            'n': (0,2),
            'ne': (1,1),
            'se': (1,-1),
            's': (0,-2),
            'sw': (-1,-1),
            'nw': (-1,1)
        }
        
        def ptwise_sum(v1, v2):
            return (v1[0] + v2[0], v1[1] + v2[1])

        pos = (0, 0)

        for step in self.input_text.split(','):
            pos = ptwise_sum(pos, directions[step])
        
        print(abs(pos[0]) + abs(abs(pos[1]) - abs(pos[0])) // 2)
        

    def part2(self):
        directions = {
            'n': (0,2),
            'ne': (1,1),
            'se': (1,-1),
            's': (0,-2),
            'sw': (-1,-1),
            'nw': (-1,1)
        }
        
        def ptwise_sum(v1, v2):
            return (v1[0] + v2[0], v1[1] + v2[1])

        def dist(v):
            return abs(pos[0]) + abs(abs(pos[1]) - abs(pos[0])) // 2

        pos = (0, 0)
        m = 0

        for step in self.input_text.split(','):
            pos = ptwise_sum(pos, directions[step])
            m = max(m, dist(pos))

        print(m)
        

Solution().part2()
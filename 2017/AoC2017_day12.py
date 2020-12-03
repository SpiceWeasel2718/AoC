class Solution:
    def __init__(self):
        with open("input_files/AoC2017_day12_input.txt") as f:
            self.input_text = f.read().split('\n')

    def part1(self):
        graph = {}

        for line in [l.split(' <-> ') for l in self.input_text]:
            graph.update({line[0]: line[1].split(', ')})
        
        seen = set()

        def explore(node):
            seen.add(node)

            for neighbor in graph[node]:
                if not neighbor in seen:
                    explore(neighbor)
        
        explore('0')

        print(len(seen))
        

    def part2(self):
        graph = {}

        for line in [l.split(' <-> ') for l in self.input_text]:
            graph.update({line[0]: line[1].split(', ')})
        
        unseen = set(graph)

        def explore(node):
            unseen.discard(node)

            for neighbor in graph[node]:
                if neighbor in unseen:
                    explore(neighbor)
        
        groups = 0

        while len(unseen) > 0:
            explore(unseen.pop())
            groups += 1

        print(groups)
        

Solution().part2()
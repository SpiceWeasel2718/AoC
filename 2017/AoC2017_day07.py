class Solution:
    def __init__(self):
        with open("input_files/AoC2017_day07_input.txt") as f:
            self.input_text = f.read().split('\n')

    def part1(self):
        parents = set()
        children = set()

        for line in [l.split(' ') for l in self.input_text]:
            if '->' in line:
                parents.add(line[0])
                children.update({child.strip(',') for child in line[3:]})
            else:
                children.add(line[0])
        
        print(parents.difference(children))

        
    def part2(self):
        weights = {}
        tree = {}

        for line in [l.split(' ') for l in self.input_text]:
            weights.update({line[0]: int(line[1].strip('()'))})

            if '->' in line:
                tree.update({line[0]: tuple(child.strip(',') for child in line[3:])})
        
        def sum_subtree(head):
            if not head in tree:
                return weights[head]
            else:
                return weights[head] + sum(sum_subtree(child) for child in tree[head])
        
        def problem_child(parent):
            towers = {}
            
            for child in tree[parent]:
                s = sum_subtree(child)
                towers.setdefault(s, set())
                towers[s].add(child)
            
            if len(towers) == 1:
                return ''
            
            if len(tree[parent]) > 2:
                for weight in towers:
                    if len(towers[weight]) == 1:
                        return towers[weight].pop()
            else:
                for child in tree[parent]:
                    problem = problem_child(child)
                    if problem:
                        return child
                        
        parent = 'vmpywg'
        child = problem_child(parent)

        while True:
            problem = problem_child(child)
            if problem:
                parent, child = child, problem
            else:
                print({child: sum_subtree(child) for child in tree[parent]})
                print(weights[child])
                break


Solution().part2()
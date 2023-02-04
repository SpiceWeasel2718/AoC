from copy import deepcopy


def part1(input_text):
    from math import prod
    from collections import deque
    from copy import deepcopy

    class Node:
        def __init__(self) -> None:
            self.multipliers = deque()
            self.value = -1
            self.l = None
            self.r = None
        
        def __iter__(self):
            cur = self
            while cur:
                yield cur
                cur = cur.r
        
        def __repr__(self) -> str:
            out = []
            for n in self:
                out.append(f'{n.value} ({len(n.multipliers)})')
            return '  '.join(out)
        
        def join_l(self, new_l):
            self.l = new_l
            if new_l:
                new_l.r = self

        def join_r(self, new_r):
            self.r = new_r
            if new_r:
                new_r.l = self
        
        def explode(self):
            self.multipliers.pop()

            if self.l:
                self.l.value += self.value
            
            self.value = 0

            old_r = self.r

            if old_r.r:
                old_r.r.value += old_r.value
                self.join_r(old_r.r)
            else:
                self.r = None
            
            del old_r
        
        def split(self):
            v = self.value
            w = v // 2

            new_r = Node()
            
            new_r.multipliers = self.multipliers.copy()
            self.multipliers.append(3)
            new_r.multipliers.append(2)
            
            self.value = w
            new_r.value = v - w

            new_r.join_r(self.r)
            new_r.join_l(self)

            self.r = new_r

    
    def parse_line(line):
        multipliers = deque()
        prev = None
        root = None

        for c in line:
            match c:
                case '[':
                    multipliers.append(3)
                case ',':
                    multipliers[-1] = 2
                case ']':
                    multipliers.pop()
                case _:
                    new_node = Node()
                    new_node.multipliers = multipliers.copy()
                    new_node.value = int(c)
                    new_node.l = prev
                    if prev:
                        prev.r = new_node
                    prev = new_node
                    if not root:
                        root = new_node
        
        return root

    
    def add_lists(root1, root2):
        for n in root1:
            n.multipliers.appendleft(3)

        root2.join_l(n)
        
        for n in root2:
            n.multipliers.appendleft(2)
        
        return root1

    
    def reduce(root):
        for n in root:
            if len(n.multipliers) > 4:
                n.explode()
        
        n = root

        while n:
            if n.value > 9:
                n.split()
                if len(n.multipliers) > 4:
                    n.explode()
                n = root
            else:
                n = n.r

        return root
    

    def magnitude(root):
        total = 0
        cur = root

        while cur:
            total += prod(cur.multipliers) * cur.value
            cur = cur.r
        
        return total

    
    summands = []

    for line in input_text.splitlines():
        summands.append(parse_line(line))

    total = summands[0]

    for s in summands[1:]:
        total = reduce(add_lists(total, s))

    return magnitude(total)


def part2(input_text):
    from math import prod
    from collections import deque

    class Node:
        def __init__(self) -> None:
            self.multipliers = deque()
            self.value = -1
            self.l = None
            self.r = None
        
        def __iter__(self):
            cur = self
            while cur:
                yield cur
                cur = cur.r
        
        def __repr__(self) -> str:
            out = []
            for n in self:
                out.append(f'{n.value} ({len(n.multipliers)})')
            return '  '.join(out)
        
        def join_l(self, new_l):
            self.l = new_l
            if new_l:
                new_l.r = self

        def join_r(self, new_r):
            self.r = new_r
            if new_r:
                new_r.l = self
        
        def explode(self):
            self.multipliers.pop()

            if self.l:
                self.l.value += self.value
            
            self.value = 0

            old_r = self.r

            if old_r.r:
                old_r.r.value += old_r.value
                self.join_r(old_r.r)
            else:
                self.r = None
            
            del old_r
        
        def split(self):
            v = self.value
            w = v // 2

            new_r = Node()
            
            new_r.multipliers = self.multipliers.copy()
            self.multipliers.append(3)
            new_r.multipliers.append(2)
            
            self.value = w
            new_r.value = v - w

            new_r.join_r(self.r)
            new_r.join_l(self)

            self.r = new_r

    
    def parse_line(line):
        multipliers = deque()
        prev = None
        root = None

        for c in line:
            match c:
                case '[':
                    multipliers.append(3)
                case ',':
                    multipliers[-1] = 2
                case ']':
                    multipliers.pop()
                case _:
                    new_node = Node()
                    new_node.multipliers = multipliers.copy()
                    new_node.value = int(c)
                    new_node.l = prev
                    if prev:
                        prev.r = new_node
                    prev = new_node
                    if not root:
                        root = new_node
        
        return root

    
    def add_lists(root1, root2):
        result = deepcopy(root1)
        r2 = deepcopy(root2)

        for n in result:
            n.multipliers.appendleft(3)

        r2.join_l(n)
        
        for n in r2:
            n.multipliers.appendleft(2)
        
        return result

    
    def reduce(root):
        for n in root:
            if len(n.multipliers) > 4:
                n.explode()
        
        n = root

        while n:
            if n.value > 9:
                n.split()
                if len(n.multipliers) > 4:
                    n.explode()
                n = root
            else:
                n = n.r

        return root
    

    def magnitude(root):
        total = 0

        for n in root:
            total += prod(n.multipliers) * n.value
        
        return total

    
    summands = []

    for line in input_text.splitlines():
        summands.append(parse_line(line))

    max_mag = 0

    for i, s in enumerate(summands):
        for j, t in enumerate(summands):
            if i != j:
                max_mag = max(magnitude(reduce(add_lists(s, t))), max_mag)
            
    return max_mag


if __name__ == '__main__':
    with open('./input_files/AoC2021_day18_input.txt') as f:
        input_text = f.read()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    time_execution = 0

    if time_execution:
        import timeit
        for part in ['part1', 'part2']:
            timer = timeit.Timer(f'{part}(input_text)', globals=globals())
            n, time = timer.autorange()
            print(f'{part} took {time/n:.5f} seconds on average when run {n} times')
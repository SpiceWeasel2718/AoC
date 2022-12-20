def part1(input_text: str):
    
    class Node:
        def __init__(self, value, parent, child=None):
            self.value = value
            self.parent = parent
            self.child = child
        
        def mix(self):
            if self.value == 0:
                return
            
            if self.value < 0:
                for __ in range(-self.value):
                    old_parent = self.parent
                    old_child = self.child
                    
                    self.parent = self.parent.parent
                    self.child = self.parent.child
                    
                    self.child.parent = self
                    self.parent.child = self
                    
                    old_parent.child = old_child
                    old_child.parent = old_parent
                
                
            elif self.value > 0:
                for __ in range(self.value):
                    old_parent = self.parent
                    old_child = self.child
                    
                    self.child = self.child.child
                    self.parent = self.child.parent
                
                    self.child.parent = self
                    self.parent.child = self
                    
                    old_parent.child = old_child
                    old_child.parent = old_parent
            
    nodes = []
    prev = None
    
    for line in input_text.splitlines():
        value = int(line)
        node = Node(value, prev)
        
        if value == 0:
            zero = node
        
        if prev is not None:
            prev.child = node
        
        prev = node
        nodes.append(node)

    nodes[0].parent = nodes[-1]
    nodes[-1].child = nodes[0]
    
    for node in nodes:
        node.mix()
    
    current = zero
    total = 0
    
    for __ in range(3):
        for ___ in range(1000):
            current = current.child
        total += current.value
        
    return total


def part2(input_text: str):

    class Node:
        node_mod = 0
        
        def __init__(self, value, parent, child=None):
            self.value = value
            self.parent = parent
            self.child = child
        
        def mix(self):
            if self.value == 0:
                return
            
            if self.value < 0:
                for __ in range((-self.value) % self.node_mod):
                    old_parent = self.parent
                    old_child = self.child
                    
                    self.parent = self.parent.parent
                    self.child = self.parent.child
                    
                    self.child.parent = self
                    self.parent.child = self
                    
                    old_parent.child = old_child
                    old_child.parent = old_parent
                
                
            elif self.value > 0:
                for __ in range(self.value % self.node_mod):
                    old_parent = self.parent
                    old_child = self.child
                    
                    self.child = self.child.child
                    self.parent = self.child.parent
                
                    self.child.parent = self
                    self.parent.child = self
                    
                    old_parent.child = old_child
                    old_child.parent = old_parent
            
    nodes = []
    prev = None
    
    for line in input_text.splitlines():
        value = int(line) * 811589153
        node = Node(value, prev)
        
        if value == 0:
            zero = node
        
        if prev is not None:
            prev.child = node
        
        prev = node
        nodes.append(node)
    
    Node.node_mod = len(nodes) - 1

    nodes[0].parent = nodes[-1]
    nodes[-1].child = nodes[0]
    
    for __ in range(10):
        for node in nodes:
            node.mix()
    
    current = zero
    total = 0
    
    for __ in range(3):
        for ___ in range(1000):
            current = current.child
        total += current.value
        
    return total


if __name__ == '__main__':
    with open('2022/input_files/AoC2022_day20_input.txt') as f:
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
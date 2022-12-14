def part1(input_text: str):
    class Dir:
        def __init__(self, parent = None):
            self.parent = parent
            self.children = {}
            self.files = {}
            self.size = None

        def get_size(self):
            if self.size is None:
                self.size = (
                    sum(self.files.values())
                    + sum(c.get_size() for c in self.children.values())
                    )
            return self.size

    head = Dir()
    head.children['/'] = Dir()
    cur_dir = head

    for line in input_text.splitlines():
        if line.startswith('$ cd'):
            new_dir_name = line[5:]

            if new_dir_name == '..':
                cur_dir = cur_dir.parent
            else:
                cur_dir = cur_dir.children[new_dir_name]

        elif line.startswith('dir'):
            __, dir_name = line.split()
            cur_dir.children[dir_name] = Dir(cur_dir)
        
        elif line[0].isnumeric():
            file_size, file_name = line.split()
            cur_dir.files[file_name] = int(file_size)
        
    stack = []
    stack.append(head)
    total = 0
    
    while stack:
        cur_dir = stack.pop()
        
        for child in cur_dir.children.values():
            stack.append(child)
        
        size = cur_dir.get_size()

        if size <= 100000:
            total += size
    
    return total


def part2(input_text: str):
    class Dir:
        def __init__(self, parent = None):
            self.parent = parent
            self.children = {}
            self.files = {}
            self.size = None

        def get_size(self):
            if self.size is None:
                self.size = (
                    sum(self.files.values())
                    + sum(c.get_size() for c in self.children.values())
                    )
            return self.size

    head = Dir()
    head.children['/'] = Dir()
    cur_dir = head

    for line in input_text.splitlines():
        if line.startswith('$ cd'):
            new_dir_name = line[5:]

            if new_dir_name == '..':
                cur_dir = cur_dir.parent
            else:
                cur_dir = cur_dir.children[new_dir_name]

        elif line.startswith('dir'):
            __, dir_name = line.split()
            cur_dir.children[dir_name] = Dir(cur_dir)
        
        elif line[0].isnumeric():
            file_size, file_name = line.split()
            cur_dir.files[file_name] = int(file_size)
        
    stack = []
    stack.append(head)
    lower_bound = head.get_size() - 40000000
    best = 70000000
    
    while stack:
        cur_dir = stack.pop()
        
        size = cur_dir.get_size()

        if lower_bound <= size:
            for child in cur_dir.children.values():
                stack.append(child)
            
            if size < best:
                best = size
    
    return best


if __name__ == '__main__':
    with open('2022/input_files/AoC2022_day07_input.txt') as f:
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
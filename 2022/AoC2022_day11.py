def part1(input_text: str):
    class Monkey:
        def __init__(self, items, op_text, test_val, true_target, false_target) -> None:
            self.items = items
            self.op_text = op_text
            self.test_val = test_val
            self.true_target = true_target
            self.false_target = false_target
            self.n_inspected = 0
        
        def operation(self, old):
            return eval(self.op_text)

        def test(self, val):
            return self.false_target if (val % self.test_val) else self.true_target
    
    
    monkeys = []
    
    for block in input_text.split('\n\n'):
        
        lines = block.splitlines()
        
        __, items_text = lines[1].split(': ')
        items = [int(c) for c in items_text.split(', ')]
        __, operation = lines[2].split('= ')
        __, test_text = lines[3].split('by ')
        __, true_text = lines[4].split('monkey ')
        __, false_text = lines[5].split('monkey ')
        
        monkeys.append(Monkey(items, operation, int(test_text), int(true_text), int(false_text)))


    for __ in range(20):
        for monkey in monkeys:
            monkey.n_inspected += len(monkey.items)
            
            for val in map(monkey.operation, monkey.items):
                val //= 3
                monkeys[monkey.test(val)].items.append(val)
            
            monkey.items = []
   
   
    counts = set([m.n_inspected for m in monkeys])
    m1 = max(counts)
    counts.remove(m1)
    
    return m1 * max(counts)


def part2(input_text: str):
    class Monkey:
        def __init__(self, items, op_text, test_val, true_target, false_target) -> None:
            self.items = items
            self.op_text = op_text
            self.test_val = test_val
            self.true_target = true_target
            self.false_target = false_target
            self.n_inspected = 0
        
        def operation(self, old):
            return eval(self.op_text)

        def test(self, val):
            return self.false_target if (val % self.test_val) else self.true_target
    
    
    monkeys = []
    product = 1
    
    for block in input_text.split('\n\n'):
        
        lines = block.splitlines()
        
        __, items_text = lines[1].split(': ')
        items = [int(c) for c in items_text.split(', ')]
        __, operation = lines[2].split('= ')
        __, test_text = lines[3].split('by ')
        __, true_text = lines[4].split('monkey ')
        __, false_text = lines[5].split('monkey ')
        
        monkeys.append(Monkey(items, operation, int(test_text), int(true_text), int(false_text)))
        product *= int(test_text)


    for __ in range(10000):
        for monkey in monkeys:
            monkey.n_inspected += len(monkey.items)
            
            for val in map(monkey.operation, monkey.items):
                val %= product
                monkeys[monkey.test(val)].items.append(val)
            
            monkey.items = []
   
   
    counts = set([m.n_inspected for m in monkeys])
    m1 = max(counts)
    counts.remove(m1)
    
    return m1 * max(counts)


if __name__ == '__main__':
    with open('2022/input_files/AoC2022_day11_input.txt') as f:
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
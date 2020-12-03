def part1(input_text):
    instructions = []
    registers = {'last_freq': 0, 'pos': 0}

    for line in (l.split() for l in input_text):
        for k in line[1:]:
            if k.isalpha():
                registers.setdefault(k, 0)
            else:
                registers[k] = int(k)
        instructions.append(line)
    
    def rsnd(arg):
        registers['last_freq'] = registers[arg[0]]
    def rset(arg):
        registers[arg[0]] = registers[arg[1]]
    def radd(arg):
        registers[arg[0]] += registers[arg[1]]
    def rmul(arg):
        registers[arg[0]] *= registers[arg[1]]
    def rmod(arg):
        registers[arg[0]] %= registers[arg[1]]
    def rrcv(arg):
        if registers[arg[0]]:
            registers['pos'] = len(instructions)
    def rjgz(arg):
        if registers[arg[0]] > 0:
            registers['pos'] += -1 + registers[arg[1]]
    
    funcs = {
        'snd': rsnd,
        'set': rset,
        'add': radd,
        'mul': rmul,
        'mod': rmod,
        'rcv': rrcv,
        'jgz': rjgz
    }

    while 0 <= registers['pos'] < len(instructions):
        funcs[instructions[registers['pos']][0]](instructions[registers['pos']][1:])
        registers['pos'] += 1
    
    return registers['last_freq']


def part2(input_text):
    import threading
    import concurrent.futures
    from collections import deque

    instructions = []
    blank_registry = {}

    for line in (l.split() for l in input_text):
        for k in line[1:]:
            if k.isalpha():
                blank_registry.setdefault(k, 0)
            else:
                blank_registry[k] = int(k)
        instructions.append(line)
    
    class Registry:
        terminate_event = threading.Event()

        def __init__(self, program_id):
            self.registers = blank_registry.copy()
            self.pos = 0
            self.queue = deque()
            self.queue_event = threading.Event()
            self.queue_event.set()
            self.registers['p'] = program_id
            self.send_count = 0
            self.program_id = program_id
            
            
        def rsnd(self, arg):
            self.send_count += 1
            self.partner_registry.queue.append(self.registers[arg[0]])
            self.partner_registry.queue_event.set()
        def rset(self, arg):
            self.registers[arg[0]] = self.registers[arg[1]]
        def radd(self, arg):
            self.registers[arg[0]] += self.registers[arg[1]]
        def rmul(self, arg):
            self.registers[arg[0]] *= self.registers[arg[1]]
        def rmod(self, arg):
            self.registers[arg[0]] %= self.registers[arg[1]]
        def rrcv(self, arg):
            if len(self.queue) == 0:
                self.queue_event.clear()
                if not self.partner_registry.queue_event.is_set():
                    self.terminate_event.set()
                    self.partner_registry.queue_event.set()
                    return
                self.queue_event.wait()
            self.registers[arg[0]] = self.queue.popleft()
        def rjgz(self, arg):
            if self.registers[arg[0]] > 0:
                self.pos += self.registers[arg[1]] - 1
        
        funcs = {
            'snd': rsnd,
            'set': rset,
            'add': radd,
            'mul': rmul,
            'mod': rmod,
            'rcv': rrcv,
            'jgz': rjgz
        }

        def set_partner_registry(self, partner):
            self.partner_registry = partner
        
        def run(self):
            while 0 <= self.pos < len(instructions) and not self.terminate_event.is_set():
                self.funcs[instructions[self.pos][0]](self, instructions[self.pos][1:])
                self.pos += 1
            
            return self.send_count

    
    reg0 = Registry(0)
    reg1 = Registry(1)

    reg0.set_partner_registry(reg1)
    reg1.set_partner_registry(reg0)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        res0 = executor.submit(reg0.run)
        res1 = executor.submit(reg1.run)
    
    return res1.result()


if __name__ == "__main__":
    import timeit
    
    with open("input_files/AoC2017_day18_input.txt") as f:
        input_text = f.read().split('\n')
    
    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
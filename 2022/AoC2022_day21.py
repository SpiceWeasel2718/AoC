def part1(input_text: str):
    results = {}
    waiting = {}

    for line in input_text.splitlines():
        words = line.split()
        monkey = words[0][:-1]
        
        if len(words) == 2:
            results[monkey] = int(words[1])
        else:
            waiting[monkey] = tuple(words[1:])
        
    operations = {
        '+': lambda x, y : results[x] + results[y],
        '-': lambda x, y : results[x] - results[y],
        '*': lambda x, y : results[x] * results[y],
        '/': lambda x, y : results[x] // results[y],
    }
    
    while 'root' not in results:
        for monkey, expression in waiting.items():
            x, op, y = expression
            if x in results and y in results:
                results[monkey] = operations[op](x, y)
    
    return results['root']


def part2(input_text: str):
    from sympy import symbols, solveset, S
    
    results = {'humn': symbols('h')}
    waiting = {}

    for line in input_text.splitlines():
        words = line.split()
        monkey = words[0][:-1]
        
        if monkey == 'humn':
            continue
        
        if monkey == 'root':
            r1 = words[1]
            r2 = words[3]
            continue
        
        if len(words) == 2:
            results[monkey] = int(words[1])
        else:
            waiting[monkey] = tuple(words[1:])
        
    operations = {
        '+': lambda x, y : results[x] + results[y],
        '-': lambda x, y : results[x] - results[y],
        '*': lambda x, y : results[x] * results[y],
        '/': lambda x, y : results[x] / results[y],
    }
    
    while r1 not in results or r2 not in results:
        for monkey, expression in waiting.items():
            x, op, y = expression
            if x in results and y in results:
                results[monkey] = operations[op](x, y)
    
    h = solveset(results[r1] - results[r2], 'h', S.Reals)
    
    return int(h.args[0])


if __name__ == '__main__':
    with open('2022/input_files/AoC2022_day21_input.txt') as f:
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
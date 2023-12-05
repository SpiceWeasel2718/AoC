def part1(input_text: str):
    import re
    from collections import defaultdict

    numbers = defaultdict(list)
    symbols = {} # {'*', '&', '#', '$', '%', '/', '-', '@', '=', '+'}

    s = 0
    
    for x, line in enumerate(input_text.splitlines()):
        chunks = re.split(r'(\d+|[@#$%&*/\-+=])', line)
        y = 0

        for chunk in chunks:
            if chunk == '':
                continue
            elif chunk.startswith('.'):
                y += len(chunk)*1j
            elif chunk.isnumeric():
                numbers[chunk].append(x + y)
                y += len(chunk)*1j
            else:
                symbols[x + y] = chunk
                y += 1j
    
    for n, starts in numbers.items():
        for pos in starts:
            if any(z in symbols for z in [pos - 1j, pos + len(n)*1j]):
                s += int(n)
                continue
            for d in range(-1, len(n) + 1):
                if any(z in symbols for z in [pos - 1 + d*1j, pos + 1 + d*1j]):
                    s += int(n)
                    break
    
    return s


def part2(input_text: str):
    import re
    from collections import defaultdict

    numbers = {}
    symbols = defaultdict(list) # {'*', '&', '#', '$', '%', '/', '-', '@', '=', '+'}

    s = 0
    
    for x, line in enumerate(input_text.splitlines()):
        chunks = re.split(r'(\d+|[@#$%&*/\-+=])', line)
        y = 0

        for chunk in chunks:
            if chunk == '':
                continue
            elif chunk.startswith('.'):
                y += len(chunk)*1j
            elif chunk.isnumeric():
                n = int(chunk)
                for __ in range(len(chunk)):
                    numbers[x + y] = n
                    y += 1j
            else:
                symbols[chunk].append(x + y)
                y += 1j

    for pos in symbols['*']:
        adj = []

        for z in [pos-1j, pos+1j]:
            if z in numbers:
                adj.append(numbers[z])
        
        for d in [-1, 1]:
            if (z := pos + d) in numbers:
                adj.append(numbers[z])
            else:
                for z in [pos+d-1j, pos+d+1j]:
                    if z in numbers:
                        adj.append(numbers[z])
                        
        if len(adj) == 2:
            s += adj[0] * adj[1]
    return s
            

if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2023_day03_input.txt') as f:
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
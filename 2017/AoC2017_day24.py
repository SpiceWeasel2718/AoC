def part1(input_text: str):
    from collections import defaultdict
    
    pieces = defaultdict(list)
    
    for line in input_text.splitlines():
        n1, n2 = [int(n) for n in line.split('/')]
        pieces[n1].append((n1, n2))
        pieces[n2].append((n2, n1))
    
    max_value = 0
    bridges = [(0, set(), 0)]
    
    while bridges:
        port, history, value = bridges.pop()
        max_value = max(max_value, value)
        
        for piece in pieces[port]:
            n1, n2 = piece
            if (n1, n2) not in history and (n2, n1) not in history:
                bridges.append((n2, history.union({(n1, n2), (n2, n1)}), value + n1 + n2))
                
    return max_value


def part2(input_text: str):
    from collections import defaultdict
    
    pieces = defaultdict(list)
    
    for line in input_text.splitlines():
        n1, n2 = [int(n) for n in line.split('/')]
        pieces[n1].append((n1, n2))
        pieces[n2].append((n2, n1))
    
    max_value = 0
    max_length = 0
    bridges = [(0, set(), (0, 0))]
    
    while bridges:
        port, history, specs = bridges.pop()
        
        length, value = specs
        if length >= max_length:
            max_length = length
            max_value = max(max_value, value)
        
        for piece in pieces[port]:
            n1, n2 = piece
            if (n1, n2) not in history and (n2, n1) not in history:
                bridges.append((n2, history.union({(n1, n2), (n2, n1)}), (length + 1, value + n1 + n2)))
                
    return max_value


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2017_day24_input.txt') as f:
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
def part1(input_text: str):
    platform = {}
    entities = {'.': 0, '#': -1, 'O': 1}

    for a, line in enumerate(lines := input_text.splitlines()):
        for b, c in enumerate(line):
            platform[a+b*1j] = entities[c]
    
    n_rows = len(lines)
    n_cols = len(lines[0])

    for a in range(n_rows):
        for b in range(n_cols):
            z = a + b*1j
            if platform[z] == 1:
                while (w := z-1) in platform and platform[w] == 0:
                    platform[z] = 0
                    platform[w] = 1
                    z = w
    
    load = 0

    for a in range(n_rows):
        load += (n_rows - a) * [platform[a+b*1j] for b in range(n_cols)].count(1)
    
    return load


def part2(input_text: str):
    platform = {}
    entities = {'.': 0, '#': -1, 'O': 1}
    
    for a, line in enumerate(lines := input_text.splitlines()):
        for b, c in enumerate(line):
            platform[a+b*1j] = entities[c]
    
    n_rows = len(lines)
    n_cols = len(lines[0])
    
    def cycle(platform):
        for offset, d in [(0, 1), 
                          (n_rows-1, 1j), 
                          ((n_rows-1 + (n_cols-1)*1j), -1), 
                          ((n_cols-1)*1j, -1j)]:
            for a in range(n_rows):
                for b in range(n_cols):
                    z = (a + b*1j) * d + offset
                    if platform[z] == 1:
                        while (w := z-d) in platform and platform[w] == 0:
                            platform[z] = 0
                            platform[w] = 1
                            z = w
        return platform
    
    def encode_state(platform):
        n = 0
        for a in range(n_rows):
            for b in range(n_cols):
                n <<= 1
                n += (platform[a+b*1j] == 1)
        return n

    state = encode_state(platform)
    seen = set()
    history = []

    while state not in seen:
        seen.add(state)
        history.append(state)
        platform = cycle(platform)
        state = encode_state(platform)

    loop_start = history.index(state)
    loop_len = len(history) - loop_start
    n_cycles = 1000000000

    for __ in range((n_cycles - loop_start) % loop_len):
        platform = cycle(platform)

    load = 0

    for a in range(n_rows):
        load += (n_rows - a) * [platform[a+b*1j] for b in range(n_cols)].count(1)
    
    return load


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2023_day14_input.txt') as f:
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
def part1(input_text: str):
    platform = {}
    entities = {'.': 0, '#': -1, 'O': 1}
    text_lines = input_text.splitlines()
    n_lines = len(text_lines)
    n_cols = len(text_lines[0])

    for a, line in enumerate(text_lines):
        for b, c in enumerate(line):
            platform[a+b*1j] = entities[c]
    
    for a in range(n_lines):
        for b in range(n_cols):
            z = a + b*1j
            if platform[z] == 1:
                while z-1 in platform and platform[z-1] == 0:
                    platform[z] = 0
                    platform[z-1] = 1
                    z = z-1
    
    load = 0

    for a in range(n_lines):
        load += (n_lines - a) * len([platform[a+b*1j] for b in range(n_cols) if platform[a+b*1j] == 1])
    
    return load


def part2(input_text: str):
    platform = {}
    entities = {'.': 0, '#': -1, 'O': 1}
    text_lines = input_text.splitlines()
    n_lines = len(text_lines)
    n_cols = len(text_lines[0])

    for a, line in enumerate(text_lines):
        for b, c in enumerate(line):
            platform[a+b*1j] = entities[c]
    
    def cycle(platform):
        for a in range(n_lines):
            for b in range(n_cols):
                z = a + b*1j
                if platform[z] == 1:
                    while z-1 in platform and platform[z-1] == 0:
                        platform[z] = 0
                        platform[z-1] = 1
                        z = z-1
        for a in range(n_lines):
            for b in range(n_cols):
                z = b + a*1j
                if platform[z] == 1:
                    while z-1j in platform and platform[z-1j] == 0:
                        platform[z] = 0
                        platform[z-1j] = 1
                        z = z-1j
        for a in range(n_lines-1, -1, -1):
            for b in range(n_cols):
                z = a + b*1j
                if platform[z] == 1:
                    while z+1 in platform and platform[z+1] == 0:
                        platform[z] = 0
                        platform[z+1] = 1
                        z = z+1
        for a in range(n_lines):
            for b in range(n_cols-1, -1, -1):
                z = a + b*1j
                if platform[z] == 1:
                    while z+1j in platform and platform[z+1j] == 0:
                        platform[z] = 0
                        platform[z+1j] = 1
                        z = z+1j
        return platform
    
    def encode(platform):
        n = 0
        for a in range(n_lines):
            for b in range(n_cols):
                n <<= 1
                n += platform[a+b*1j]
        return n

    state = encode(platform)
    seen = set()
    history = []

    while state not in seen:
        seen.add(state)
        history.append(state)
        platform = cycle(platform)
        state = encode(platform)

    loop_start = history.index(state)
    loop_len = len(history) - loop_start
    n_cycles = 1000000000

    for __ in range((n_cycles - loop_start) % loop_len):
        platform = cycle(platform)

    load = 0

    for a in range(n_lines):
        load += (n_lines - a) * len([platform[a+b*1j] for b in range(n_cols) if platform[a+b*1j] == 1])
    
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
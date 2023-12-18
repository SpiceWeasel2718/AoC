def part1(input_text: str):
    tiles = {}
    tile_types = {
        '/': {-1: [1j], 1j: [-1], 1: [-1j], -1j: [1]},
        '\\': {-1: [-1j], 1j: [1], 1: [1j], -1j: [-1]},
        '|': {-1: [-1], 1j: [-1, 1], 1: [1], -1j: [-1, 1]},
        '-': {-1: [-1j, 1j], 1j: [1j], 1: [-1j, 1j], -1j: [-1j]},
    }

    for a, line in enumerate(lines := input_text.splitlines()):
        for b, c in enumerate(line):
            if c != '.':
                tiles[a+b*1j] = c
    
    bound_re = len(lines)
    bound_im = len(lines[0])

    energized = set()
    seen_states = set()

    beams = [(-1j, 1j)]

    while beams:
        state = beams.pop()

        if state in seen_states:
            continue
        else:
            seen_states.add(state)
        
        pos, v = state
        pos += v

        if pos.real < 0 or pos.real >= bound_re or pos.imag < 0 or pos.imag >= bound_im:
            continue

        energized.add(pos)

        if pos in tiles:
            for w in tile_types[tiles[pos]][v]:
                beams.append((pos, w))
        else:
            beams.append((pos, v))
        
    return len(energized)


def part2(input_text: str):
    tiles = {}
    tile_types = {
        '/': {-1: [1j], 1j: [-1], 1: [-1j], -1j: [1]},
        '\\': {-1: [-1j], 1j: [1], 1: [1j], -1j: [-1]},
        '|': {-1: [-1], 1j: [-1, 1], 1: [1], -1j: [-1, 1]},
        '-': {-1: [-1j, 1j], 1j: [1j], 1: [-1j, 1j], -1j: [-1j]},
    }

    for a, line in enumerate(lines := input_text.splitlines()):
        for b, c in enumerate(line):
            if c != '.':
                tiles[a+b*1j] = c
    
    bound_re = len(lines)
    bound_im = len(lines[0])

    def count_energized(start):
        energized = set()
        seen_states = set()

        beams = [start]

        while beams:
            state = beams.pop()

            if state in seen_states:
                continue
            else:
                seen_states.add(state)
            
            pos, v = state
            pos += v

            if pos.real < 0 or pos.real >= bound_re or pos.imag < 0 or pos.imag >= bound_im:
                continue

            energized.add(pos)

            if pos in tiles:
                for w in tile_types[tiles[pos]][v]:
                    beams.append((pos, w))
            else:
                beams.append((pos, v))
            
        return len(energized)

    max_energized = 0

    for re in range(bound_re):
        max_energized = max(max_energized, \
                            count_energized((re-1j, 1j)), \
                            count_energized((re+bound_im*1j, -1j)))
    
    for im in range(bound_im):
        max_energized = max(max_energized, \
                            count_energized((-1+im*1j, 1)), \
                            count_energized((bound_re+im*1j, -1)))

    return max_energized


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2023_day16_input.txt') as f:
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
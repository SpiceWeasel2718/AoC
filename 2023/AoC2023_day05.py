def part1(input_text: str):
    import math
    
    seeds_text, *maps_text = input_text.split('\n\n')

    seeds = [int(n) for n in (seeds_text.split())[1:]]
    
    maps = []

    for chunk in maps_text:
        current_map = []

        for line in (chunk.splitlines())[1:]:
            current_map.append([int(n) for n in line.split()])
        
        maps.append(current_map)
    
    min_loc = math.inf

    for seed in seeds:
        loc = seed
        
        for current_map in maps:
            for section in current_map:
                if section[1] <= loc < section[1] + section[2]:
                    loc = section[0] + loc - section[1]
                    break
        
        min_loc = min(min_loc, loc)
    
    return min_loc


def part2(input_text: str):
    seeds_text, *maps_text = input_text.split('\n\n')

    seeds = [int(n) for n in (seeds_text.split())[1:]]
    
    maps = []

    for chunk in maps_text:
        current_map = []

        for line in (chunk.splitlines())[1:]:
            current_map.append([int(n) for n in line.split()])
        
        maps.append(current_map)
    
    parts = list(zip(seeds[::2], seeds[1::2]))
    next_parts = []
    
    for current_map in maps:
        while parts:
            seed, d = parts.pop()
            seed_end = seed + d

            for dest, src, rng in current_map:
                src_end = src + rng
                if seed < src_end and src < seed_end:
                    if src <= seed:
                        if seed_end <= src_end:
                            next_parts.append((dest + seed - src, d))
                        else:
                            next_parts.append((dest + seed - src, src_end - seed))
                            parts.append((src_end, seed_end - src_end))
                        break
                    else:
                        if seed_end <= src_end:
                            next_parts.append((dest, seed_end - src))
                        else:
                            next_parts.append((dest, rng))
                            parts.append((src_end, seed_end - src_end))
                        d = src - seed
                        seed_end = src
            else:
                next_parts.append((seed, d))
        
        parts = next_parts
        next_parts = []
    
    return min([p[0] for p in parts])


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2023_day05_input.txt') as f:
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
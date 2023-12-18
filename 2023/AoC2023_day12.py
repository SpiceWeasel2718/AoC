def part1(input_text: str):
    import re

    s = 0

    for line in input_text.splitlines():
        spring_text, group_text = line.split()
        chunks = re.split(r'\.+', spring_text.strip('.'))
        springs = '.'.join(chunks)
        groups = [int(n) for n in group_text.split(',')]

        n_springs = len(springs)
        n_groups = len(groups)

        # find min and max group start indices
        pos_ranges = []
        min_pos, max_pos = 0, n_springs - (sum(groups) + n_groups - 1)
        for group in groups:
            pos_ranges.append([min_pos, max_pos])
            min_pos += group + 1
            max_pos += group + 1
        
        # find which of those start positions are actually valid placements
        valid_positions = []
        
        for group, pos_range in zip(groups, pos_ranges):
            min_pos, max_pos = pos_range
            valid_pos = []

            for pos in range(min_pos, max_pos+1):
                if (pos > 0 and springs[pos-1] == '#') or \
                    (pos + group < n_springs and springs[pos+group] == '#') or \
                    '.' in springs[pos:pos+group]:
                    continue
                else:
                    valid_pos.append(pos)

            valid_positions.append(valid_pos)
        
        # trim first and last ranges based on '#' locations
        if (l := springs.find('#')) > -1:
            valid_positions[0] = [p for p in valid_positions[0] if p <= l]
        
        if (r := springs.rfind('#')) > -1:
            valid_positions[-1] = [p for p in valid_positions[-1] if p + groups[-1] > r]

        # given a placement of group i, find valid placements of group i+1
        next_positions = []
        next_max = n_springs

        for i, group, valid_pos in zip(range(n_groups-1), groups, valid_positions):
            next_positions.append({})

            for pos in valid_pos:
                if pos > next_max:
                    break
                l = springs.find('#', pos+group+1)
                if l == -1:
                    l = n_springs
                next_positions[i][pos] = [p for p in valid_positions[i+1] if pos+group < p <= l]
            
            next_max = max(np[-1] for np in next_positions[i].values() if np)
        
        # count arrangements
        subarrangements = [{} for __ in range(n_groups-1)]
        subarrangements.append({p: 1 for p in valid_positions[-1]})

        for i in range(n_groups-2, -1, -1):
            for pos, next_pos in next_positions[i].items():
                subarrangements[i][pos] = sum(subarrangements[i+1][np] for np in next_pos)
        
        s += sum(subarrangements[0].values())

    return s


def part2(input_text: str):
    import re
            
    s = 0

    for line in input_text.splitlines():
        spring_text, group_text = line.split()
        chunks = re.split(r'\.+', ('?'.join(5 * [spring_text])).strip('.'))
        springs = '.'.join(chunks)
        groups = [int(n) for n in (','.join(5 * [group_text])).split(',')]

        n_springs = len(springs)
        n_groups = len(groups)

        # find min and max group start indices
        pos_ranges = []
        min_pos, max_pos = 0, n_springs - (sum(groups) + n_groups - 1)
        for group in groups:
            pos_ranges.append([min_pos, max_pos])
            min_pos += group + 1
            max_pos += group + 1
        
        # find which of those start positions are actually valid placements
        valid_positions = []
        
        for group, pos_range in zip(groups, pos_ranges):
            min_pos, max_pos = pos_range
            valid_pos = []

            for pos in range(min_pos, max_pos+1):
                if (pos > 0 and springs[pos-1] == '#') or \
                    (pos + group < n_springs and springs[pos+group] == '#') or \
                    '.' in springs[pos:pos+group]:
                    continue
                else:
                    valid_pos.append(pos)

            valid_positions.append(valid_pos)
        
        # trim first and last ranges based on '#' locations
        if (l := springs.find('#')) > -1:
            valid_positions[0] = [p for p in valid_positions[0] if p <= l]
        
        if (r := springs.rfind('#')) > -1:
            valid_positions[-1] = [p for p in valid_positions[-1] if p + groups[-1] > r]

        # given a placement of group i, find valid placements of group i+1
        next_positions = []
        next_max = n_springs

        for i, group, valid_pos in zip(range(n_groups-1), groups, valid_positions):
            next_positions.append({})

            for pos in valid_pos:
                if pos > next_max:
                    break
                l = springs.find('#', pos+group+1)
                if l == -1:
                    l = n_springs
                next_positions[i][pos] = [p for p in valid_positions[i+1] if pos+group < p <= l]
            
            next_max = max(np[-1] for np in next_positions[i].values() if np)
        
        # count arrangements
        subarrangements = [{} for __ in range(n_groups-1)]
        subarrangements.append({p: 1 for p in valid_positions[-1]})

        for i in range(n_groups-2, -1, -1):
            for pos, next_pos in next_positions[i].items():
                subarrangements[i][pos] = sum(subarrangements[i+1][np] for np in next_pos)
        
        s += sum(subarrangements[0].values())

    return s


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2023_day12_input.txt') as f:
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
def part1(input_text: str):
    s = 0

    for pattern in input_text.split('\n\n'):
        lines = pattern.splitlines()
        horiz= [0] * len(lines)
        vert = [0] * len(lines[0])
        
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                is_hash = (c == '#')
                horiz[i] <<= 1
                horiz[i] += is_hash
                vert[j] <<= 1
                vert[j] += is_hash
        
        for axis, value_list in enumerate([vert, horiz]):
            for line_number in range(1, len(value_list)):
                for l1, l2 in zip(value_list[line_number-1::-1], value_list[line_number:]):
                    if l1 != l2:
                        break
                else:
                    s += line_number if axis == 0 else line_number * 100
                    break
            else:
                continue
            break
    
    return s


def part2(input_text: str):
    s = 0

    for pattern in input_text.split('\n\n'):
        lines = pattern.splitlines()
        horiz= [0] * len(lines)
        vert = [0] * len(lines[0])
        
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                is_hash = (c == '#')
                horiz[i] <<= 1
                horiz[i] += is_hash
                vert[j] <<= 1
                vert[j] += is_hash
        
        for axis, value_list in enumerate([vert, horiz]):
            for line_number in range(1, len(value_list)):
                diff = 0
                for l1, l2 in zip(value_list[line_number-1::-1], value_list[line_number:]):
                    diff += (l1 ^ l2).bit_count()
                if diff == 1:
                    s += line_number if axis == 0 else line_number * 100
                    break
            else:
                continue
            break
    
    return s


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2023_day13_input.txt') as f:
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
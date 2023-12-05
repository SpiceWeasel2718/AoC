def part1(input_text: str):
    s = 0

    for line in input_text.splitlines():
        n = ''
        
        for c in line:
            if c.isdigit():
                n += c
                break
        for c in line[::-1]:
            if c.isdigit():
                n += c
                break
        
        s += int(n)
    
    return s


def part2(input_text: str):
    import re

    spellings = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    s = 0

    for line in input_text.splitlines():
        chunks = re.split(r'\d', line)
        n = ''

        start = chunks[0]
        ind = len(start)
        val = line[ind] if len(chunks) > 1 else ''
        
        if start:
            for k in spellings:
                i = start.find(k, 0, ind+1)
                if i >= 0:
                    ind = i
                    val = spellings[k]
        
        n += val

        end = chunks[-1]
        ind = 0
        val = line[-len(end)-1] if len(chunks) > 1 else ''
        
        if end:
            for k in spellings:
                i = end.rfind(k, ind)
                if i >= 0:
                    ind = i
                    val = spellings[k]
        
        n += val
    
        s += int(n)
    
    return s


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2023_day01_input.txt') as f:
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
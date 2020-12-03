def part1(input_text):
    path = {}

    for i, line in enumerate(input_text):
        for j, c in enumerate(line):
            if c in set('-+|') or c.isalpha():
                path[(i,j)] = c
    
    def vadd(v1, v2):
        return tuple(a + b for a, b in zip(v1, v2))

    def get_turns(v):
        a, b = v
        return [(b, -a), (-b, a)]

    pos = (0, input_text[0].index('|'))
    d = (1, 0)
    letters = ''

    while True:
        if path[pos] == '+':
            turns = get_turns(d)
            d = turns[0] if vadd(pos, turns[0]) in path else turns[1]
        elif path[pos].isalpha():
            letters += path[pos]
            if not any(vadd(pos, v) in path for v in get_turns(d)+[d]):
                return letters
        pos = vadd(pos, d)


def part2(input_text):
    path = {}

    for i, line in enumerate(input_text):
        for j, c in enumerate(line):
            if c in set('-+|') or c.isalpha():
                path[(i,j)] = c
    
    def vadd(v1, v2):
        return tuple(a + b for a, b in zip(v1, v2))

    def get_turns(v):
        a, b = v
        return [(b, -a), (-b, a)]

    pos = (0, input_text[0].index('|'))
    d = (1, 0)
    count = 1

    while True:
        if path[pos] == '+':
            turns = get_turns(d)
            d = turns[0] if vadd(pos, turns[0]) in path else turns[1]
        elif path[pos].isalpha():
            if not any(vadd(pos, v) in path for v in get_turns(d)+[d]):
                return count
        pos = vadd(pos, d)
        count += 1


if __name__ == "__main__":
    from pathlib import Path
    with open(next(Path().glob('**/AoC2017_day19_input.txt'))) as f:
        input_text = f.read().split('\n')

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
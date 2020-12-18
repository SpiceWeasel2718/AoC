import re

def part1(input_text):
    def paren_sub(pattern):
        res, n = re.subn(r'\*', ')*', pattern.group())
        return str(eval('('*n + res))

    s = 0

    for expr in input_text.splitlines():
        n = 1
        while n:
            expr, n = re.subn(r'\(([\d +*]+)\)', paren_sub, expr)
        
        res, n = re.subn(r'\*', ')*', expr)
        s += eval('('*n + res)
    
    return s


def part2(input_text):
    def paren_sub(pattern):
        res = re.sub(r'\*', ')*(', pattern.group())
        return str(eval(f'({res})'))

    s = 0

    for expr in input_text.splitlines():
        n = 1
        while n:
            expr, n = re.subn(r'\(([\d +*]+)\)', paren_sub, expr)
        
        res = re.sub(r'\*', ')*(', expr)
        s += eval(f'({res})')
    
    return s


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day18_input.txt') as f:
        input_text = f.read()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    time_execution = 1

    if time_execution:
        import timeit
        for part in ['part1', 'part2']:
            timer = timeit.Timer(f'{part}(input_text)', globals=globals())
            n, time = timer.autorange()
            print(f'{part} took {time/n:.5f} seconds on average when run {n} times')
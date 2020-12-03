from itertools import chain, cycle, repeat
import numpy as np
import math

def part1(input_text):
    signal = np.array([int(c) for c in input_text[0]])
    size = len(signal)

    m = np.empty((size, size), dtype=int)
    
    for i in range(1, size+1):
        pattern = chain(repeat(0, i-1), cycle(chain(repeat(1, i), repeat(0, i), repeat(-1, i), repeat(0, i))))
        m[i-1] = np.array([next(pattern) for __ in range(size)])

    for __ in range(100):
        signal = abs(m @ signal) % 10

    return ''.join([str(n) for n in signal[:8]])


def part2(input_text):
    #input_text[0] = '02935109699940807407585447034323'  # 78725270

    signal = [int(c) for c in input_text[0]]
    size = len(signal)
    offset = int(input_text[0][:7])
    n_terms = 10000*size - offset
    
    def gen_coeffs(n=99):
        f = math.factorial
        current_row = [f(n)//(f(n-i)*f(i)) % 10 for i in range(n+1)]
        yield current_row[0]
        while True:
            last_row = current_row
            current_row = []
            for a, b in zip(last_row, last_row[1:]):
                current_row.append((a+b)%10)
            current_row.append(1)
            yield current_row[0]

    g = gen_coeffs()
    coeffs = np.array([next(g) for __ in range(n_terms)])

    result = []
    for i in range(1,9):
        result.append(sum(c*s for c,s in zip(coeffs[n_terms-i::-1], cycle(signal[::-1]))) % 10)
    return ''.join([str(n) for n in result])


if __name__ == '__main__':
    from pathlib import Path
    with open(next(Path().glob('**/AoC2019_day16_input.txt'))) as f:
        input_text = f.read().splitlines()

    #print('part 1:', part1(input_text))
    #print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    print(f'part1 took at least {min(p1_timer.repeat(repeat=1, number=1)) :.5f} seconds')
    print(f'part2 took at least {min(p2_timer.repeat(repeat=1, number=1)) :.5f} seconds')



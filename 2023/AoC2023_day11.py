def part1(input_text: str):
    from itertools import combinations

    galaxies = []
    reals = set()
    ims = set()
    
    for a, line in enumerate(input_text.splitlines()):
        for b, c in enumerate(line):
            if c == '#':
                galaxies.append(a+b*1j)
                reals.add(a)
                ims.add(b)
    
    max_re = int(galaxies[-1].real)
    max_im = int(max(ims))

    missing_re = [(n not in reals) for n in range(0, max_re+1)]
    missing_im = [(n not in ims) for n in range(0, max_im+1)]
    
    s = 0
    
    for g1, g2 in combinations(galaxies, 2):
        r1, i1 = int(g1.real), int(g1.imag)
        r2, i2 = int(g2.real), int(g2.imag)

        s += abs(r2 - r1) + sum(missing_re[min(r1, r2) : max(r1, r2)])
        s += abs(i2 - i1) + sum(missing_im[min(i1, i2) : max(i1, i2)])
    
    return s


def part2(input_text: str):
    from itertools import combinations

    galaxies = []
    reals = set()
    ims = set()
    
    for a, line in enumerate(input_text.splitlines()):
        for b, c in enumerate(line):
            if c == '#':
                galaxies.append(a+b*1j)
                reals.add(a)
                ims.add(b)
    
    max_re = int(galaxies[-1].real)
    max_im = int(max(ims))

    missing_re = [(n not in reals) for n in range(0, max_re+1)]
    missing_im = [(n not in ims) for n in range(0, max_im+1)]
    
    s = 0
    coeff = 1000000 - 1
    
    for g1, g2 in combinations(galaxies, 2):
        r1, i1 = int(g1.real), int(g1.imag)
        r2, i2 = int(g2.real), int(g2.imag)

        s += abs(r2 - r1) + coeff * sum(missing_re[min(r1, r2) : max(r1, r2)])
        s += abs(i2 - i1) + coeff * sum(missing_im[min(i1, i2) : max(i1, i2)])
    
    return s


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2023_day11_input.txt') as f:
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
def part1(input_text: str):
    from math import comb

    s = 0

    for line in input_text.splitlines():
        seq = [int(i) for i in line.split()]
        layers = [[seq[0]]]
        
        while len(layers) < len(seq) and (len(layers) < 3 or any(layers[l][-1] for l in range(3))):
            layers.append([seq[len(layers[0])]])
            for i in range(len(layers[0]), 0, -1):
                layers[i-1].append(layers[i][-1] - layers[i-1][-1])

        n = len(seq)
        s += sum(c * comb(n, k) for k, c in enumerate(layers[0][:-2]))

    return s


def part2(input_text: str):
    from math import comb

    s = 0

    for line in input_text.splitlines():
        seq = [int(i) for i in (line.split())[::-1]]
        layers = [[seq[0]]]
        
        while len(layers) < len(seq) and (len(layers) < 3 or any(layers[l][-1] for l in range(3))):
            layers.append([seq[len(layers[0])]])
            for i in range(len(layers[0]), 0, -1):
                layers[i-1].append(layers[i][-1] - layers[i-1][-1])

        n = len(seq)
        s += sum(c * comb(n, k) for k, c in enumerate(layers[0][:-2]))

    return s


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2023_day09_input.txt') as f:
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
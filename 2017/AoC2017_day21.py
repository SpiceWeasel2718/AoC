import numpy as np

def part1(input_text):
    signals = {'#': 1, '.': 0}
    rules = {}

    for line in input_text:
        k, v = [np.array([[signals[c] for c in row] for row in part.split('/')]) for part in line.split(' => ')]
        rules[repr(k)] = v
        for __ in range(3):
            k = np.rot90(k)
            rules[repr(k)] = v

        k = np.fliplr(k)
        rules[repr(k)] = v
        for __ in range(3):
            k = np.rot90(k)
            rules[repr(k)] = v
    
    pattern = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ])
    
    for __ in range(5):
        size = np.shape(pattern)[0]
        n_blocks = size // 2 if size % 2 == 0 else size // 3
        blocks = [np.hsplit(row, n_blocks) for row in np.vsplit(pattern, n_blocks)]
        pattern = np.block([[rules[repr(square)] for square in row] for row in blocks])
    
    return np.sum(pattern)


def part2(input_text):
    signals = {'#': 1, '.': 0}
    rules = {}

    for line in input_text:
        k, v = [np.array([[signals[c] for c in row] for row in part.split('/')]) for part in line.split(' => ')]
        rules[repr(k)] = v
        for __ in range(3):
            k = np.rot90(k)
            rules[repr(k)] = v

        k = np.fliplr(k)
        rules[repr(k)] = v
        for __ in range(3):
            k = np.rot90(k)
            rules[repr(k)] = v
    
    pattern = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ])
    
    for __ in range(18):
        size = np.shape(pattern)[0]
        n_blocks = size // 2 if size % 2 == 0 else size // 3
        blocks = [np.hsplit(row, n_blocks) for row in np.vsplit(pattern, n_blocks)]
        pattern = np.block([[rules[repr(square)] for square in row] for row in blocks])
    
    return np.sum(pattern)


if __name__ == '__main__':
    from pathlib import Path
    with open(next(Path().glob('**/AoC2017_day21_input.txt'))) as f:
        input_text = f.read().splitlines()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    #print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    #print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
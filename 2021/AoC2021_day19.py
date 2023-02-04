def part1(input_text):
    from collections import defaultdict
    
    import numpy as np
    

    scanners = {}

    for i, block in enumerate(input_text.split('\n\n')):
        beacons = []
        for line in block.splitlines()[1:]:
            beacons.append(np.array([int(n) for n in line.split(',')]))
        scanners[i] = beacons

    def magnitude(v):
        return sum(i*i for i in v)
    
    diff_magnitudes = {}

    for s, scanner in scanners.items():
        dm = set()

        for i, v in enumerate(scanner[:-1]):
            for w in scanner[i+1:]:
                dm.add(magnitude(v-w))
        
        diff_magnitudes[s] = dm
    
    nbrs = defaultdict(list)

    for i in range(len(scanners)-1):
        for j in range(i+1, len(scanners)):
            if len(diff_magnitudes[i] & diff_magnitudes[j]) >= 66:
                nbrs[i].append(j)
                nbrs[j].append(i)
    
    breakpoint() 





def part2(input_text):
    pass


if __name__ == '__main__':
    with open('./input_files/AoC2021_day19_input.txt') as f:
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
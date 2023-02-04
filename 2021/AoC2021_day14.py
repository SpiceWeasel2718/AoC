def part1(input_text):
    from collections import Counter

    polymer, rules = input_text.split('\n\n')
    subs = {}

    for line in rules.splitlines():
        k, v = line.split(' -> ')
        subs[(k[0], k[1])] = v + k[1]

    for __ in range(10):
        next_poly = [polymer[0]]

        for c1, c2 in zip(polymer, polymer[1:]):
            next_poly.append(subs[(c1, c2)])
        
        polymer = ''.join(next_poly)
    
    counts = Counter(polymer).most_common()

    return counts[0][1] - counts[-1][1]


def part2(input_text):
    from collections import Counter

    steps = 40

    polymer, rules = input_text.split('\n\n')
    subs = {}
    
    for line in rules.splitlines():
        k, v = line.split(' -> ')
        subs[(k[0], k[1])] = v

    sequences = {}

    for pair in subs:
        start, end = pair
        seq = [start]
        
        for __ in range(steps):
            seq.append(subs[(seq[-1], end)])

        sequences[pair] = seq

    added_letters = {k: [Counter(v)] for k, v in subs.items()}

    for n in range(1, steps):
        for pair, seq in sequences.items():
            start, end = pair
            
            c = Counter(seq[1 : n+1])
            
            for i, p in enumerate(zip(seq[:n], seq[1 : n+1])):
                c += added_letters[p][n-1-i]
            
            c += added_letters[(seq[n], end)][0]
            
            added_letters[pair].append(c)
    
    c = Counter(polymer)

    for pair in zip(polymer, polymer[1:]):
        c += added_letters[pair][steps-1]
    
    counts = c.most_common()

    return counts[0][1] - counts[-1][1]


if __name__ == '__main__':
    with open('./input_files/AoC2021_day14_input.txt') as f:
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
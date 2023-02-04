def part1(input_text: str):
    claims = []

    for line in input_text.splitlines():
        __, __, s1, s2 = line.split()
        claim = [int(n) for n in s1[:-1].split(',')]
        rec = [int(n) for n in s2.split('x')]
        claim.extend([n+d-1 for n, d in zip(claim, rec)])
        claims.append(claim)
    
    overlap = set()

    for i, rec1 in enumerate(claims):
        x1, y1, x2, y2 = rec1
        for rec2 in claims[i+1:]:
            a1, b1, a2, b2 = rec2
            # check for overlap
            if not any([x2 < a1, x1 > a2, y2 < b1, y1 > b2]):
                # add all coordinates in intersection to set
                for x in range(max(x1, a1), min(x2, a2)+1):
                    for y in range(max(y1, b1), min(y2, b2)+1):
                        overlap.add((x, y))
    
    return len(overlap)


def part2(input_text: str):
    claims = []

    for line in input_text.splitlines():
        claim_id, __, s1, s2 = line.split()
        claim = [int(n) for n in s1[:-1].split(',')]
        rec = [int(n) for n in s2.split('x')]
        claim.extend([n+d-1 for n, d in zip(claim, rec)])
        claim.append(int(claim_id[1:]))
        claims.append(claim)
    
    overlaps = set(range(1, len(claims)+1))
    
    for i, rec1 in enumerate(claims):
        x1, y1, x2, y2, id1 = rec1
        for rec2 in claims[i+1:]:
            a1, b1, a2, b2, id2 = rec2
            # check for overlap
            if not any([x2 < a1, x1 > a2, y2 < b1, y1 > b2]):
                overlaps.discard(id1)
                overlaps.discard(id2)

    return overlaps.pop()


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2018_day03_input.txt') as f:
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
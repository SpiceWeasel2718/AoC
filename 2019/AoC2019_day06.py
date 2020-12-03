def part1(input_text):
    from collections import defaultdict

    orbits = [string.split(')') for string in input_text]

    orbit_tree = defaultdict(set)

    for orbit in orbits:
        orbit_tree[orbit[0]].add(orbit[1])
    
    count = 0
    depth = 0
    current_level = set()
    next_level = set(['COM'])

    while len(next_level) > 0:
        depth += 1
        current_level, next_level = next_level, set()

        for node in current_level:
            try:
                count += depth * len(orbit_tree[node])
                next_level.update(orbit_tree[node])
            except KeyError:
                pass
    
    return count


def part2(input_text):
    orbits = [string.split(')') for string in input_text]

    parents = {orbit[1]: orbit[0] for orbit in orbits}
    
    you = ['YOU']
    while you[-1] != 'COM':
        you.append(parents[you[-1]])
    
    san = ['SAN']
    while san[-1] != 'COM':
        san.append(parents[san[-1]])

    ind = -1
    while you[ind] == san[ind]:
        ind -= 1
    
    meet = you[ind + 1]

    return you.index(meet) + san.index(meet) - 2


if __name__ == '__main__':
    from pathlib import Path
    with open(next(Path().glob('**/AoC2019_day06_input.txt'))) as f:
        input_text = f.read().split('\n')

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
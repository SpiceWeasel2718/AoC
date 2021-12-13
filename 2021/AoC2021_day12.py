def part1(input_text):
    from collections import defaultdict, deque
    
    nbrs = defaultdict(set)

    for line in input_text.splitlines():
        a, b = line.split('-')
        nbrs[a].add(b)
        nbrs[b].add(a)
    
    queue = deque([node, {'start'}] for node in nbrs['start'])
    count = 0

    while queue:
        current, seen = queue.pop()

        if current == 'end':
            count += 1
            continue
        elif current.islower():
            seen.add(current)

        for nbr in nbrs[current] - seen:
            queue.append([nbr, seen.copy()])
    
    return count


def part2(input_text):
    from collections import defaultdict, deque
    
    nbrs = defaultdict(set)

    for line in input_text.splitlines():
        a, b = line.split('-')
        if b != 'start':
            nbrs[a].add(b)
        if a != 'start':
            nbrs[b].add(a)
    
    queue = deque([node, {'start'}, False] for node in nbrs['start'])
    count = 0

    while queue:
        current, seen, twice = queue.pop()

        if current == 'end':
            count += 1
            continue
        elif current.islower():
            seen.add(current)

        if twice:
            for nbr in nbrs[current] - seen:
                queue.append([nbr, seen.copy(), True])
        else:
            for nbr in nbrs[current]:
                queue.append([nbr, seen.copy(), (nbr in seen)])
    
    return count


if __name__ == '__main__':
    with open('./input_files/AoC2021_day12_input.txt') as f:
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
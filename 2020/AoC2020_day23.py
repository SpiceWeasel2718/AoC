def part1(input_text):
    cups = {}
    prev = None

    for c in input_text.rstrip():
        n = int(c) - 1
        if prev is None:
            current = n
        else:
            cups[prev] = n
        prev = n
    
    cups[prev] = current
    n_cups = len(cups)

    for __ in range(100):
        start = cups[current]
        middle = cups[start]
        end = cups[middle]

        destination = (current - 1) % n_cups
        while destination in [start, middle, end]:
            destination = (destination - 1) % n_cups
        
        n = cups[end]
        cups[current] = n
        current = n

        n = cups[destination]
        cups[destination] = start
        cups[end] = n
    
    seq = [cups[0]]
    for __ in range(7):
        seq.append(cups[seq[-1]])

    return ''.join(str(n+1) for n in seq)


def part2(input_text):
    cups = {}
    prev = None

    for c in input_text.rstrip():
        n = int(c) - 1
        if prev is None:
            current = n
        else:
            cups[prev] = n
        prev = n
    
    for n in range(9, 1000000):
        cups[prev] = n
        prev = n
    
    cups[prev] = current
    n_cups = len(cups)

    for __ in range(10000000):
        start = cups[current]
        middle = cups[start]
        end = cups[middle]

        destination = (current - 1) % n_cups
        while destination in [start, middle, end]:
            destination = (destination - 1) % n_cups
        
        n = cups[end]
        cups[current] = n
        current = n

        n = cups[destination]
        cups[destination] = start
        cups[end] = n

    return (cups[0] + 1) * (cups[cups[0]] + 1)


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day23_input.txt') as f:
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
def part1(input_text):
    target, id_str = input_text.splitlines()
    target = int(target)
    ids = id_str.split(',')

    best_wait = target
    best_id = 0

    for n in ids:
        if n != 'x':
            bus_id = int(n)
            wait = bus_id - (target % bus_id)
            if wait < best_wait:
                best_id = bus_id
                best_wait = wait
    
    return best_wait * best_id


def part2(input_text):
    ids = input_text.splitlines()[1].split(',')
    id_iter = ((i, int(n)) for i, n in enumerate(ids) if n != 'x')

    x = next(id_iter)[1]
    increment = x

    for a, n in id_iter:
        x += a
        while x % n:
            x += increment
        x -= a
        increment *= n

    return x


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day13_input.txt') as f:
        input_text = f.read()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    time_execution = 1

    if time_execution:
        import timeit
        for part in ['part1', 'part2']:
            timer = timeit.Timer(f'{part}(input_text)', globals=globals())
            n, time = timer.autorange()
            print(f'{part} took {time/n:.5f} seconds on average when run {n} times')
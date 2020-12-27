def part1(input_text):
    card_public, door_public = (int(n) for n in input_text.rstrip().splitlines())
    
    value = 1
    key = 1

    while value != card_public:
        value = (value * 7) % 20201227
        key = (key * door_public) % 20201227

    return key


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day25_input.txt') as f:
        input_text = f.read()

    print('part 1:', part1(input_text))

    time_execution = 1

    if time_execution:
        import timeit
        timer = timeit.Timer(f'part1(input_text)', globals=globals())
        n, time = timer.autorange()
        print(f'part1 took {time/n:.5f} seconds on average when run {n} times')
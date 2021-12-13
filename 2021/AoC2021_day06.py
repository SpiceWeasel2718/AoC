def part1(input_text):
    fish = [0] * 9
    
    for n in input_text.split(','):
        fish[int(n)] += 1
    
    for d in range(80):
        fish[(d + 7) % 9] += fish[d % 9]

    return sum(fish)


def part2(input_text):
    fish = [0] * 9
    
    for n in input_text.split(','):
        fish[int(n)] += 1
    
    for d in range(256):
        fish[(d + 7) % 9] += fish[d % 9]

    return sum(fish)


if __name__ == '__main__':
    with open('./input_files/AoC2021_day06_input.txt') as f:
        input_text = f.read()
    
    input_text0 = "3,4,3,1,2"

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    time_execution = 0

    if time_execution:
        import timeit
        for part in ['part1', 'part2']:
            timer = timeit.Timer(f'{part}(input_text)', globals=globals())
            n, time = timer.autorange()
            print(f'{part} took {time/n:.5f} seconds on average when run {n} times')
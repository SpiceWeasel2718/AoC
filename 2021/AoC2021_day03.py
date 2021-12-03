def part1(input_text):
    numbers = input_text.splitlines()
    count = [0] * len(numbers[0])

    for number in numbers:
        for i, c in enumerate(number):
            count[i] += (c == '1')

    gamma = 0
    half = len(numbers) / 2

    for i, n in enumerate(reversed(count)):
        if n > half:
            gamma += 2**i
    
    return gamma * (gamma ^ (2**len(count) - 1))


def part2(input_text):
    numbers_str = input_text.splitlines()
    numbers = [int(n, base=2) for n in numbers_str]
    partitions = [[set(), set()] for __ in range(len(numbers_str[0]))]

    for n, s in zip(numbers, numbers_str):
        for i, c in enumerate(s):
            partitions[i][(c == '1')].add(n)

    if len(partitions[0][1]) >= len(numbers) / 2:
        uncommon, common = partitions[0]
    else:
        common, uncommon = partitions[0]
    
    i = 1

    while len(common) > 1:
        zeros = common & partitions[i][0]
        ones = common & partitions[i][1]

        common = ones if len(ones) >= len(zeros) else zeros
        i += 1

    i = 1

    while len(uncommon) > 1:
        zeros = uncommon & partitions[i][0]
        ones = uncommon & partitions[i][1]
        
        uncommon = ones if len(ones) < len(zeros) else zeros
        i += 1

    return common.pop() * uncommon.pop()
    

    

if __name__ == '__main__':
    with open('./input_files/AoC2021_day03_input.txt') as f:
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
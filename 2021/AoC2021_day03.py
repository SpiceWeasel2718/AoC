def part1(input_text):
    numbers = input_text.splitlines()
    bits = len(numbers[0])
    count = [0] * bits

    for i in range(bits):
        count[i] = sum((n[i] == '1') for n in numbers)

    gamma = 0
    half = len(numbers) / 2

    for c in count:
        gamma <<= 1
        gamma += (c > half)
    
    return gamma * (gamma ^ (2**bits - 1))


def part2(input_text):
    numbers = input_text.splitlines()
    bits = len(numbers[0])
    binary = [int(n, 2) for n in numbers]

    def partition(num_list, mask):
        if len(num_list) <= 1:
            return num_list

        ones = []
        zeros = []
        
        for n in num_list:
            if n & mask:
                ones.append(n)
            else:
                zeros.append(n)
        
        return (ones, zeros) if len(ones) >= len(zeros) else (zeros, ones)
        
    mask = 1 << (bits - 1)
    common, uncommon = partition(binary, mask)

    while len(common) > 1 and len(uncommon) > 1:
        mask >>= 1
        common, __ = partition(common, mask)
        __, uncommon = partition(uncommon, mask)        
    
    return common[0] * uncommon[0]
    

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
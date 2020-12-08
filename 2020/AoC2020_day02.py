def part1(input_text):
    valid = 0

    for line in input_text.splitlines():
        policy, letter, pswd = line.split(' ')
        min_n, max_n = [int(n) for n in policy.split('-')]
        letter = letter[0]

        count = 0
        for c in pswd:
            count += (c == letter)
        
        if min_n <= count <= max_n:
            valid += 1
    
    return valid
            

def part2(input_text):
    valid = 0

    for line in input_text.splitlines():
        policy, letter, pswd = line.split(' ')
        i1, i2 = [int(n)-1 for n in policy.split('-')]
        letter = letter[0]

        if (pswd[i1] == letter) != (pswd[i2] == letter):
            valid += 1
    
    return valid


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day02_input.txt') as f:
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
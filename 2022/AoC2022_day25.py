def part1(input_text: str):
    digits = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
    s = 0
    
    for line in input_text.splitlines():
        power = 1
        
        for c in line[::-1]:
            s += digits[c] * power
            power *= 5

    number = []
    
    while s:
        rem = s % 5
        
        if rem <= 2:
            number.append(str(rem))
        else:
            s += 5
            number.append('=' if rem == 3 else '-')
            
        s = (s - rem) // 5
        
    return ''.join(number[::-1])


if __name__ == '__main__':
    with open('2022/input_files/AoC2022_day25_input.txt') as f:
        input_text = f.read()
    
    print('part 1:', part1(input_text))

    time_execution = 0

    if time_execution:
        import timeit
        for part in ['part1']:
            timer = timeit.Timer(f'{part}(input_text)', globals=globals())
            n, time = timer.autorange()
            print(f'{part} took {time/n:.5f} seconds on average when run {n} times')
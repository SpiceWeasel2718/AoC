def part1(input_text):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    count = 0
    
    for block in input_text.split('\n\n'):
        passport = set()
        for pair in block.split():
            passport.add(pair.split(':')[0])
    
        count += all(r in passport for r in required)
    
    return count


def part2(input_text):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    hexdigits = set('0123456789abcdef')
    count = 0

    for block in input_text.split('\n\n'):
        passport = {}
        for pair in block.split():
            k, v = pair.split(':')
            passport[k] = v
    
        if not all(r in passport for r in required):
            continue

        if not all([
                (1920 <= int(passport['byr']) <= 2002),
                (2010 <= int(passport['iyr']) <= 2020),
                (2020 <= int(passport['eyr']) <= 2030)
        ]):
            continue
        
        hgt = passport['hgt']
        if hgt.endswith('cm'):
            if not 150 <= int(hgt[:-2]) <= 193:
                continue
        elif hgt .endswith('in'):
            if not 59 <= int(hgt[:-2]) <= 76:
                continue
        else:
            continue
        
        hcl = passport['hcl']
        if len(hcl) != 7 or not hcl[0] == '#' or not all(c in hexdigits for c in hcl[1:]):
            continue

        if not passport['ecl'] in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
            continue
        
        pid = passport['pid']
        if len(pid) != 9 or not pid.isnumeric():
            continue
        
        count += 1
    
    return count


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day04_input.txt') as f:
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
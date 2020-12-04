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

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    # print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    # print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
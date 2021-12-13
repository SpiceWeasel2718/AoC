def part1(input_text):
    unique_lengths = {2, 4, 3, 7}
    count = 0

    for line in input_text.splitlines():
        __, display = line.split(' | ')
        
        for digit in display.split():
            count += (len(digit) in unique_lengths)
    
    return count


def part2(input_text):
    total = 0
    
    for line in input_text.splitlines():
        digits, display = line.split(' | ')
        fives = []
        sixes = []

        for digit in digits.split():
            match len(digit):
                case 2:
                    one = frozenset(digit)
                case 3:
                    seven = frozenset(digit)
                case 4:
                    four = frozenset(digit)
                case 5:
                    fives.append(frozenset(digit))
                case 6:
                    sixes.append(frozenset(digit))
                case 7:
                    eight = frozenset(digit)
        
        for d in sixes:
            if four <= d:
                nine = d
            elif one <= d:
                zero = d
            else:
                six = d
        
        for d in fives:
            if one <= d:
                three = d
            elif d <= nine:
                five = d
            else:
                two = d
        
        numbers = {
            zero: 0,
            one: 1,
            two: 2,
            three: 3,
            four: 4,
            five: 5, 
            six: 6,
            seven: 7,
            eight: 8,
            nine: 9
        }

        value = 0

        for digit in display.split():
            value = 10*value + numbers[frozenset(digit)]
        
        total += value
    
    return total


if __name__ == '__main__':
    with open('./input_files/AoC2021_day08_input.txt') as f:
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
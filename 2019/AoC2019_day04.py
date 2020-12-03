def increment(digit_list, end):
    while digit_list < end:
        yield digit_list
        if digit_list[-1] < 9:
            digit_list[-1] += 1
        else:
            rollover_ind = digit_list.index(9) - 1
            new_value = digit_list[rollover_ind] + 1
            for i in range(rollover_ind, 6):
                digit_list[i] = new_value
            

def part1(input_text):
    lower, upper = ([int(c) for c in string] for string in input_text.split('-'))
    
    def valid_pass(digit_list):
        has_double = False
        for i in range(5):
            if digit_list[i] > digit_list[i+1]:
                return False
            if digit_list[i] == digit_list[i+1]:
                has_double = True
        return has_double
    
    count = 0

    for password in increment(lower, upper):
        if valid_pass(password):
            count += 1
    
    return count


def part2(input_text):
    import collections
    lower, upper = ([int(c) for c in string] for string in input_text.split('-'))

    def valid_pass(digit_list):
        for i in range(5):
            if digit_list[i+1] < digit_list[i]:
                return False
        c = collections.Counter(digit_list)
        for k in c:
            if c[k] == 2:
                return True
        else:
            return False

    count = 0

    for password in increment(lower, upper):
        if valid_pass(password):
            count += 1
    
    return count


if __name__ == "__main__":
    import timeit
    
    input_text = '168630-718098'
    
    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
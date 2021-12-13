def part1(input_text):
    positions = [int(n) for n in input_text.split(',')]

    def sum_dist(point):
        return sum(abs(point - p) for p in positions)

    left, right = min(positions), max(positions)
    mid = (right + left) // 2

    while right - left > 1:
        value = sum_dist(mid)
        test_val = value
        offset = mid
        
        while test_val == value:
            offset += 1
            test_val = sum_dist(offset)
        
        if test_val < value:
            left = offset
        else:
            right = mid
        
        mid = (right + left) // 2
    
    return min(sum_dist(left), sum_dist(right))


def part2(input_text):
    positions = [int(n) for n in input_text.split(',')]

    def sum_dist(point):
        s = 0
        for p in positions:
            n = abs(point - p)
            s += n * (n + 1) // 2
        return s

    left, right = min(positions), max(positions)
    mid = (right + left) // 2

    while right - left > 1:
        value = sum_dist(mid)
        test_val = value
        offset = mid
        
        while test_val == value:
            offset += 1
            test_val = sum_dist(offset)
        
        if test_val < value:
            left = offset
        else:
            right = mid
        
        mid = (right + left) // 2
    
    return min(sum_dist(left), sum_dist(right))


if __name__ == '__main__':
    with open('./input_files/AoC2021_day07_input.txt') as f:
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
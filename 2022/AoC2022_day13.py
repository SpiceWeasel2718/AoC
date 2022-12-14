def part1(input_text: str):
    
    def compare(left, right):
        for l, r in zip(left, right):
            tl, tr = (type(l) is int), (type(r) is int)
            
            if tl and tr:
                if l != r:
                    return l < r
            else:
                sub_check = compare([l] if tl else l, [r] if tr else r)
                if sub_check is not None:
                    return sub_check
        
        if len(left) != len(right):
            return len(left) < len(right)
        else:
            return None

    
    input_list = input_text.splitlines()
    correct = []
    
    for i, l, r in zip(range(1, len(input_list)), input_list[::3], input_list[1::3]):
        left = eval(l)
        right = eval(r)
        
        if compare(left, right):
            correct.append(i)
                
    return sum(correct)


def part2(input_text: str):
    from functools import cmp_to_key
    
    def compare(left, right):
        for l, r in zip(left, right):
            tl, tr = (type(l) is int), (type(r) is int)
            
            if tl and tr:
                if l != r:
                    return -1 if l < r else 1
            else:
                sub_check = compare([l] if tl else l, [r] if tr else r)
                if sub_check != 0:
                    return sub_check
        
        if len(left) != len(right):
            return -1 if len(left) < len(right) else 1
        else:
            return 0

    
    input_list = input_text.splitlines()
    packets = [[[2]], [[6]]]
    
    for l, r in zip(input_list[::3], input_list[1::3]):
        packets.append(eval(l))
        packets.append(eval(r))

    packets.sort(key=cmp_to_key(compare))
    
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


if __name__ == '__main__':
    with open('2022/input_files/AoC2022_day13_input.txt') as f:
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
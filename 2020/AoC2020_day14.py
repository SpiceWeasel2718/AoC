def part1(input_text):
    mem = {}
    
    for line in input_text.splitlines():
        var, val = line.split(' = ', 1)
        if var == 'mask':
            mask_or = 0
            mask_and = 0
            for c in val:
                mask_or <<= 1
                mask_and <<= 1
                if c != '0':
                    mask_and += 1
                    if c == '1':
                        mask_or += 1
        else:
            mem[var] = (int(val) | mask_or) & mask_and
    
    return sum(mem.values())


def part2(input_text):
    all_ones = 2**36 - 1
    mem = {}
    
    for line in input_text.splitlines():
        var, val = line.split(' = ', 1)

        if var == 'mask':
            x_masks = []
            mask0 = 0
            
            for i, c in enumerate(val):
                mask0 <<= 1
                if c != '0':
                    mask0 += 1
                    if c == 'X':
                        x_masks.append(all_ones ^ (1 << (35-i)))
                        
        else:
            addrs = [int(var[4:-1]) | mask0]

            for x_mask in x_masks:
                new_addrs = []
                for addr in addrs:
                    new_addrs.append(addr & x_mask)
                addrs.extend(new_addrs)
            
            for addr in addrs:
                mem[addr] = val
    
    return sum(int(val) for val in mem.values())


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day14_input.txt') as f:
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
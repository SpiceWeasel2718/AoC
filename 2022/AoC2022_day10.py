def part1(input_text):
    cycle_num = 0
    x = 1
    total = 0
    
    for line in input_text.splitlines():
        cycle_num += 1
        if (cycle_num - 20) % 40 == 0:
            total += cycle_num * x
    
        if line != 'noop':
            cycle_num += 1
            if (cycle_num - 20) % 40 == 0:
                total += cycle_num * x
            x += int(line.split()[1])

    return total


def part2(input_text):
    cycle_num = 0
    x = 1
    pixels = []
    
    for line in input_text.splitlines():
        pixels.append('#' if x-1 <= cycle_num % 40 <= x+1 else '.')
        cycle_num += 1
    
        if line != 'noop':
            pixels.append('#' if x-1 <= cycle_num % 40 <= x+1 else '.')
            cycle_num += 1
            x += int(line.split()[1])
    
    output = ''
    
    for row in range(6):
        output += '\n' + ''.join(pixels[row*40:(row+1)*40])
    
    return output


if __name__ == '__main__':
    with open('./input_files/AoC2022_day10_input.txt') as f:
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
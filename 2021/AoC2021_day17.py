def part1(input_text):
    y_bounds = (input_text.rsplit('=', maxsplit=1)[1]).split('..')
    lower = int(y_bounds[0])
    return lower * (lower + 1) // 2

def part2(input_text):
    from math import sqrt, ceil
    from collections import defaultdict

    *__, x_text, y_text = input_text.split()
    x_l, x_u = [int(n) for n in x_text[2:-1].split('..')]
    y_l, y_u = [int(n) for n in y_text[2:].split('..')]
    
    min_v_x, max_v_x = ceil(-0.5 + sqrt(0.25 + 2*x_l)), x_u
    min_v_y, max_v_y = y_l, -y_l - 1

    v_x_per_step = defaultdict(list)
    v_y_per_step = defaultdict(list)
    
    for v_y in range(min_v_y, max_v_y+1):
        if v_y >= 0:
            y = 0
            v = -v_y - 1
            step = 2 * v_y + 1
        else:
            y = v_y
            v = v_y - 1
            step = 1

        while y >= y_l:
            if y <= y_u:
                v_y_per_step[step].append(v_y)

            y += v
            v -= 1
            step += 1
    
    max_steps = max(v_y_per_step)

    for v_x in range(min_v_x, max_v_x+1):
        x = v_x
        v = v_x - 1
        step = 1

        while x <= x_u and step <= max_steps:
            if x >= x_l:
                v_x_per_step[step].append(v_x)
            
            x += v
            v -= (v > 0)
            step += 1

    vectors = set()

    for n in range(max_steps+1):
        for v_x in v_x_per_step[n]:
            for v_y in v_y_per_step[n]:
                vectors.add((v_x, v_y))
    
    return len(vectors)



if __name__ == '__main__':
    with open('./2021/input_files/AoC2021_day17_input.txt') as f:
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
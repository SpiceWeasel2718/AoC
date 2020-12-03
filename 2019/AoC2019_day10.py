import math

def gen_lines(x_size, y_size=0):
    if not y_size:
        y_size = x_size
    for dx in range(-x_size+1, x_size):
        for dy in range(-y_size+1, y_size):
            if math.gcd(dx, dy) == 1:
                yield (dx, dy)
            

def part1(input_text):
    asteroids = [[1 if c=='#' else 0 for c in line.strip()] for line in input_text]
    x_size = len(asteroids[0])
    y_size = len(asteroids)

    directions = list(gen_lines(len(asteroids)))

    maxval = 0

    for i in range(x_size):
        for j in range(y_size):
            count = 0
            for dx, dy in directions:
                x, y = i, j
                while True:
                    x += dx
                    y += dy
                    
                    if 0 <= x < x_size and 0 <= y < y_size:
                        if asteroids[y][x]:
                            count += 1
                            break
                    else:
                        break
            
            if count > maxval:
                maxval = count
                best_pos = (i, j)
    
    return best_pos, maxval


def part2(input_text, best_pos=(13, 17)):
    asteroids = [[1 if c=='#' else 0 for c in line.strip()] for line in input_text]
    x_size = len(asteroids[0])
    y_size = len(asteroids)

    directions = []
    for dx, dy in gen_lines(len(asteroids)):
        x, y = best_pos
        while True:
            x += dx
            y += dy
            if 0 <= x < x_size and 0 <= y < y_size:
                if asteroids[y][x]:
                    directions.append((dx, dy))
                    break
            else:
                break

    directions.sort(key=lambda dxdy: math.atan2(-dxdy[0], dxdy[1]))
    dx, dy = directions[198]  # (0, -1) causes an off-by-1
    
    x, y = best_pos
    x += dx
    y += dy
    while not asteroids[y][x]:
        x += dx
        y += dy
    
    return 100*x + y


if __name__ == '__main__':
    from pathlib import Path
    with open(next(Path().glob('**/AoC2019_day10_input.txt'))) as f:
        input_text = f.read().splitlines()

    best_pos, answer = part1(input_text)
    print('part 1:', answer)
    print('part 2:', part2(input_text, best_pos))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
def part1(input_text):
    mask = [[(c == 'L') for c in line] for line in input_text.splitlines()]
    rows = len(mask)
    cols = len(mask[0])
    area = [[0]*cols for __ in range(rows)]
    old_area = []

    nbr_offset = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    while old_area != area:
        old_area, area = area, [[0]*cols for __ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                if not mask[r][c]:
                    continue
                count = 0
                for ro, co in nbr_offset:
                    if 0 <= (rr := r + ro) < rows and 0 <= (cc := c + co) < cols:
                        count += old_area[rr][cc]
                if not old_area[r][c] and count == 0:
                    area[r][c] = 1
                elif old_area[r][c] and count >= 4:
                    area[r][c] = 0
                else:
                    area[r][c] = old_area[r][c]
    
    return sum(sum(row) for row in area)
        


def part2(input_text):
    mask = [[(c == 'L') for c in line] for line in input_text.splitlines()]
    rows = len(mask)
    cols = len(mask[0])
    area = [[0]*cols for __ in range(rows)]
    old_area = []

    nbr_offset = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    while old_area != area:
        old_area, area = area, [[0]*cols for __ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                if not mask[r][c]:
                    continue
                count = 0
                for ro, co in nbr_offset:
                    rr, cc = r + ro, c + co
                    while (0 <= rr < rows and 0 <= cc < cols) and not mask[rr][cc]:
                        rr += ro
                        cc += co
                    if (0 <= rr < rows and 0 <= cc < cols):
                        count += old_area[rr][cc]
                if not old_area[r][c] and count == 0:
                    area[r][c] = 1
                elif old_area[r][c] and count >= 5:
                    area[r][c] = 0
                else:
                    area[r][c] = old_area[r][c]
    
    return sum(sum(row) for row in area)


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day11_input.txt') as f:
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
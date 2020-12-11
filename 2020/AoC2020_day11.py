def part1(input_text):
    old_area = {}
    area = {}

    for r, line in enumerate(input_text.splitlines()):
        for c, char in enumerate(line):
            if char == 'L':
                area[(r, c)] = 0

    nbr_offset = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbors = {}
    for r, c in area:
        neighbors[(r, c)] = [(r+ro, c+co) for ro, co in nbr_offset if (r+ro, c+co) in area]
    
    changed = True

    while changed:
        old_area, area = area, {}
        changed = False

        for pos in old_area:
            count = sum(old_area[nbr] for nbr in neighbors[pos])
            if count == 0 and not old_area[pos]:
                area[pos] = 1
                changed = True
            elif count >= 4 and old_area[pos]:
                area[pos] = 0
                changed = True
            else:
                area[pos] = old_area[pos]
    
    return sum(area.values())


def part2(input_text):
    old_area = {}
    area = {}
    all_seats = set()

    for r, line in enumerate(input_list := input_text.splitlines()):
        for c, char in enumerate(line):
            all_seats.add((r, c))
            if char == 'L':
                area[(r, c)] = 0

    rows, cols = len(input_list), len(input_list[0])

    nbr_offset = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbors = {}
    
    for r, c in area:
        neighbors[(r, c)] = []
        for ro, co in nbr_offset:
            rr, cc = r + ro, c + co
            while (rr, cc) not in area:
                rr += ro
                cc += co
                if (rr, cc) not in all_seats:
                    break
            else:
                neighbors[(r, c)].append((rr, cc))

    changed = True

    while changed:
        old_area, area = area, {}
        changed = False
        
        for pos in old_area:
            count = sum(old_area[nbr] for nbr in neighbors[pos])
            if count == 0 and not old_area[pos]:
                area[pos] = 1
                changed = True
            elif count >= 5 and old_area[pos]:
                area[pos] = 0
                changed = True
            else:
                area[pos] = old_area[pos]
    
    return sum(area.values())


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day11_input.txt') as f:
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
def part1(input_text):
    grid = {}

    for re, line in enumerate(input_text.splitlines()):
        for im, c in enumerate(line):
            grid[re + im*1j] = int(c)

    total = 0

    for pos in grid:
        height = grid[pos]

        for direction in [1, -1, 1j, -1j]:
            cur_pos = pos + direction

            while cur_pos in grid:
                if grid[cur_pos] >= height:
                    break
                cur_pos += direction
            else:
                total += 1
                break

    return total


def part2(input_text):
    grid = {}

    for re, line in enumerate(input_text.splitlines()):
        for im, c in enumerate(line):
            grid[re + im*1j] = int(c)

    max_score = 0

    for pos in grid:
        height = grid[pos]
        score = 1

        for direction in [1, -1, 1j, -1j]:
            cur_pos = pos + direction
            trees = 0

            while cur_pos in grid:
                trees += 1
                if grid[cur_pos] >= height:
                    break
                cur_pos += direction

            score *= trees
        
        max_score = max(score, max_score)
            
    return max_score


if __name__ == '__main__':
    with open('./input_files/AoC2022_day08_input.txt') as f:
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
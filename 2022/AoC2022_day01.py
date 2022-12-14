def part1(input_text: str):
    m = 0
    temp = 0

    for line in input_text.splitlines():
        if line:
            temp += int(line)
        else:
            m = max(m, temp)
            temp = 0
    
    return m


def part2(input_text: str):
    import heapq
    
    top3 = []
    temp = 0
    
    for line in input_text.splitlines():
        if line:
            temp += int(line)
        else:
            if len(top3) < 3:
                heapq.heappush(top3, temp)
            else:
                heapq.heappushpop(top3, temp)

            temp = 0
    
    return sum(top3)


if __name__ == '__main__':
    with open('2022/input_files/AoC2022_day01_input.txt') as f:
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
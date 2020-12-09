from collections import deque, Counter

def part1(input_text):
    series = [int(n) for n in input_text.splitlines()]
    forward_sums = deque()
    valid_values = Counter()

    for i, num in enumerate(series[:25]):
        forward_sums.append([num + n for n in series[i+1:i+25]])
        valid_values.update([num + n for n in series[:i]])

    for i, num in enumerate(series[25:], start=25):
        if not valid_values[num]:
            return num
        valid_values.subtract(forward_sums.popleft())
        valid_values.update([sums_list[j] for j, sums_list in enumerate(reversed(forward_sums))])
        forward_sums.append([num + n for n in series[i+1:i+25]])


def part2(input_text, target):
    series = [int(n) for n in input_text.splitlines()]
    series_len = len(series)

    start_iter = iter(range(series_len))
    end_iter = iter(range(1, series_len))
    start = next(start_iter)
    end = next(end_iter)
    total = sum(series[:2])

    while total != target:
        if total < target:
            end = next(end_iter)
            total += series[end]
        else:
            total -= series[start]
            start = next(start_iter)

    return min(seq := series[start:end+1]) + max(seq)


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day09_input.txt') as f:
        input_text = f.read()

    print('part 1:', (target := part1(input_text)))
    print('part 2:', part2(input_text, target))

    time_execution = 1

    if time_execution:
        import timeit
        timer = timeit.Timer(f'part1(input_text)', globals=globals())
        n, time = timer.autorange()
        print(f'part1 took {time/n:.5f} seconds on average when run {n} times')
        
        timer = timeit.Timer(f'part2(input_text, target)', globals=globals())
        n, time = timer.autorange()
        print(f'part2 took {time/n:.5f} seconds on average when run {n} times')
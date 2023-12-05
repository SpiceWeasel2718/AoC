def part1(input_text: str):
    s = 0

    for line in input_text.splitlines():
        label, draws = line.split(': ', maxsplit=1)
        game_id = int(label[5:])
        max_counts = {'red': 0, 'green': 0, 'blue': 0}
        
        for draw in draws.split('; '):
            for color_count in draw.split(', '):
                n, color = color_count.split(' ', maxsplit=1)
                max_counts[color] = max(int(n), max_counts[color])
        
        if max_counts['red'] <= 12 and max_counts['green'] <= 13 and max_counts['blue'] <= 14:
            s += game_id
    
    return s


def part2(input_text: str):
    s = 0

    for line in input_text.splitlines():
        _, draws = line.split(': ', maxsplit=1)
        max_counts = {'red': 0, 'green': 0, 'blue': 0}
        
        for draw in draws.split('; '):
            for color_count in draw.split(', '):
                n, color = color_count.split(' ', maxsplit=1)
                max_counts[color] = max(int(n), max_counts[color])
        
        prod = 1
        for v in max_counts.values():
            prod *= v
        
        s += prod
    
    return s


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2023_day02_input.txt') as f:
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
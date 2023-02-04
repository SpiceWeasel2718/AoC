def part1(input_text: str):
    from collections import Counter
    
    twos, threes = 0, 0

    for line in input_text.splitlines():
        counts = Counter(line)
        values = set(counts.values())
        twos += (2 in values)
        threes += (3 in values)
    
    return twos * threes
            

def part2(input_text: str):
    boxes = input_text.splitlines()
    id_length = len(boxes[0])

    for i, box1 in enumerate(boxes):
        for box2 in boxes[i+1:]:
            shared = []
            for c1, c2 in zip(box1, box2):
                if c1 == c2:
                    shared.append(c1)
            if len(shared) == id_length - 1:
                return ''.join(shared)


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2018_day02_input.txt') as f:
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
def part1(input_text: str):
    def calc_hash(string):
        current_value = 0
        for c in string:
            current_value = ((current_value + ord(c)) * 17) % 256
        return current_value
    
    return sum(calc_hash(s) for s in input_text.strip().split(','))


def part2(input_text: str):
    def calc_hash(string):
        current_value = 0
        for c in string:
            current_value = ((current_value + ord(c)) * 17) % 256
        return current_value
    
    boxes = []
    for __ in range(256):
        # Python dicts preserve insertion order nowadays
        boxes.append({})

    for step in input_text.strip().split(','):
        if step.endswith('-'):
            label = step[:-1]
            h = calc_hash(label)
            
            if label in boxes[h]:
                del boxes[h][label]
        else:
            label = step[:-2]
            f = int(step[-1])
            h = calc_hash(label)

            boxes[h][label] = f
    
    s = 0

    for bn, box in enumerate(boxes, start=1):
        for sn, f in enumerate(box.values(), start=1):
            s += bn * sn * f
    
    return s


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2023_day15_input.txt') as f:
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
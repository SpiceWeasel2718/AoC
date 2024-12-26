def part1(input_text: str):
    import re
    
    pairs = re.findall(r'mul\((\d+),(\d+)\)', input_text)

    return sum(int(i1) * int(i2) for i1, i2 in pairs)


def part2(input_text: str):
    import re
    
    prog = re.compile(r'mul\((\d+),(\d+)\)')
    pairs = []
    
    for chunk in input_text.split('do()'):
        idx = chunk.find("don't()")
        pairs.extend(re.findall(prog, chunk[:idx]))

    return sum(int(i1) * int(i2) for i1, i2 in pairs)


if __name__ == '__main__':
    from pathlib import Path

    current_file = Path(__file__)
    input_file = current_file.parent / 'input_files' / (current_file.stem + '_input.txt')
    
    with open(input_file) as fp:
        input_text = fp.read()

    print('Part 1:')
    print(p1 := part1(input_text))
    print('Part 2:')
    print(part2(input_text))
def part1(input_text: str):
    list1 = []
    list2 = []
    
    for line in input_text.splitlines():
        i1, i2 = line.split()
        list1.append(int(i1))
        list2.append(int(i2))

    return sum(abs(i1 - i2) for i1, i2 in zip(sorted(list1), sorted(list2)))


def part2(input_text: str):
    from collections import Counter
    
    left_list = []
    right_dict = Counter()
    
    for line in input_text.splitlines():
        i1, i2 = line.split()
        left_list.append(i1)
        right_dict[i2] += 1

    return sum(int(i) * right_dict[i] for i in left_list)


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
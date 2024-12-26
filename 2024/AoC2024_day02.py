def part1(input_text: str):
    from itertools import pairwise
    
    s = 0
    
    for line in input_text.splitlines():
        levels = [int(i) for i in line.split()]
        
        # if decreasing, reverse sequence so it's increasing
        if levels[1] < levels[0]:
            levels.reverse()
        
        for i1, i2 in pairwise(levels):
            if not (1 <= i2 - i1 <= 3):
                break
        else:
            s += 1

    return s


def part2(input_text: str):
    from itertools import pairwise
    
    def check_seq(seq):
        if len(seq) < 2:
            return True
        else:
            return all(1 <= i2 - i1 <= 3 for i1, i2 in pairwise(seq))
    
    s = 0
    
    for line in input_text.splitlines():
        levels = [int(i) for i in line.split()]
        
        # if decreasing, reverse sequence so it's increasing
        if sum(i1 < i2 for i1, i2 in pairwise(levels[:4])) < 2:
            levels.reverse()
        
        deltas = [i2 - i1 for i1, i2 in pairwise(levels)]
        
        for idx, d in enumerate(deltas):
            if not (1 <= d <= 3):
                l_bad = idx
                break
        else:
            s += 1
            continue
        
        idx_max = len(deltas) - 1
        
        for idx, d in enumerate(reversed(deltas)):
            if not (1 <= d <= 3):
                r_bad = idx_max - idx
                break
        
        if l_bad + 1 == r_bad and 1 <= deltas[l_bad] + deltas[r_bad] <= 3:
            s += 1
        elif l_bad == r_bad and (
            l_bad == 0 or \
            l_bad == idx_max or \
            1 <= deltas[l_bad-1] + deltas[l_bad] <= 3 or \
            1 <= deltas[l_bad] + deltas[l_bad+1] <= 3
        ):
            s += 1
        
    return s

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
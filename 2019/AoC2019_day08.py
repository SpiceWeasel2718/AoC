def part1(input_text):
    from collections import Counter
    input_text = input_text[0]
    counts = [Counter(input_text[i:i+150]) for i in range(0, len(input_text), 150)]
    m = min(counts, key=lambda a: a['0'])
    return m['1']*m['2']
    

def part2(input_text):
    input_text = input_text[0]
    image = []
    for i in range(150):
        for c in input_text[i::150]:
            if c != '2':
                image.append(c if c == '1' else ' ')
                break
        else:
            image.append('2')
    return '\n' + '\n'.join([''.join(image[i:i+25]) for i in range(0, 150, 25)])


if __name__ == '__main__':
    from pathlib import Path
    with open(next(Path().glob('**/AoC2019_day08_input.txt'))) as f:
        input_text = f.read().split('\n')

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    #print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    #print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
def part1(input_text):
    coordinates, fold_instructions = input_text.split('\n\n')

    dots = set(
        complex(*[int(n) for n in line.split(',')]) 
        for line in coordinates.splitlines()
    )

    for line in fold_instructions.splitlines():
        temp, n = line.split('=')
        dimension = temp[-1]
        value = int(n)

        if dimension == "x":
            for pos in list(dots):
                if pos.real > value:
                    dots.remove(pos)
                    dots.add(pos - 2 * (pos.real - value))
        else:
            for pos in list(dots):
                if pos.imag > value:
                    dots.remove(pos)
                    dots.add(pos - 2j * (pos.imag - value))

    return len(dots)


def part2(input_text):
    coordinates, fold_instructions = input_text.split('\n\n')

    dots = set(
        complex(*[int(n) for n in line.split(',')]) 
        for line in coordinates.splitlines()
    )

    for line in fold_instructions.splitlines():
        temp, n = line.split('=')
        dimension = temp[-1]
        value = int(n)

        if dimension == "x":
            max_x = value

            for pos in list(dots):
                if pos.real > value:
                    dots.remove(pos)
                    dots.add(pos - 2 * (pos.real - value))
        else:
            max_y = value

            for pos in list(dots):
                if pos.imag > value:
                    dots.remove(pos)
                    dots.add(pos - 2j * (pos.imag - value))

    return '\n' + '\n'.join(
        ''.join(
            ('#' if complex(x, y) in dots else ' ') 
            for x in range(max_x)
        )
        for y in range(max_y)
    )


if __name__ == '__main__':
    with open('./input_files/AoC2021_day13_input.txt') as f:
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
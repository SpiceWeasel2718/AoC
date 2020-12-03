def part1(input_text):
    from intcode import IntComp

    computer = IntComp(input_text)
    computer.program[1] = 12
    computer.program[2] = 2
    computer.execute()

    return computer.program[0]


def part2(input_text):
    from intcode import IntComp

    computer = IntComp(input_text)

    for i in range(len(computer.program)):
        for j in range(len(computer.program)):
            computer.reset()
            computer.program[1] = i
            computer.program[2] = j
            computer.execute()

            if computer.program[0] == 19690720:
                return 100 * i + j


if __name__ == "__main__":
    import timeit

    input_text = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,1,13,23,27,1,6,27,31,1,31,10,35,1,35,6,39,1,39,13,43,2,10,43,47,1,47,6,51,2,6,51,55,1,5,55,59,2,13,59,63,2,63,9,67,1,5,67,71,2,13,71,75,1,75,5,79,1,10,79,83,2,6,83,87,2,13,87,91,1,9,91,95,1,9,95,99,2,99,9,103,1,5,103,107,2,9,107,111,1,5,111,115,1,115,2,119,1,9,119,0,99,2,0,14,0'

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
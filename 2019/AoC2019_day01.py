def part1(input_text):
    return sum((int(line) // 3) - 2 for line in input_text)

def part2(self):
    def fuel_needed(mass):
        mass = (mass // 3) - 2
        while mass > 0:
            yield mass
            mass = (mass // 3) - 2
    
    return sum(sum(fuel_needed(int(line))) for line in input_text)


if __name__ == "__main__":
    import timeit

    with open("input_files/AoC2019_day01_input.txt") as f:
        input_text = f.read().split('\n')

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
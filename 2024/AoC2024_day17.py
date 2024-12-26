def part1(input_text: str):
    import re

    registers_text, program_text = input_text.split("\n\n")
    registers = [int(n) for n in re.findall(r"\d+", registers_text)]
    program = [int(n) for n in re.findall(r"\d", program_text)]

    combo = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: registers[0],
        5: registers[1],
        6: registers[2],
    }

    ptr = 0
    out = []

    while ptr < len(program):
        inst, op = program[ptr], program[ptr + 1]

        match inst:
            case 0:  # adv
                combo[4] = combo[4] // (2 << (combo[op] - 1))
            case 1:  # bxl
                combo[5] = combo[5] ^ op
            case 2:  # bst
                combo[5] = combo[op] % 8
            case 3:  # jnz
                if combo[4]:
                    ptr = op
                    continue
            case 4:  # bxc
                combo[5] = combo[5] ^ combo[6]
            case 5:  # out
                out.append(combo[op] % 8)
            case 6:  # bdv
                combo[5] = combo[4] // (2 << (combo[op] - 1))
            case 7:  # cdv
                combo[6] = combo[4] // (2 << (combo[op] - 1))

        ptr += 2

    return ",".join(str(n) for n in out)


def part2(input_text: str):
    import re

    registers_text, program_text = input_text.split("\n\n")
    registers = [int(n) for n in re.findall(r"\d+", registers_text)]
    program = [int(n) for n in re.findall(r"\d", program_text)]

    def run_program(a):
        combo = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: a,
            5: registers[1],
            6: registers[2],
        }

        ptr = 0
        out = []

        while ptr < len(program):
            inst, op = program[ptr], program[ptr + 1]

            match inst:
                case 0:  # adv
                    combo[4] = (
                        combo[4]
                        if combo[op] == 0
                        else combo[4] // (2 << (combo[op] - 1))
                    )
                case 1:  # bxl
                    combo[5] = combo[5] ^ op
                case 2:  # bst
                    combo[5] = combo[op] % 8
                case 3:  # jnz
                    if combo[4]:
                        ptr = op
                        continue
                case 4:  # bxc
                    combo[5] = combo[5] ^ combo[6]
                case 5:  # out
                    out.append(combo[op] % 8)
                case 6:  # bdv
                    combo[5] = (
                        combo[4]
                        if combo[op] == 0
                        else combo[4] // (2 << (combo[op] - 1))
                    )
                case 7:  # cdv
                    combo[6] = (
                        combo[4]
                        if combo[op] == 0
                        else combo[4] // (2 << (combo[op] - 1))
                    )

            ptr += 2

        return out

    # My program's output increases in length by 1 at every power of 8,
    # and digits don't change for at least a power of 8 dependent on their index
    power = len(program) - 1
    a = 8**power

    def find_match(a, power):
        if power == -1:
            return a

        while run_program(a)[power] != program[power]:
            a += 8**power

        while run_program(a)[power:] == program[power:]:
            if b := find_match(a, power - 1):
                return b
            else:
                a += 8**power

        return False

    return find_match(a, power)


if __name__ == "__main__":
    from pathlib import Path

    current_file = Path(__file__)
    input_file = (
        current_file.parent / "input_files" / (current_file.stem + "_input.txt")
    )

    with open(input_file) as fp:
        input_text = fp.read()

    print("Part 1:")
    print(p1 := part1(input_text))
    print("Part 2:")
    print(part2(input_text))

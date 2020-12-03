part = 1

with open("input_files/AoC2016_day25_input.txt") as f:
    input_text = f.read().split("\n")


def cpy(args, pos):
    registers[args[1]] = args[0] if type(args[0]) is int else registers[args[0]]
    return pos + 1


def inc(arg, pos):
    registers[arg[0]] += 1
    return pos + 1


def dec(arg, pos):
    registers[arg[0]] -= 1
    return pos + 1


def jnz(args, pos):
    return pos + args[1] if (args[0] if type(args[0]) is int else registers[args[0]]) != 0 else pos + 1


operations = {
    "cpy": cpy,
    "inc": inc,
    "dec": dec,
    "jnz": jnz,
    "out": "out"
}

instructions = []

for line in input_text:
    temp = line.split()
    instructions.append([operations[temp[0]]] + [arg if arg.isalpha() else int(arg) for arg in temp[1:]])

a = 0

while True:
    registers = {"a": a,
                 "b": 0,
                 "c": 0,
                 "d": 0}

    expected_transmission = 0
    pos = 0

    print(f'\rTesting {a}...', end='')

    while pos < len(input_text):
        if instructions[pos][0] != 'out':
            pos = instructions[pos][0](instructions[pos][1:], pos)
        else:
            if expected_transmission == registers[instructions[pos][1]]:
                expected_transmission = (expected_transmission + 1) % 2
                pos += 1
            else:
                break

    a += 1









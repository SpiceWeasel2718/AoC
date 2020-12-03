with open("input_files/AoC2016_day12_input.txt") as f:
    input_text = f.read().split("\n")

registers = {"a": 0,
             "b": 0,
             "c": 1,
             "d": 0}


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
    "jnz": jnz
}

instructions = []

for line in input_text:
    temp = line.split()
    instructions.append([operations[temp[0]]] + [arg if arg.isalpha() else int(arg) for arg in temp[1:]])

pos = 0

while pos < len(input_text):
    pos = instructions[pos][0](instructions[pos][1:], pos)

print(registers["a"])







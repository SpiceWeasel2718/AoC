f = open("input_files/AoC2016_day23_input.txt")
input_text = f.read().split("\n")
f.close()

registers = {"a": 12,
             "b": 0,
             "c": 0,
             "d": 0}
instructions = [line.split() for line in input_text]
pos = 0

def interpret(string):
    return registers[string] if string.isalpha() else int(string)


def inc(reg, pos):
    registers[reg[0]] += 1
    return pos + 1

def dec(reg, pos):
    registers[reg[0]] -= 1
    return pos + 1

def cpy(args, pos):
    if args[1].isalpha():
        registers[args[1]] = interpret(args[0])
    return pos + 1

def tgl(arg, pos):
    target = pos + interpret(arg[0])
    if 0 <= target < len(instructions):
        if len(instructions[target]) == 2:
            instructions[target][0] = "dec" if instructions[target][0] == "inc" else "inc"
        else:
            instructions[target][0] = "cpy" if instructions[target][0] == "jnz" else "jnz"
    return pos + 1

def jnz(args, pos):
    if interpret(args[0]) != 0:
        return pos + interpret(args[1])
    return pos + 1


ops = {
    "inc": inc,
    "dec": dec,
    "cpy": cpy,
    "tgl": tgl,
    "jnz": jnz
}


while pos < len(input_text):
    pos = ops[instructions[pos][0]](instructions[pos][1:], pos)

print(registers["a"])






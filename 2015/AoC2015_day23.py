import math as m

f = open("input_files/AoC2015_day23_input.txt")
input_text = f.read().split("\n")
f.close()

instructions = [line.split() for line in input_text]
registers = {"a": 1, "b": 0}
ind = 0

while ind < len(instructions):
    inst = instructions[ind]

    if inst[0] == "hlf":
        registers[inst[1]] = m.floor(registers[inst[1]] / 2)
        ind += 1
    elif inst[0] == "tpl":
        registers[inst[1]] *= 3
        ind += 1
    elif inst[0] == "inc":
        registers[inst[1]] += 1
        ind += 1
    elif inst[0] == "jmp":
        ind += int(inst[1])
    elif inst[0] == "jie":
        if registers[inst[1].rstrip(",")] % 2 == 0:
            ind += int(inst[2])
        else:
            ind += 1
    elif inst[0] == "jio":
        if registers[inst[1].rstrip(",")] == 1:
            ind += int(inst[2])
        else:
            ind += 1
    else:
        break

print(registers["a"], registers["b"])




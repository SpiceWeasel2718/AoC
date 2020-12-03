f = open("input_files/AoC2015_day08_input.txt")
inputs = f.read().split("\n")
f.close()

total = 0

"""
Part 1

for line in inputs:
    while "\\\\" in line:
        line = "".join(line.rsplit("\\\\", 1))
        total += 1
    while "\\\"" in line:
        line = "".join(line.rsplit("\\\"", 1))
        total += 1
    while "\\x" in line:
        line = "".join(line.rsplit("\\x", 1))
        total += 3

    total += 2
"""

for line in inputs:
    for c in line:
        if c == "\"":
            total += 1
        elif c == "\\":
            total += 1

    total += 2

print(total)




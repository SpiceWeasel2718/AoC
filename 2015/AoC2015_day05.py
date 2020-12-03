f = open("input_files/AoC2015_day05_input.txt")
inputs = f.readlines()
f.close()

nice = 0

"""
Part 1

for string in inputs:
    if any(x in string for x in ("ab", "cd", "pq", "xy")):
        continue

    repeat = False
    vowels = 0

    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            repeat = True
        if string[i] in "aeiou":
            vowels += 1

    if vowels > 2 and repeat:
        nice += 1
"""

for string in inputs:
    pair = False
    repeat = False

    for i in range(len(string)-2):
        if string[i:i+2] in string[i+2:]:
            pair = True
        if string[i] == string[i+2]:
            repeat = True

    if pair and repeat:
        nice += 1

print(nice)


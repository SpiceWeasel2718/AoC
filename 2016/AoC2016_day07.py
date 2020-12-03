import re

f = open("input_files/AoC2016_day07_input.txt")
input_text = f.read().split("\n")
f.close()


def abba(string):
    for i in range(1, len(string)-2):
        if string[i-1] != string[i] and string[i-1:i+1] == string[i+2]+string[i+1]:
            return True
    return False


def find_abas(string):
    abas = []
    for i in range(len(string)-2):
        if string[i+2] == string[i] and string[i+1] != string[i] and string[i:i+3] not in abas:
            abas.append(string[i:i+3])
    return abas


def bab(string):
    return string[1] + string[0] + string[1]


valid_ips = []

"""
# Part 1

for line in input_text:
    data = re.split(r"[][]", line)
    valid = False
    for i in range(len(data)):
        if abba(data[i]):
            if i % 2 == 1:
                valid = False
                break
            else:
                valid = True

    if valid:
        valid_ips.append(data)
"""

for line in input_text:
    data = re.split(r"[][]", line)
    abas = []
    for i in range(0, len(data), 2):
        abas += find_abas(data[i])
    valid = False
    for i in range(1, len(data), 2):
        for aba in abas:
            if bab(aba) in data[i]:
                valid = True
                break
        if valid:
            break

    if valid:
        valid_ips.append(data)

print(len(valid_ips))

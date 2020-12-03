f = open("input_files/AoC2016_day21_input.txt")
input_text = f.read().split("\n")
f.close()

"""
# Part 1

password = [c for c in "abcdefgh"]

for line in input_text:
    instruct = line.split()

    if line.startswith("swap p"):
        temp = [int(instruct[2]), int(instruct[5])]
        c = password[temp[0]]
        password[temp[0]] = password[temp[1]]
        password[temp[1]] = c
    elif line.startswith("swap l"):
        temp = [instruct[2], instruct[5]]
        for i in range(len(password)):
            if password[i] == temp[0]:
                password[i] = temp[1]
            elif password[i] == temp[1]:
                password[i] = temp[0]
    elif line.startswith("rotate l"):
        temp = int(instruct[2])
        password = password[temp:] + password[:temp]
    elif line.startswith("rotate r"):
        temp = int(instruct[2])
        password = password[-temp:] + password[:-temp]
    elif line.startswith("rotate b"):
        ind = password.index(instruct[6])
        temp = (1 + ind + (1 if ind >= 4 else 0)) % 8
        password = password[-temp:] + password[:-temp]
    elif line.startswith("re"):
        ind = [int(instruct[2]), int(instruct[4])+1]
        temp = password[ind[0]: ind[1]]
        temp.reverse()
        password = password[:ind[0]] + temp + password[ind[1]:]
    else:
        c = password.pop(int(instruct[2]))
        password.insert(int(instruct[5]), c)

print("".join(password))
"""

input_text.reverse()
scramble = [c for c in "fbgdceah"]
pos_map = [1, 1, 6, 2, 7, 3, 0, 4]

for line in input_text:
    instruct = line.split()

    if line.startswith("swap p"):
        temp = [int(instruct[2]), int(instruct[5])]
        c = scramble[temp[0]]
        scramble[temp[0]] = scramble[temp[1]]
        scramble[temp[1]] = c
    elif line.startswith("swap l"):
        temp = [instruct[2], instruct[5]]
        for i in range(len(scramble)):
            if scramble[i] == temp[0]:
                scramble[i] = temp[1]
            elif scramble[i] == temp[1]:
                scramble[i] = temp[0]
    elif line.startswith("rotate l"):
        temp = int(instruct[2])
        scramble = scramble[-temp:] + scramble[:-temp]
    elif line.startswith("rotate r"):
        temp = int(instruct[2])
        scramble = scramble[temp:] + scramble[:temp]
    elif line.startswith("rotate b"):
        ind = scramble.index(instruct[6])
        temp = pos_map[ind]
        scramble = scramble[temp:] + scramble[:temp]
    elif line.startswith("re"):
        ind = [int(instruct[2]), int(instruct[4])+1]
        temp = scramble[ind[0]: ind[1]]
        temp.reverse()
        scramble = scramble[:ind[0]] + temp + scramble[ind[1]:]
    else:
        c = scramble.pop(int(instruct[5]))
        scramble.insert(int(instruct[2]), c)

print("".join(scramble))





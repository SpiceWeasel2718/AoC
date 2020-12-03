import hashlib

passcode = "veumntbg"


def open_doors(state):
    h = hashlib.md5((passcode + state[1]).encode("utf-8")).hexdigest()
    x = state[0][0]
    y = state[0][1]
    options = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
    directions = ["U", "D", "L", "R"]

    output = []

    for i in range(4):
        if -1 not in options[i] and 4 not in options[i] and h[i].isalpha() and h[i] != "a":
            output.append([options[i], state[1] + directions[i]])

    return output


states = [[(0, 0), ""]]

while len(states) > 0:
    for i in range(len(states)):
        for state in open_doors(states.pop(0)):
            if state[0] == (3, 3):
                print(len(state[1]), state)
            else:
                states.append(state)







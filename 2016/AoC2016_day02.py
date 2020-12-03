f = open("input_files/AoC2016_day02_input.txt")
input_text = f.read().split("\n")
f.close()

keypad_part1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
keypad = [
    ["","",1,"",""],
    ["",2,3,4,""],
    [5,6,7,8,9],
    ["","A", "B", "C",""],
    ["","","D","",""]
]

code = []
ind = [2,0]

for line in input_text:
    for d in line:
        if d == "U":
            if abs(2-(ind[0]-1)) + abs(2-ind[1]) < 3:
                ind[0] -= 1
        elif d == "D":
            if abs(2-(ind[0]+1)) + abs(2-ind[1]) < 3:
                ind[0] += 1
        elif d == "R":
            if abs(2-ind[0]) + abs(2-(ind[1]+1)) < 3:
                ind[1] += 1
        elif d == "L":
            if abs(2-ind[0]) + abs(2-(ind[1]-1)) < 3:
                ind[1] -= 1
    code.append(keypad[ind[0]][ind[1]])

print(code)

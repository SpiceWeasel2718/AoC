f = open("input_files/AoC2016_day08_input.txt")
input_text = f.read().split("\n")
f.close()

screen = [(50*[0]).copy() for i in range(6)]

for line in input_text:
    if line.startswith("rect"):
        data = line[5:].split("x")
        for r in range(int(data[1])):
            for c in range(int(data[0])):
                screen[r][c] = 1
    elif line.startswith("rotate row"):
        data = line[13:].split(" by ")
        row = int(data[0])
        shift = int(data[1])
        before = screen[row].copy()
        for i in range(len(before)):
            screen[row][i] = before[i-shift]
    elif line.startswith("rotate column"):
        data = line[16:].split(" by ")
        col = int(data[0])
        shift = int(data[1])
        before = [screen[r][col] for r in range(6)]
        for i in range(len(before)):
            screen[i][col] = before[i-shift]


for s in screen:
    print("".join(["#" if c else " " for c in s]))

print(sum([sum(row) for row in screen]))

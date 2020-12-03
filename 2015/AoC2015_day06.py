f = open("input_files/AoC2015_day06_input.txt")
inputs = f.readlines()
f.close()


def turn_on(node):
    return node + 1
    #return 1


def turn_off(node):
    return max(node - 1, 0)
    #return 0


def toggle(node):
    return node + 2
    #return (node + 1) % 2


grid = []
for i in range(1000):
    grid.append(1000*[0])

for line in inputs:
    if line.startswith("turn on"):
        coords = [c.split(",") for c in line[8:].rstrip().split(" through ")]
        op = turn_on
    elif line.startswith("turn off"):
        coords = [c.split(",") for c in line[9:].rstrip().split(" through ")]
        op = turn_off
    elif line.startswith("toggle"):
        coords = [c.split(",") for c in line[7:].rstrip().split(" through ")]
        op = toggle

    for x in range(int(coords[0][0]), int(coords[1][0])+1):
        for y in range(int(coords[0][1]), int(coords[1][1])+1):
            grid[x][y] = op(grid[x][y])

total = 0

for row in grid:
    total += sum(row)

print(total)


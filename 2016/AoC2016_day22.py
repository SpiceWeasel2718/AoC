f = open("input_files/AoC2016_day22_input.txt")
input_text = f.read().split("\n")
f.close()


class Node:
    def __init__(self, coords, size, used, avail, use_p):
        self.coords = coords
        self.size = size
        self.used = used
        self.avail = avail
        self.use_p = use_p


nodes = []
dims = [0, 0]

for line in input_text[2:]:
    data = line.split()
    coords = [int(c[1:]) for c in (data[0].split("-"))[1:]]
    for i in range(2):
        dims[i] = max(coords[i]+1, dims[i])
    nodes.append(Node(coords, int(data[1][:-1]), int(data[2][:-1]), int(data[3][:-1]), int(data[4][:-1])))


# Most are 64T-73T used, all but one are >= 64T
# all but one are <30T avail

"""
# Part 1

viable_pairs = []

for n in nodes:
    if n.used == 0:
        continue
    for n2 in nodes:
        if n != n2 and n.used <= n2.avail:
            viable_pairs.append((n, n2))

print(len(viable_pairs))
"""

grid = [list(range(dims[1])).copy() for i in range(dims[0])]
graph = grid.copy()

for n in nodes:
    grid[n.coords[0]][n.coords[1]] = n

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y].used > 99:
            graph[x][y] = "#"
        elif grid[x][y].used == 0:
            graph[x][y] = "O"
        elif grid[x][y].used < 99:
            graph[x][y] = "-"

for g in graph:
    print(g)

# 34 moves to shift the target data one space left (up in the print result), leaving the open space to the right of (below) it
# 5 moves to shift the target data one node left from this position; 35 spaces left to move
# 209 total




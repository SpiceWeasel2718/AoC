from copy import deepcopy

f = open("input_files/AoC2015_day18_input.txt")
input_text = f.read().split("\n")
f.close()

grid = []

for i in range(len(input_text)):
    grid.append([])
    for c in input_text[i]:
        grid[i].append(1 if c == "#" else 0)

grid[99][0] = 1

def update_grid(grid):
    new_grid = deepcopy(grid)
    num_rows = len(grid)
    num_cols = len(grid[0])

    for i in range(num_rows):
        topedge = True if i == 0 else False
        bottomedge = True if i == num_rows-1 else False
        for j in range(num_cols):
            leftedge = True if j == 0 else False
            rightedge = True if j == num_cols - 1 else False

            if any([topedge and leftedge, topedge and rightedge, bottomedge and leftedge, bottomedge and rightedge]):
                continue

            nbrs = 0

            if not topedge:
                nbrs += grid[i - 1][j]
                if not leftedge:
                    nbrs += grid[i - 1][j - 1]
                if not rightedge:
                    nbrs += grid[i - 1][j + 1]
            if not bottomedge:
                nbrs += grid[i + 1][j]
                if not leftedge:
                    nbrs += grid[i + 1][j - 1]
                if not rightedge:
                    nbrs += grid[i + 1][j + 1]
            if not leftedge:
                nbrs += grid[i][j - 1]
            if not rightedge:
                nbrs += grid[i][j + 1]

            if grid[i][j] == 1 and nbrs not in [2, 3]:
                new_grid[i][j] = 0
            if grid[i][j] == 0 and nbrs == 3:
                new_grid[i][j] = 1

    return new_grid


for i in range(100):
    grid = update_grid(grid)

print(sum([sum(row) for row in grid]))


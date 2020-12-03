input_const = 1364


def is_wall(coords):
    x = coords[0]
    y = coords[1]
    total = 0
    for num in str(bin(x*x + 3*x + 2*x*y + y + y*y + input_const)):
        if num == "1":
            total += 1
    return total % 2


maze = []

for i in range(50):
    maze.append([])
    for j in range(50):
        maze[i].append(1 if is_wall((i, j)) else 0)

# maze[x][y] = (x, y)

paths = [
    [(0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (2, 4), (2, 5), (2, 6)]
]

"""
# Part 1

done = False

while not done:
    for i in range(len(paths)):
        path = paths.pop(0)
        x = path[-1][0]
        y = path[-1][1]

        if (x, y) == (31, 39):
            done = True
            print(len(path))
            break

        for nbr in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
            if maze[nbr[0]][nbr[1]] == 1 or nbr == path[-2] or nbr[0] < 0 or nbr[1] < 0 or nbr in path:
                continue
            else:
                paths.append(path + [nbr])
"""

locations = [(1, 1)] + paths[0]

while len(paths[0]) < 50:
    for i in range(len(paths)):
        path = paths.pop(0)
        x = path[-1][0]
        y = path[-1][1]

        if (x, y) == (31, 39):
            done = True
            print(len(path))
            break

        for nbr in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
            if maze[nbr[0]][nbr[1]] == 1 or nbr == path[-2] or nbr[0] < 0 or nbr[1] < 0 or nbr in path:
                continue
            else:
                paths.append(path + [nbr])
                if nbr not in locations:
                    locations.append(nbr)

print(len(locations))









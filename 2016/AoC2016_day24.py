import math
import itertools

part = 2

with open("input_files/AoC2016_day24_input.txt") as f:
    input_text = f.read().split("\n")

ducts = [[c for c in line] for line in input_text]

area_width, area_length = len(ducts), len(ducts[0])

points = {}

for i in range(area_width):
    for j in range(area_length):
        if ducts[i][j].isdigit():
            points.update({ducts[i][j]: (i, j)})

point_names = tuple(points.keys())


def get_valid_neighbors(p):
    return [q for q in ((p[0]+1, p[1]), (p[0]-1, p[1]), (p[0], p[1]+1), (p[0], p[1]-1)) if ducts[q[0]][q[1]] != '#']


# construct graph
graph = {}

for i in range(area_width):
    for j in range(area_length):
        if ducts[i][j] != '#':
            neighbors = get_valid_neighbors((i, j))

            if len(neighbors) != 2 or ducts[i][j].isdigit():
                graph[(i, j)] = {}

                for direction in neighbors:
                    current = direction
                    prev = (i, j)
                    dist = 1

                    adjacents = get_valid_neighbors(current)
                    while len(adjacents) == 2 and ducts[current[0]][current[1]] == '.':
                        adjacents.remove(prev)
                        prev = current
                        current = adjacents[0]
                        dist += 1
                        adjacents = get_valid_neighbors(current)

                    graph[(i, j)][current] = dist


# Dijkstra
point_dists = {p: dict.fromkeys(point_names, 0) for p in point_names}

for point_name in point_names:
    unvisited = set(graph.keys())
    visited = set()
    node_distances = dict.fromkeys(graph.keys(), math.inf)
    node_distances[points[point_name]] = 0

    while len(unvisited) > 0:
        current_node = min(unvisited, key=lambda node: node_distances[node])

        neighbors = graph[current_node]
        for neighbor in neighbors:
            node_distances[neighbor] = min(node_distances[neighbor], node_distances[current_node] + neighbors[neighbor])

        visited.add(current_node)
        unvisited.remove(current_node)

    for target in point_names:
        point_dists[point_name][target] = node_distances[points[target]]

for p in point_dists:
    print(p, point_dists[p])

# Traveling salesman nearest neighbor
# part 1
if part == 1:
    unvisited = set(point_names)
    unvisited.remove('0')
    route = ['0']
    dist = 0

    while len(unvisited) > 0:
        nearest = min(unvisited, key=lambda p: point_dists[route[-1]][p])
        dist += point_dists[route[-1]][nearest]
        route.append(nearest)
        unvisited.remove(nearest)

    print(dist, route)

# part 2
if part == 2:
    unvisited = set(point_names)
    unvisited.remove('0')
    min_dist = math.inf
    route = []

    for perm in itertools.permutations(unvisited):
        current = '0'
        dist = 0
        for p in perm:
            dist += point_dists[current][p]
            current = p

        dist += point_dists[current]['0']
        if dist < min_dist:
            min_dist = dist
            route = ['0'] + list(perm) + ['0']

    print(min_dist, route)





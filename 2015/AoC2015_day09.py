f = open("input_files/AoC2015_day09_input.txt")
inputs = f.read().split("\n")
f.close()

graph = {}
shortest_path = 0
longest_path = 0

for line in inputs:
    data = line.split(" = ")
    dist = int(data[1])
    shortest_path += dist
    cities = data[0].split(" to ")
    if not cities[0] in graph.keys():
        graph.update({cities[0]: {}})
    if not cities[1] in graph.keys():
        graph.update({cities[1]: {}})
    graph[cities[0]].update({cities[1]: dist})
    graph[cities[1]].update({cities[0]: dist})

city_list = list(graph.keys())
n_cities = len(city_list)

paths = [[city_list[0]]]

for i in range(len(city_list)-1):
    for j in range(len(paths)):
        path = paths.pop(0)
        for city in city_list:
            if city not in path:
                paths.append(path + [city])

for path in paths:
    dists = n_cities*[0]
    for i in range(len(path)-1):
        for j in range(len(dists)):
            dists[j] += graph[path[(i+j)%n_cities]][path[(i+j+1)%n_cities]]
    shortest_path = min(shortest_path, min(dists))
    longest_path = max(longest_path, max(dists))

print(shortest_path)
print(longest_path)

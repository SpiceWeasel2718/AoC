f = open("input_files/AoC2016_day01_input.txt")
input_text = f.read().split("\n")
f.close()

directions = input_text[0].split(", ")

coords = [0, 0]
orientation = [0, 1]
locations = []
done = False

for d in directions:
    dist = int(d[1:])
    if d[0] == "L":
        orientation = [-orientation[1], orientation[0]]
    elif d[0] == "R":
        orientation = [orientation[1], -orientation[0]]

    for j in range(dist):
        coords = [coords[i] + orientation[i] for i in range(2)]
        if coords in locations:
            print(sum(coords))
            done = True
            break
        else:
            locations.append(coords.copy())

    if done:
        break

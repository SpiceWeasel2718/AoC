f = open("input_files/AoC2015_day16_input.txt")
input_text = f.read().split("\n")
f.close()

target = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

properties = list(target.keys())

aunts = []

for line in input_text:
    aunt = {}
    data = [s.rstrip(",:") for s in line.split()]
    for i in range(2, len(data)-1):
        if data[i] in properties:
            aunt.update({data[i]: int(data[i+1])})
    aunts.append(aunt)

for i in range(len(aunts)):
    match = True
    for prop in aunts[i].keys():
        if prop in ["cats", "trees"] and aunts[i][prop] <= target[prop]:
            match = False
        if prop in ["pomeranians", "goldfish"] and aunts[i][prop] >= target[prop]:
            match = False
        if prop not in ["cats", "trees", "pomeranians", "goldfish"] and aunts[i][prop] != target[prop]:
            match = False

    if match:
        print(i+1)


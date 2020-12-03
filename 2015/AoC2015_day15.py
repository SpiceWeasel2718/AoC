from itertools import combinations

f = open("input_files/AoC2015_day15_input.txt")
input_text = f.read().split("\n")
f.close()

total_tsp = 100

partitions = combinations(range(total_tsp), len(input_text)-1)

ingredients_dict = {}

for line in input_text:
    data = line.split()
    ingredients_dict.update({data[0][:-1]: {"capacity": int(data[2][:-1]), "durability": int(data[4][:-1]),
                                       "flavor": int(data[6][:-1]), "texture": int(data[8][:-1]),
                                       "calories": int(data[10])}})

properties = ["capacity", "durability", "flavor", "texture"]
ingredients = list(ingredients_dict.keys())


def score(partition):
    temp = [0] + list(partition) + [total_tsp]
    amounts = []
    for i in range(1, len(temp)):
        amounts.append(temp[i] - temp[i-1])

    calories = 0

    for i in range(len(ingredients)):
        calories += ingredients_dict[ingredients[i]]["calories"] * amounts[i]

    if calories != 500:
        return 0

    scores = len(properties)*[0]

    for i in range(len(properties)):
        for j in range(len(ingredients)):
            scores[i] += ingredients_dict[ingredients[j]][properties[i]] * amounts[j]

    if any([s < 1 for s in scores]):
        return 0
    else:
        score = 1
        for s in scores:
            score *= s
        return score


total = 0

for partition in partitions:
    s = score(partition)
    total = max(total, s)

print(total)





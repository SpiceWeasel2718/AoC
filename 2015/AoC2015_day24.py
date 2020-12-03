from itertools import combinations

f = open("input_files/AoC2015_day24_input.txt")
input_text = f.read().split("\n")
f.close()

weights = [int(n) for n in input_text]
# note all weights are odd

target_weight = int(sum(weights)/4)

max_size = 1
while sum(weights[:max_size+1]) < target_weight:
    max_size += 1

min_size = 1
while sum(weights[-min_size:]) < target_weight:
    min_size += 1

selections = []

for n in range(min_size, max_size+1):
    if n % 2 != target_weight % 2:
        continue
    for sel in combinations(weights, n):
        if sum(sel) == target_weight:
            selections.append(sel)
    if selections:
        break


def product(l):
    prod = 1
    for elem in l:
        prod *= elem
    return prod


print(min([product(sel) for sel in selections]))


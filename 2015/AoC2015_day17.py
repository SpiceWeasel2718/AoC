from itertools import combinations


containers = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]
containers.sort()

min_num = 1
max_num = 1

while sum(containers[-min_num:]) < 150:
    min_num += 1
while sum(containers[:max_num]) < 150:
    max_num += 1

solutions = []

for n in range(min_num, max_num):
    selections = combinations(containers, n)
    for sel in selections:
        if sum(sel) == 150:
            solutions.append(sel)

total = 0
for sol in solutions:
    if len(sol) == min_num:
        total += 1

print(total)


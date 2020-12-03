f = open("input_files/AoC2016_day20_input.txt")
input_text = f.read().split("\n")
f.close()

intervals = [[int(p) for p in line.split("-")] for line in input_text]
intervals.sort(key=lambda a: a[0])

"""
# Part 1

ub = intervals[0][1] + 1
ind = 1

while intervals[ind][0] <= ub:
    ub = max(ub, intervals[ind][1] + 1)
    ind += 1

print(ub)
"""

complement = [[0, 4294967295]]

for J in intervals:
    to_remove = []
    for i in range(len(complement)):
        if complement[i][1] < J[0]:
            continue
        elif J[1] < complement[i][0]:
            break
        elif J[0] <= complement[i][0]:
            if J[1] < complement[i][1]:
                complement[i][0] = J[1]+1
                break
            else:
                to_remove.append(complement[i])
        else:
            if J[1] < complement[i][1]:
                complement.insert(i, [complement[i][0], J[0]-1])
                complement[i+1][0] = J[1] + 1
                break
            else:
                complement[i][1] = J[0]-1

    for rem in to_remove:
        complement.remove(rem)

total = len(complement)

for C in complement:
    total += C[1] - C[0]

print(total)











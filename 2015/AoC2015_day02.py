f = open("input_files/AoC2015_day02_input.txt")
inputs = f.readlines()
f.close()

area = 0
ribbon = 0

for box in inputs:
    d = list(map(int, box.rstrip().split("x")))
    d.sort()

    area += d[0] * d[1] + 2 * (d[0] * d[1] + d[0] * d[2] + d[1] * d[2])
    ribbon += 2*(d[0] + d[1]) + d[0]*d[1]*d[2]

print(area)
print(ribbon)


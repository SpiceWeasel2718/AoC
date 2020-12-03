target_coord = (2981, 3075)

code = 20151125

layer = target_coord[0] + target_coord[1] - 1
ind = int(layer*(layer-1)/2) + target_coord[1]

for i in range(ind-1):
    code = code * 252533 % 33554393

print(code)

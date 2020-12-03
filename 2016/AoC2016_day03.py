f = open("input_files/AoC2016_day03_input.txt")
input_text = f.read().split("\n")
f.close()

data = []

for i in range(int(len(input_text)/3)):
    batch = [[],[],[]]
    for j in range(3):
        row = input_text[3*i+j].strip().split()
        for k in range(3):
            batch[k].append(int(row[k]))
    data += batch

valid = 0

for arr in data:
    if all([arr[i%3] + arr[(i+1)%3] > arr[(i+2)%3] for i in range(3)]):
        valid += 1

print(valid)


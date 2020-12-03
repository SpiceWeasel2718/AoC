from itertools import permutations

f = open("input_files/AoC2015_day13_input.txt")
input_text = f.read().split("\n")
f.close()

happ_data = {}

for line in input_text:
    words = line.split()
    if words[0] not in happ_data.keys():
        happ_data.update({words[0]: {}})

    if words[2] == "lose":
        words[3] = "-" + words[3]

    happ_data[words[0]].update({words[-1][0:-1]: int(words[3])})

guests = list(happ_data.keys())


happ_data.update({"You": {}})

for guest in guests:
    happ_data[guest].update({"You": 0})
    happ_data["You"].update({guest: 0})

guests.append("You")


connections = []

for guest in guests[:-1]:
    for guest2 in guests[guests.index(guest)+1:]:
        connections.append([guest, guest2, happ_data[guest][guest2] + happ_data[guest2][guest]])

connections.sort(reverse=True, key=lambda a: a[2])

table = {}
for guest in guests:
    table.update({guest: [0]})


arrangements = permutations(range(len(guests)))

totals = []
num_guest = len(guests)

for arr in arrangements:
    total = 0
    for i in range(len(arr)):
        total += happ_data[guests[arr[i]]][guests[arr[(i+1) % num_guest]]] + \
                 happ_data[guests[arr[(i+1) % num_guest]]][guests[arr[i]]]
    totals.append(total)

print(max(totals))



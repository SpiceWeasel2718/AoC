f = open("input_files/AoC2016_day04_input.txt")
input_text = f.read().split("\n")
f.close()

alphabet_dict = {}

for i in range(97, 123):
    alphabet_dict.update({chr(i): 0})

alphabet = list(alphabet_dict.keys())

rooms = []

for line in input_text:
    data = line.split("-")
    info = data[-1].rstrip("]").split("[")

    letters = alphabet.copy()
    letter_counts = alphabet_dict.copy()

    for string in data[:-1]:
        for c in string:
            letter_counts[c] += 1
    letters.sort(key=lambda l: letter_counts[l], reverse=True)
    check = "".join(letters[:5])
    if check == info[1]:
        rooms.append(data[:-1] + [int(info[0])])

for room in rooms:
    name = []
    for enc_word in room[:-1]:
        name.append("")
        for c in enc_word:
            name[-1] += chr(((ord(c)-97+room[-1]) % 26) + 97)
    if "northpole" in " ".join(name):
        print(" ".join(name), room[-1])





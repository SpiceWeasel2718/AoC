f = open("input_files/AoC2016_day06_input.txt")
input_text = f.read().split("\n")
f.close()

letter_counts = {}

for i in range(97, 123):
    letter_counts.update({chr(i): len(input_text[0])*[0]})

for line in input_text:
    for i in range(len(line)):
        letter_counts[line[i]][i] += 1


message = len(input_text[0]) * [""]
counts = len(input_text[0]) * [50]

for letter in letter_counts.keys():
    for pos in range(len(letter_counts[letter])):
        if letter_counts[letter][pos] < counts[pos]:
            counts[pos] = letter_counts[letter][pos]
            message[pos] = letter

print("".join(message))

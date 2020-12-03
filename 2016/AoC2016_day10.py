f = open("input_files/AoC2016_day10_input.txt")
input_text = f.read().split("\n")
f.close()


bots = {}
outputs = {}

instructions = len(input_text)

while len(input_text) > 0:
    remove_lines = []
    for line in input_text:
        data = line.split()
        if data[0] == "value":
            if not bots.get(data[5]):
                bots.update({data[5]: [data[1]]})
            else:
                bots[data[5]].append(data[1])
            remove_lines.append(line)
        else:
            if not bots.get(data[1]):
                bots.update({data[1]: []})
            elif len(bots[data[1]]) == 2:
                bots[data[1]].sort(key=lambda a: int(a))

                if bots[data[1]] == ["17", "61"]:
                    print(data[1])

                for i in [6, 11]:
                    if data[i-1] == "bot":
                        if not bots.get(data[i]):
                            bots.update({data[i]: []})
                        bots[data[i]].append(bots[data[1]].pop(0))
                    else:
                        if not outputs.get(data[i]):
                            outputs.update({data[i]: bots[data[1]].pop(0)})

                remove_lines.append(line)

    for line in remove_lines:
        input_text.remove(line)

print(int(outputs["0"]) * int(outputs["1"]) * int(outputs["2"]))








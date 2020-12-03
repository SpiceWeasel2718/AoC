f = open("input_files/AoC2016_day09_input.txt")
input_text = f.read().split("\n")
f.close()


def expand(text):
    ind = text.find("(")
    decomp_text = text[:ind]

    while ind > -1:
        text = text[ind:]
        ind2 = text.find(")")
        data = [int(n) for n in text[1:ind2].split("x")]
        text = text[ind2 + 1:]
        ind = text.find("(", data[0])
        decomp_text += data[1] * text[:data[0]]
        decomp_text += text[data[0]:ind] if ind > -1 else text[data[0]:]

    return decomp_text


def expanded_len(text):
    ind = text.find("(")
    if ind == -1:
        return len(text)

    count = ind

    while ind > -1:
        text = text[ind:]
        ind2 = text.find(")")
        data = [int(n) for n in text[1:ind2].split("x")]
        text = text[ind2 + 1:]
        ind = text.find("(", data[0])

        count += data[1] * expanded_len(text[:data[0]])
        count += expanded_len(text[data[0]:ind] if ind > -1 else text[data[0]:])

    return count


# print(len(expand(input_text[0])))
print(expanded_len(input_text[0]))





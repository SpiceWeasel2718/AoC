seq = "hxbxwxba"
seq = "hxbxxyzz"


def increment(string):
    if string[-1] != "z":
        return string[:-1] + chr(ord(string[-1]) + 1)
    elif string == "zzzzzzzz":
        return "aaaaaaaa"
    else:
        string = string.rstrip("z")
        return string[:-1] + chr(ord(string[-1]) + 1) + (8-len(string))*"a"


def is_valid_pass(string):
    if any([c in string for c in ["i", "o", "l"]]):
        return False

    straight = False
    if string[0] == string[1]:
        pair = 1
        justpair = True
    else:
        pair = 0
        justpair = False

    for i in range(2, len(string)):
        if string[i] == string[i-1] and not justpair:
            pair += 1
            justpair = True
        else:
            justpair = False
        if ord(string[i-1]) == ord(string[i]) - 1 and ord(string[i-2]) == ord(string[i]) - 2:
            straight = True

    return straight and pair > 1


seq = increment(seq)

while not is_valid_pass(seq):
    seq = increment(seq)

print(seq)

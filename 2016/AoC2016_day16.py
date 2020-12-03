state = "11011110011011101"
#disk_size = 272
disk_size = 35651584


def iterate(seq):
    output = seq + "0"
    for i in range(len(seq)-1, -1, -1):
        output += "1" if seq[i] == "0" else "0"
    return output


def checksum(seq):
    output = seq
    while len(output) % 2 == 0:
        seq = output
        output = ""
        for i in range(0, len(seq), 2):
            output += "1" if seq[i] == seq[i+1] else "0"

    return output


while len(state) < disk_size:
    state = iterate(state)

print(checksum(state[:disk_size]))




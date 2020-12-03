seq = "1113122113"

def look_and_say(in_seq):
    out_seq = ""
    n = in_seq[0]
    count = 0
    for i in range(len(in_seq)):
        digit = in_seq[i]
        if digit == n:
            count += 1
        else:
            out_seq += str(count) + n
            n = digit
            count = 1

    return out_seq + str(count) + n


for i in range(50):
    seq = look_and_say(seq)

print(len(seq))

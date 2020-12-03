"""
Input:

Disc #1 has 13 positions; at time=0, it is at position 11.
Disc #2 has 5 positions; at time=0, it is at position 0.
Disc #3 has 17 positions; at time=0, it is at position 11.
Disc #4 has 3 positions; at time=0, it is at position 0.
Disc #5 has 7 positions; at time=0, it is at position 2.
Disc #6 has 19 positions; at time=0, it is at position 17.
"""

disc_info = [
    [11+1, 13],
    [0+2, 5],
    [11+3, 17],
    [0+4, 3],
    [2+5, 7],
    [17+6, 19],
    [0+7, 11]  # Part 2
]

t = 15

while any([(t + info[0]) % info[1] != 0 for info in disc_info]):
    t += 19

print(t)












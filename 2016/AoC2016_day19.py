import math as m

elves = 3012210
pos = 1
inc = 2


def highest_pwr_of_2(n):
    return n & (~(n - 1))


"""
# Part 1

while elves > 1:
    if elves % 2 == 1:
        elves -= 1
        pos += inc

    div = highest_pwr_of_2(elves)
    inc *= div
    elves = int(elves / div)

print(pos)
"""

# Part 2

k = 3

while k < elves:
    k *= 3

k = int(k/3)
rem = elves - k

if rem < k:
    print(rem)
else:
    print(2*rem - k)











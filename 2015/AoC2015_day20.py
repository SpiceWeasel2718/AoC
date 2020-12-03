import math as m

pres_limit = 36000000


def divisors(num):
    if num == 1:
        return [1]
    result = []
    for div in range(m.floor(num/50)+1, m.ceil(num / 2)+1):
        if num % div == 0:
            result.append(div)
    result.append(num)
    return result


target_sum = m.ceil(pres_limit/11)

house = 831600
ul = 0

while True:
    house += 30
    div = divisors(house)
    s = sum(div)
    ul = max(ul, s)
    print(house, ul)
    if s >= target_sum:
        print(s, div)
        break




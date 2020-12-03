import collections
import math

def part1(input_text):
    reactions = {}
    for line in input_text:
        ingredients, product = line.split(' => ')
        strings = [ing.split(' ') for ing in ingredients.split(', ')]
        prod_strings = product.split(' ')
        reactions[prod_strings[1]] = [{string[1]: int(string[0]) for string in strings}, int(prod_strings[0])]

    leftovers = {k: 0 for k in reactions}
    steps = collections.deque([(1, 'FUEL')])

    total = 0

    while not len(steps) == 0:
        needed_amount, product = steps.popleft()
        if leftovers[product] >= needed_amount:
            leftovers[product] -= needed_amount
            continue
        needed_amount -= leftovers[product]
        leftovers[product] = 0
        product_amount = reactions[product][1]
        times = needed_amount // product_amount
        if needed_amount % product_amount != 0:
            times += 1
        
        leftovers[product] += (product_amount * times) - needed_amount
        
        for el, n in reactions[product][0].items():
            if el == 'ORE':
                total += n * times
            else:
                steps.append((times * n, el))

    return total
    

def part2(input_text):
    reactions = {}
    for line in input_text:
        ingredients, product = line.split(' => ')
        strings = [ing.split(' ') for ing in ingredients.split(', ')]
        prod_strings = product.split(' ')
        reactions[prod_strings[1]] = [{string[1]: int(string[0]) for string in strings}, int(prod_strings[0])]

    leftovers = {k: 0 for k in reactions}
    ore_needed = 0
    fuel = 1
    factor = 0

    while True:
        leftovers = {k: 0 for k in reactions}
        steps = collections.deque([(fuel, 'FUEL')])
        ore_needed = 0

        while not len(steps) == 0:
            needed_amount, product = steps.popleft()
            if leftovers[product] >= needed_amount:
                leftovers[product] -= needed_amount
                continue
            needed_amount -= leftovers[product]
            leftovers[product] = 0
            product_amount = reactions[product][1]
            times = needed_amount // product_amount
            if needed_amount % product_amount != 0:
                times += 1
            
            leftovers[product] += (product_amount * times) - needed_amount
            
            for el, n in reactions[product][0].items():
                if el == 'ORE':
                    ore_needed += times * n
                else:
                    steps.append((times * n, el))
        
        if factor == 0:
            factor = 10 ** int(math.log10(1000000000000 // ore_needed))
            fuel = factor

        if ore_needed > 1000000000000:
            fuel -= factor
            if factor == 1:
                break
            else:
                factor //= 10
        else:
            fuel += factor
    
    return fuel


if __name__ == '__main__':
    from pathlib import Path
    with open(next(Path().glob('**/AoC2019_day14_input.txt'))) as f:
        input_text = f.read().splitlines()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
import re

def part1(input_text):
    foods = []
    allergens = {}
    all_ingredients = set()

    for line in input_text.splitlines():
        ingredients_text, allergens_text = re.match(r'(\w+(?: \w+)*) \(contains (\w+(?:, \w+)*)\)', line).groups()
        ingredients = set(ingredients_text.split())
        all_ingredients |= ingredients
        foods.append(ingredients.copy())
        for allergen in allergens_text.split(', '):
            if allergen in allergens:
                allergens[allergen] &= ingredients
            else:
                allergens[allergen] = ingredients.copy()
    
    safe = all_ingredients
    for unsafe in allergens.values():
        safe -= unsafe
    
    return sum(len(food & safe) for food in foods)


def part2(input_text):
    allergens = {}

    for line in input_text.splitlines():
        ingredients_text, allergens_text = re.match(r'(\w+(?: \w+)*) \(contains (\w+(?:, \w+)*)\)', line).groups()
        ingredients = set(ingredients_text.split())
        for allergen in allergens_text.split(', '):
            if allergen in allergens:
                allergens[allergen] &= ingredients
            else:
                allergens[allergen] = ingredients.copy()
    
    determined = set()

    for possibilities in allergens.values():
        if len(possibilities) == 1:
            determined |= possibilities
    
    done = False

    while not done:
        done = True
        for possibilities in allergens.values():
            if len(possibilities) > 1:
                done = False
                possibilities -= determined
                if len(possibilities) == 1:
                    determined |= possibilities
    
    return ','.join(allergens[allergen].pop() for allergen in sorted(allergens))


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day21_input.txt') as f:
        input_text = f.read()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    time_execution = 1

    if time_execution:
        import timeit
        for part in ['part1', 'part2']:
            timer = timeit.Timer(f'{part}(input_text)', globals=globals())
            n, time = timer.autorange()
            print(f'{part} took {time/n:.5f} seconds on average when run {n} times')
import re

def part1(input_text):
    rules, __, nearby = input_text.split('\n\n', 2)
    rules_re = re.compile(r'\D+: (\d+)-(\d+) or (\d+)-(\d+)')

    ranges = []

    for rule in rules.splitlines():
        a, b, c, d = re.match(rules_re, rule).groups()
        ranges.append((int(a), int(b)))
        ranges.append((int(c), int(d)))

    error_rate = 0

    for ticket_str in nearby.splitlines()[1:]:
        for s in ticket_str.split(','):
            n = int(s)
            for a, b in ranges:
                if a <= n <= b:
                    break
            else:
                error_rate += n

    return error_rate


def part2(input_text):
    rules_str, your, nearby = input_text.split('\n\n', 2)
    rules_re = re.compile(r'(\D+): (\d+)-(\d+) or (\d+)-(\d+)')

    rules = {}

    for rule in rules_str.splitlines():
        name, *ranges = re.match(rules_re, rule).groups()
        rules[name] = [int(n) for n in ranges]

    valid = []

    for ticket_str in nearby.splitlines()[1:]:
        ticket = [int(n) for n in ticket_str.split(',')]
        for n in ticket:
            for a, b, c, d in rules.values():
                if a <= n <= b or c <= n <= d:
                    break
            else:
                break
        else:
            valid.append(ticket)

    all_fields = set(rules)
    field_order = []
    determined = set()

    for i in range(len(rules)):
        possible_fields = all_fields.copy()
        
        for ticket in valid:
            n = ticket[i]
            to_remove = []
            for field in possible_fields:
                a, b, c, d = rules[field]
                if not (a <= n <= b or c <= n <= d):
                    to_remove.append(field)
            possible_fields.difference_update(to_remove)
        
        if len(possible_fields) == 1:
            determined |= possible_fields
        
        field_order.append(possible_fields)

    while len(determined) < len(rules):
        for f in field_order:
            if len(f) > 1:
                f -= determined
            else:
                determined |= f
    
    prod = 1

    for n, field in zip(your.splitlines()[1].split(','), field_order):
        if field.pop().startswith('departure'):
            prod *= int(n)

    return prod


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day16_input.txt') as f:
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
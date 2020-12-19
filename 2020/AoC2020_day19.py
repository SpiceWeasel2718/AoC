import re

def part1(input_text):
    rules_text, messages = input_text.split('\n\n')

    rules = {}
    determined = set()

    for rule in rules_text.splitlines():
        num, contents = rule.split(': ', 1)
        if contents[0] == '"':
            rules[num] = contents[1:-1]
            determined.add(num)
        else:
            parts = contents.split(' | ')
            rules[num] = [p.split() for p in parts]
    
    while len(determined) != len(rules):
        for num, expr in rules.items():
            if num not in determined:
                all_determined = True
                for sequence in expr:
                    for i, n in enumerate(sequence):
                        if n in determined:
                            sequence[i] = rules[n]
                        elif n in rules:
                            all_determined = False

                if all_determined:
                    rules[num] = '|'.join(f"(?:{')(?:'.join(e)})" for e in expr)
                    determined.add(num)

    count = 0

    for message in messages.splitlines():
        if re.fullmatch(rules['0'], message):
            count += 1
    
    return count


def part2(input_text):
    rules_text, messages = input_text.split('\n\n')

    rules = {}
    determined = set()

    for rule in rules_text.splitlines():
        num, contents = rule.split(': ', 1)
        if contents[0] == '"':
            rules[num] = contents[1:-1]
            determined.add(num)
        else:
            parts = contents.split(' | ')
            rules[num] = [p.split() for p in parts]
    
    while len(determined) != len(rules):
        for num, expr in rules.items():
            if num not in determined:
                all_determined = True
                for sequence in expr:
                    for i, n in enumerate(sequence):
                        if n in determined:
                            sequence[i] = rules[n]
                        elif n in rules:
                            all_determined = False

                if all_determined:
                    rules[num] = '|'.join(f"(?:{')(?:'.join(e)})" for e in expr)
                    determined.add(num)

    rule_31_prefix = f"(?:{rules['31']}){{1,"
    count = 0

    for message in messages.splitlines():
        start = 0
        max_31 = -1

        while m := re.match(rules['42'], message[start:]):
            start += m.end()
            max_31 += 1

        if max_31 >= 1 and re.fullmatch(f"{rule_31_prefix}{max_31}}}", message[start:]):
            count += 1
    
    return count


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day19_input.txt') as f:
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
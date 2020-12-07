from collections import deque

def part1(input_text):
    rules = {}
    for line in input_text.splitlines():
        color, contents = line.split(' bags contain ')
        rules[color] = {}

        for bag_type in contents.split(', '):
            n, *sub_color_words = bag_type.split()
            if n == 'no':
                break
            rules[color][' '.join(sub_color_words[:-1])] = int(n)
    
    count = 0

    for color in rules:
        color_queue = deque([color])
        # faster with a deque than a list, apparently

        while color_queue:
            contents = rules[color_queue.popleft()]
            
            if 'shiny gold' in contents:
                count += 1
                break
            else:
                color_queue.extend(contents)
                
    return count

    # The way I would do it with a recursive function, which is like 3x slower:

    # def contains_shiny_gold(color):
    #     return ('shiny gold' in (contents := rules[color])) or any(contains_shiny_gold(sub_color) for sub_color in contents)

    # for color in rules:
    #     count += contains_shiny_gold(color)


def part2(input_text):
    rules = {}
    for line in input_text.splitlines():
        color, contents = line.split(' bags contain ')
        rules[color] = {}

        for bag_type in contents.split(', '):
            n, *sub_color_words = bag_type.split()
            if n == 'no':
                break
            rules[color][' '.join(sub_color_words[:-1])] = int(n)
    
    def sum_bags(color):
        if not rules[color]:
            return 1
        return 1 + sum(n * sum_bags(sub_color) for sub_color, n in rules[color].items())

    return sum_bags('shiny gold') - 1


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day07_input.txt') as f:
        input_text = f.read()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
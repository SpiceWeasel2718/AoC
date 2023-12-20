def part1(input_text: str):
    chunks = input_text.split('\n\n')
    workflows = {}

    def make_lambda(k, cmp, n):
        if cmp == '<':
            return (lambda part : (part[k] < n))
        else:
            return (lambda part : (part[k] > n))

    for line in chunks[0].splitlines():
        name, rules_text = line.split('{', maxsplit=1)
        rules = rules_text.split(',')
        end = (rules.pop())[:-1]
        
        workflow = []
        
        for rule in rules:
            cond, dest = rule.split(':', maxsplit=1)
            k, cmp, n = cond[0], cond[1], int(cond[2:])

            workflow.append((make_lambda(k, cmp, n), dest))

        workflow.append((lambda part : True, end))
        workflows[name] = workflow

    s = 0

    for line in chunks[1].splitlines():
        part = {}

        for coord in line[1:-1].split(','):
            part[coord[0]] = int(coord[2:])

        wf = 'in'

        while wf != 'A':
            for rule, dest in workflows[wf]:
                if rule(part):
                    wf = dest
                    break
            if wf == 'R':
                break
        else:
            s += sum(part.values())

    return s


def part2(input_text: str):
    from copy import deepcopy

    chunks = input_text.split('\n\n')
    workflows = {}

    for line in chunks[0].splitlines():
        name, rules_text = line.split('{', maxsplit=1)
        rules = rules_text.split(',')
        end = (rules.pop())[:-1]
        
        workflow = []
        
        for rule in rules:
            cond, dest = rule.split(':', maxsplit=1)
            k, cmp, n = cond[0], cond[1], int(cond[2:])

            workflow.append((k, cmp, n, dest))
            
        while workflow and workflow[-1][1] == end:
            workflow.pop()

        workflow.append(('x', '<', 4001, end))
        workflows[name] = workflow

    accepted = []
    part_range = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}

    queue = [('in', part_range)]

    while queue:
        wf, pr = queue.pop()

        if wf == 'A':
            accepted.append(pr)
            continue
        elif wf == 'R':
            continue

        for k, cmp, n, dest in workflows[wf]:
            if cmp == '<':
                if pr[k][1] < n:
                    queue.append((dest, pr))
                    break
                elif pr[k][0] >= n:
                    continue
                else:
                    prc = deepcopy(pr)
                    prc[k][1] = n-1
                    queue.append((dest, prc))
                    pr[k][0] = n
            else:
                if pr[k][0] > n:
                    queue.append((dest, pr))
                    break
                elif pr[k][1] <= n:
                    continue
                else:
                    prc = deepcopy(pr)
                    prc[k][0] = n+1
                    queue.append((dest, prc))
                    pr[k][1] = n

    s = 0

    for pr in accepted:
        prod = 1
        for l, r in pr.values():
            prod *= r - l + 1
        s += prod

    return s


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2023_day19_input.txt') as f:
        input_text = f.read()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    time_execution = 0

    if time_execution:
        import timeit
        for part in ['part1', 'part2']:
            timer = timeit.Timer(f'{part}(input_text)', globals=globals())
            n, time = timer.autorange()
            print(f'{part} took {time/n:.5f} seconds on average when run {n} times')
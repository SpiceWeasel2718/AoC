def part1(input_text: str):
    from itertools import cycle

    turns, network_text = input_text.split('\n\n')

    network = {}

    for line in network_text.splitlines():
        network[line[:3]] = [line[7:10], line[12:15]]
    
    turns_iter = iter(cycle(turns))
    current = 'AAA'
    steps = 0

    while current != 'ZZZ':
        turn = next(turns_iter)
        current = network[current][0] if turn == 'L' else network[current][1]
        steps += 1

    return steps


def part2(input_text: str):
    from itertools import cycle
    from math import lcm

    turns, network_text = input_text.split('\n\n')

    network = {}
    a_nodes = []

    for line in network_text.splitlines():
        node = line[:3]
        network[node] = [line[7:10], line[12:15]]
        if node.endswith('A'):
            a_nodes.append(node)
    
    turns_len = len(turns)
    waypoint_lists = []

    for start_node in a_nodes:
        seen = set()
        current = start_node
        waypoint_list = []

        for step, turn in enumerate(cycle(turns)):
            state = (current, step % turns_len)
            if state in seen:
                waypoint_list.append(step)
                waypoint_list.append(step % turns_len)
                break
            else:
                if current.endswith('Z'):
                    waypoint_list.append(step)
                seen.add(state)
                current = network[current][0] if turn == 'L' else network[current][1]
        
        waypoint_lists.append(waypoint_list)

    # By inspection, each path is a loop with length = the number of steps 
    # from the start node to the first Z node, even though the paths don't 
    # loop back to their start nodes. There is only one Z node per path.
    return lcm(*[wl[0] for wl in waypoint_lists])


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2023_day08_input.txt') as f:
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
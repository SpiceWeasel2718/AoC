def part1(input_text: str):
    from collections import defaultdict
    from math import inf

    maze_points = set()

    for row, line in enumerate(input_text.splitlines()):
        for col, c in enumerate(line):
            if c != "#":
                pos = row + col * 1j
                maze_points.add(pos)
                if c == "S":
                    start_pos = pos
                elif c == "E":
                    end_pos = pos

    directions = [1, 1j, -1, -1j]
    maze = defaultdict(list)

    for pos in maze_points:
        for d in directions:
            test_pos = pos + d
            if test_pos in maze_points:
                maze[(pos, d)].append((test_pos, d))
                rd = d * 1j
                maze[(pos, rd)].append((pos, d))
                maze[(pos, -rd)].append((pos, d))

    end_states = []

    for d in directions:
        if end_pos + d in maze_points:
            end_state = (end_pos, -d)
            end_states.append(end_state)
            maze[end_state] = []

    unvisited = set(maze)
    costs = defaultdict(lambda: inf)
    costs[(start_pos, 1j)] = 0

    while any(end_state in unvisited for end_state in end_states):
        state = min(unvisited, key=lambda k: costs[k])
        unvisited.remove(state)
        for nbr in maze[state]:
            if state[1] == nbr[1]:
                costs[nbr] = min(costs[nbr], costs[state] + 1)
            else:
                costs[nbr] = min(costs[nbr], costs[state] + 1000)

    return min(costs[k] for k in end_states)


def part2(input_text: str):
    from collections import defaultdict
    from math import inf

    maze_points = set()

    for row, line in enumerate(input_text.splitlines()):
        for col, c in enumerate(line):
            if c != "#":
                pos = row + col * 1j
                maze_points.add(pos)
                if c == "S":
                    start_pos = pos
                elif c == "E":
                    end_pos = pos

    directions = [1, 1j, -1, -1j]
    maze = defaultdict(list)

    for pos in maze_points:
        for d in directions:
            maze[(pos, d)].append((pos, d * 1j))
            maze[(pos, d)].append((pos, -d * 1j))

            test_pos = pos + d
            if test_pos in maze_points:
                maze[(pos, d)].append((test_pos, d))

    end_states = []

    for d in directions:
        if end_pos + d in maze_points:
            end_state = (end_pos, -d)
            end_states.append(end_state)

    unvisited = set(maze)
    costs = defaultdict(lambda: inf)
    costs[(start_pos, 1j)] = 0
    paths = defaultdict(set)
    paths[(start_pos, 1j)] = {(start_pos, 1j)}

    while min(costs[k] for k in unvisited) <= min(costs[k] for k in end_states):
        state = min(unvisited, key=lambda k: costs[k])
        unvisited.remove(state)
        for nbr in maze[state]:
            if state[1] == nbr[1]:
                m = min(costs[nbr], costs[state] + 1)
                if m == costs[nbr]:
                    paths[nbr] |= paths[state]
                else:
                    paths[nbr] = paths[state] | {nbr}
                costs[nbr] = m
            else:
                m = min(costs[nbr], costs[state] + 1000)
                if m == costs[nbr]:
                    paths[nbr] |= paths[state]
                else:
                    paths[nbr] = paths[state] | {nbr}
                costs[nbr] = m

    all_paths = set()

    for end_state in end_states:
        all_paths |= paths[end_state]

    all_tiles = {pos for pos, d in all_paths}

    return len(all_tiles)


if __name__ == "__main__":
    from pathlib import Path

    current_file = Path(__file__)
    input_file = (
        current_file.parent / "input_files" / (current_file.stem + "_input.txt")
    )

    with open(input_file) as fp:
        input_text = fp.read()

    print("Part 1:")
    print(p1 := part1(input_text))
    print("Part 2:")
    print(part2(input_text))

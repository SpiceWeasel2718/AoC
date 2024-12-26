def part1(input_text: str):
    from collections import deque
    from itertools import pairwise, permutations

    numpad_adj = {
        "A": {"0": "<", "3": "^"},
        "0": {"A": ">", "2": "^"},
        "1": {"2": ">", "4": "^"},
        "2": {"0": "v", "1": "<", "5": "^", "3": ">"},
        "3": {"A": "v", "2": "<", "6": "^"},
        "4": {"1": "v", "7": "^", "5": ">"},
        "5": {"2": "v", "4": "<", "8": "^", "6": ">"},
        "6": {"3": "v", "5": "<", "9": "^"},
        "7": {"4": "v", "8": ">"},
        "8": {"5": "v", "7": "<", "9": ">"},
        "9": {"6": "v", "8": "<"},
    }

    direction_pad_adj = {
        "A": {">": "v", "^": "<"},
        "^": {"A": ">", "v": "v"},
        ">": {"A": "^", "v": "<"},
        "v": {"<": "<", "^": "^", ">": ">"},
        "<": {"v": ">"},
    }

    def pad_transitions(pad_adj):
        pad = {key: {key: ["A"]} for key in pad_adj}

        for key, target in permutations(pad_adj, 2):
            valid_paths = []
            queue = deque()
            queue.append([key])
            max_path_len = 10
            while queue:
                path = queue.pop()
                for k in pad_adj[path[-1]]:
                    if k not in path:
                        new_path = path + [k]
                        if k == target and len(new_path) <= max_path_len:
                            valid_paths.append(new_path)
                            max_path_len = min(max_path_len, len(new_path))
                        elif len(new_path) < max_path_len:
                            queue.appendleft(new_path)
            pad[key][target] = []
            for path in valid_paths:
                path_str = ""
                for k, v in pairwise(path):
                    move = pad_adj[k][v]
                    if move in path_str and path_str[-1] != move:
                        break
                    path_str += move
                else:
                    pad[key][target].append(path_str + "A")

        return pad

    numpad = pad_transitions(numpad_adj)
    direction_pad = pad_transitions(direction_pad_adj)

    def input_seq(paths, depth, pad=direction_pad):
        if depth == 0:
            return paths[0]

        input_strings = []
        state = "A"

        for path in paths:
            input_str = ""
            for c in path:
                input_str += input_seq(pad[state][c], depth - 1)
                state = c
            input_strings.append(input_str)

        return min(input_strings, key=len)

    complexity = 0

    for line in input_text.splitlines():
        input_str = input_seq([line], 3, pad=numpad)
        complexity += len(input_str) * int(line[:-1])

    return complexity


def part2(input_text: str):
    from collections import deque
    from functools import cache, partial
    from itertools import pairwise, permutations

    numpad_adj = {
        "A": {"0": "<", "3": "^"},
        "0": {"A": ">", "2": "^"},
        "1": {"2": ">", "4": "^"},
        "2": {"0": "v", "1": "<", "5": "^", "3": ">"},
        "3": {"A": "v", "2": "<", "6": "^"},
        "4": {"1": "v", "7": "^", "5": ">"},
        "5": {"2": "v", "4": "<", "8": "^", "6": ">"},
        "6": {"3": "v", "5": "<", "9": "^"},
        "7": {"4": "v", "8": ">"},
        "8": {"5": "v", "7": "<", "9": ">"},
        "9": {"6": "v", "8": "<"},
    }

    direction_pad_adj = {
        "A": {">": "v", "^": "<"},
        "^": {"A": ">", "v": "v"},
        ">": {"A": "^", "v": "<"},
        "v": {"<": "<", "^": "^", ">": ">"},
        "<": {"v": ">"},
    }

    def pad_transitions(pad_adj):
        pad = {key: {key: ["A"]} for key in pad_adj}

        for key, target in permutations(pad_adj, 2):
            valid_paths = []
            queue = deque()
            queue.append([key])
            max_path_len = 10
            while queue:
                path = queue.pop()
                for k in pad_adj[path[-1]]:
                    if k not in path:
                        new_path = path + [k]
                        if k == target and len(new_path) <= max_path_len:
                            valid_paths.append(new_path)
                            max_path_len = min(max_path_len, len(new_path))
                        elif len(new_path) < max_path_len:
                            queue.appendleft(new_path)
            pad[key][target] = []
            for path in valid_paths:
                path_str = ""
                for k, v in pairwise(path):
                    move = pad_adj[k][v]
                    if move in path_str and path_str[-1] != move:
                        break
                    path_str += move
                else:
                    pad[key][target].append(path_str + "A")

        for key in pad:
            for target in pad[key]:
                pad[key][target] = tuple(pad[key][target])

        return pad

    numpad = pad_transitions(numpad_adj)
    direction_pad = pad_transitions(direction_pad_adj)

    def sequence_length(path, depth, pad=direction_pad):
        if depth == 0:
            return len(path)

        state = "A"
        seq_len = 0

        for c in path:
            seq_len += min(
                direction_seq(next_path, depth - 1) for next_path in pad[state][c]
            )
            state = c

        return seq_len

    numpad_seq = cache(partial(sequence_length, pad=numpad))
    direction_seq = cache(partial(sequence_length, pad=direction_pad))

    complexity = 0

    for line in input_text.splitlines():
        complexity += numpad_seq(line, 26) * int(line[:-1])

    return complexity


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

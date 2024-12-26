def part1(input_text: str):
    from collections import deque

    topo_map = {}
    trailheads = []

    for row, line in enumerate(input_text.splitlines()):
        for col, n in enumerate(line):
            pos = row + col * 1j
            height = int(n)
            topo_map[pos] = height
            if height == 0:
                trailheads.append(pos)

    def nbrs(pos):
        for d in [1, 1j, -1, -1j]:
            if pos + d in topo_map:
                yield pos + d

    queue = deque()
    score = 0

    for trailhead in trailheads:
        reachable = set()
        queue.append((trailhead, 0))

        while queue:
            pos, height = queue.pop()
            for nbr in nbrs(pos):
                nbr_height = topo_map[nbr]
                if nbr_height - height == 1:
                    if nbr_height == 9:
                        reachable.add(nbr)
                    else:
                        queue.append((nbr, nbr_height))

        score += len(reachable)

    return score


def part2(input_text: str):
    from collections import deque

    topo_map = {}
    trailheads = []

    for row, line in enumerate(input_text.splitlines()):
        for col, n in enumerate(line):
            pos = row + col * 1j
            height = int(n)
            topo_map[pos] = height
            if height == 0:
                trailheads.append(pos)

    def nbrs(pos):
        for d in [1, 1j, -1, -1j]:
            if pos + d in topo_map:
                yield pos + d

    queue = deque()
    score = 0

    for trailhead in trailheads:
        queue.append((trailhead, 0))

        while queue:
            pos, height = queue.pop()
            for nbr in nbrs(pos):
                nbr_height = topo_map[nbr]
                if nbr_height - height == 1:
                    if nbr_height == 9:
                        score += 1
                    else:
                        queue.append((nbr, nbr_height))

    return score


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

def part1(input_text: str):
    from collections import defaultdict
    from math import inf

    memory_width = 70
    byte_cutoff = 1024

    corruption = []

    for line in input_text.splitlines():
        a, b = [float(n) for n in line.split(",")]
        corruption.append(a + b * 1j)

    memory = set()

    for a in range(memory_width + 1):
        for b in range(memory_width + 1):
            memory.add(a + b * 1j)

    memory.difference_update(corruption[:byte_cutoff])

    start_pos = 0
    end_pos = memory_width + memory_width * 1j

    dists = defaultdict(lambda: inf)
    dists[start_pos] = 0

    while end_pos in memory:
        pos = min(memory, key=lambda k: dists[k])
        memory.remove(pos)
        for d in [1, 1j, -1, -1j]:
            nbr = pos + d
            if nbr in memory:
                dists[nbr] = dists[pos] + 1

    return dists[end_pos]


def part2(input_text: str):
    memory_width = 70

    corruption = []

    for line in input_text.splitlines():
        a, b = [float(n) for n in line.split(",")]
        corruption.append(a + b * 1j)

    memory = set()

    for a in range(memory_width + 1):
        for b in range(memory_width + 1):
            memory.add(a + b * 1j)

    end_pos = memory_width + memory_width * 1j

    def path_exists(remaining):
        queue = set()
        queue.add(0.0)

        while queue:
            pos = queue.pop()
            remaining.discard(pos)
            for d in [1, 1j, -1, -1j]:
                nbr = pos + d
                if nbr in remaining:
                    queue.add(nbr)

        return end_pos in remaining

    lb, ub = 0, len(corruption) - 1

    while lb < ub:
        m = (lb + ub) // 2
        remaining = memory - set(corruption[: m + 1])
        if path_exists(remaining):
            ub = m
        else:
            lb = m + 1

    return f"{int(corruption[ub].real)},{int(corruption[ub].imag)}"


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

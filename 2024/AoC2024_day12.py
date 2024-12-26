def part1(input_text: str):
    from collections import defaultdict, deque

    farm = defaultdict(str)

    for row, line in enumerate(input_text.splitlines()):
        for col, c in enumerate(line):
            farm[row + col * 1j] = c

    def nbrs(pos):
        for d in [1, 1j, -1, -1j]:
            yield pos + d

    plots_to_check = set(farm)
    price = 0

    while plots_to_check:
        queue = deque()
        queue.append(plots_to_check.pop())
        crop = farm[queue[0]]
        area = 0
        perimeter = 0

        while queue:
            current_plot = queue.pop()
            area += 1
            border = 4
            for nbr in nbrs(current_plot):
                if farm[nbr] == crop:
                    border -= 1
                    if nbr in plots_to_check:
                        queue.append(nbr)
                        plots_to_check.discard(nbr)
            perimeter += border

        price += area * perimeter

    return price


def part2(input_text: str):
    from collections import defaultdict, deque

    farm = defaultdict(str)

    for row, line in enumerate(input_text.splitlines()):
        for col, c in enumerate(line):
            farm[row + col * 1j] = c

    def nbrs(pos):
        for d in [1, 1j, -1, -1j]:
            yield pos + d

    plots_to_check = set(farm)
    queue = deque()
    price = 0

    while plots_to_check:
        queue.append(plots_to_check.pop())
        crop = farm[queue[0]]
        area = 0
        boundary = set()

        while queue:
            current_plot = queue.pop()
            area += 1
            for nbr in nbrs(current_plot):
                if farm[nbr] == crop:
                    if nbr in plots_to_check:
                        queue.append(nbr)
                        plots_to_check.discard(nbr)
                else:
                    boundary.add((current_plot, nbr - current_plot))

        sides = 0

        while boundary:
            side_member, normal = boundary.pop()
            sides += 1
            queue.append(side_member)
            while queue:
                current_plot = queue.pop()
                for nbr in nbrs(current_plot):
                    if (nbr, normal) in boundary:
                        queue.append(nbr)
                        boundary.discard((nbr, normal))

        price += area * sides

    return price


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

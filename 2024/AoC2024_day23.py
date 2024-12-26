def part1(input_text: str):
    from collections import defaultdict

    network = defaultdict(set)

    for line in input_text.splitlines():
        a, b = line.split("-")
        network[a].add(b)
        network[b].add(a)

    triples = set()

    for host in network:
        for conn in network[host]:
            for third in network[host] & network[conn]:
                triples.add(tuple(sorted([host, conn, third])))

    return sum(any(host.startswith("t") for host in triple) for triple in triples)


def part2(input_text: str):
    from collections import defaultdict

    network = defaultdict(set)

    for line in input_text.splitlines():
        a, b = line.split("-")
        network[a].add(b)
        network[b].add(a)

    lan = set()

    for host in network:
        subnets = {}

        for conn in network[host]:
            for c in subnets:
                if subnets[c] <= network[conn]:
                    subnets[c].add(conn)
                    break
            else:
                subnets[conn] = {host, conn}

        for c in subnets:
            if len(subnets[c]) > len(lan):
                lan = subnets[c]

    return ",".join(sorted(lan))


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

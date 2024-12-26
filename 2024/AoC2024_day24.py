def part1(input_text: str):
    import re
    from collections import deque
    from operator import and_, or_, xor

    wire_text, gate_text = input_text.split("\n\n")

    wires = {}

    for line in wire_text.splitlines():
        wire, value_str = line.split(": ")
        wires[wire] = int(value_str)

    operators = {"AND": and_, "OR": or_, "XOR": xor}
    gates = {}

    queue = deque()
    z_wires = []

    for line in gate_text.splitlines():
        i1, op, i2, out = re.findall(r"\w{2,3}", line)
        gates[out] = (i1, operators[op], i2)
        if out.startswith("z"):
            queue.append(out)
            z_wires.append(out)

    z_wires.sort()

    while queue:
        out = queue[-1]
        i1, op, i2 = gates[out]
        p1, p2 = i1 in wires, i2 in wires
        if p1 and p2:
            wires[out] = op(wires[i1], wires[i2])
            queue.pop()
        else:
            if not p1:
                queue.append(i1)
            if not p2:
                queue.append(i2)

    n = 0

    for wire in reversed(z_wires):
        n <<= 1
        n += wires[wire]

    return n


def part2(input_text: str):
    import re
    from collections import deque

    wire_text, gate_text = input_text.split("\n\n")

    x_labels, y_labels = [], []

    for line in wire_text.splitlines():
        label = line[:3]
        if line.startswith("x"):
            x_labels.append(label)
        else:
            y_labels.append(label)

    gates = {}
    z_labels = []

    for line in gate_text.splitlines():
        i1, op, i2, out = re.findall(r"\w{2,3}", line)
        sorted_args = sorted([i1, i2])
        gates[out] = (*sorted_args, op)
        if out.startswith("z"):
            z_labels.append(out)

    z_labels.sort()

    def count_gate_deps(gates):
        dep_counts = {}
        for gate in gates:
            deps = set()
            queue = deque()
            queue.append(gate)
            while queue:
                wire = queue.pop()
                deps.add(wire)
                if wire in gates:
                    i1, i2, op = gates[wire]
                    queue.appendleft(i1)
                    queue.appendleft(i2)
            dep_counts[gate] = len(deps) - 1
        return dep_counts

    dep_counts = count_gate_deps(gates)

    # From inspection, the general structure after the first couple bits is:
    # z{n} = (x{n} XOR y{n}) XOR (
    #           (y{n-1} AND x{n-1}) OR (<AND of operands of z{n-1} gate>)
    #        )
    # In particular, every z gate except the first or last must be an XOR gate where one of the arguments
    # is itself an XOR gate. Also, that argument XOR gate must have xy wires as arguments with indices that
    # match the z gate. Every XOR gate except the z00 gate must be one of these types.
    #
    # When set up properly, every zN gate besides the first couple and the last will depend on 6N arguments,
    # and there will be exactly one other non-z gate that depends on that many arguments.
    # The dependency counts of other types of gates can also be calculated, but I didn't need to use them.

    xor_gates = {gate: args for gate, args in gates.items() if args[2] == "XOR"}

    swaps = {z for z in z_labels[:-1] if z not in xor_gates}

    for gate, args in xor_gates.items():
        if gate == "z00":
            continue
        i1, i2, op = args
        if gate.startswith("z") + i1.startswith("x") != 1:
            swaps.add(gate)

    z_swaps = {swap for swap in swaps if swap.startswith("z")}
    non_z_swaps = swaps - z_swaps

    for z_swap in sorted(z_swaps):
        min_nz = min(non_z_swaps, key=lambda k: dep_counts[k])
        non_z_swaps.remove(min_nz)
        if dep_counts[min_nz] == int(z_swap[1:]) * 6:
            gates[z_swap], gates[min_nz] = gates[min_nz], gates[z_swap]

        dep_counts = count_gate_deps(gates)

    xor_gates = {}
    or_gates = {}
    reverse_gates = {}

    for gate, args in gates.items():
        reverse_gates[args] = gate
        if args[2] == "XOR":
            xor_gates[gate] = args
        elif args[2] == "OR":
            or_gates[gate] = args

    for idx, z in enumerate(z_labels[1:-1], 1):
        i1, i2, op = gates[z]
        xor_gate = reverse_gates[(x_labels[idx], y_labels[idx], "XOR")]
        if xor_gate not in [i1, i2]:
            swaps.add(xor_gate)
            if i1 in or_gates:
                swaps.add(i2)
            elif i2 in or_gates:
                swaps.add(i1)

    # One could do more checks on the AND gates and such, but this is all I needed for my input.

    return ",".join(sorted(swaps))


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

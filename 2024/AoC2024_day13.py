def part1(input_text: str):
    import re

    COST_A = 3
    COST_B = 1

    button_re = re.compile(r"Button [AB]: X\+(\d+), Y\+(\d+)")
    prize_re = re.compile(r"Prize: X=(\d+), Y=(\d+)")

    tokens = 0

    for machine in input_text.split("\n\n"):
        buttons_str = re.findall(button_re, machine)
        button_a, button_b = [float(r) + float(i) * 1j for r, i in buttons_str]

        prize_str = re.search(prize_re, machine).groups()
        prize = float(prize_str[0]) + float(prize_str[1]) * 1j

        b_conj = button_b.conjugate()
        b_mag2 = button_b * b_conj

        m = prize * b_conj
        n = button_a * b_conj

        for a in range(101):
            b = (m - a * n) / b_mag2
            if not b.imag and b.real.is_integer():
                tokens += a * COST_A + int(b.real) * COST_B
                break

    return tokens


def part2(input_text: str):
    import re

    COST_A = 3
    COST_B = 1
    POS_MOD = 10000000000000

    button_re = re.compile(r"Button [AB]: X\+(\d+), Y\+(\d+)")
    prize_re = re.compile(r"Prize: X=(\d+), Y=(\d+)")

    tokens = 0

    for machine in input_text.split("\n\n"):
        buttons_str = re.findall(button_re, machine)
        button_a, button_b = [float(r) + float(i) * 1j for r, i in buttons_str]

        prize_str = re.search(prize_re, machine).groups()
        prize = (float(prize_str[0]) + POS_MOD) + (float(prize_str[1]) + POS_MOD) * 1j

        # The problem amounts to finding an integer solution to the equation
        # a * button_a + b * button_b = prize, which implies
        # b = (prize - a * button_a) / button_b.
        # Let b0 and b1 be the values of b given by the above equation for a=0 and a=1.
        # imag(b) must be 0 for a valid solution and the equation is linear in a,
        # so we can find the value of a that satisfies this by solving
        # imag(b0) + a * imag(b1 - b0) = 0.
        # If a and the corresponding b are positive integers, the solution is valid.
        # This is essentially the logic of the following, modulo some
        # simplifications/alterations to reduce float precision issues.

        b_conj = button_b.conjugate()
        b_mag2 = (button_b * b_conj).real

        m = prize * b_conj
        n = button_a * b_conj

        c = m.imag
        delta_b = (button_a * b_conj).imag
        a = c / delta_b

        if a >= 0 and a.is_integer():
            b = (m.real - a * n.real) / b_mag2
            if b >= 0 and b.is_integer():
                tokens += a * COST_A + b * COST_B

    return int(tokens)


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

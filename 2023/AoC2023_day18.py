def part1(input_text: str):
    # guess I'll leave my original part 1 solution for posterity
    directions = {'D': 1, 'R': 1j, 'U': -1, 'L': -1j}
    trench = []
    lagoon = set()
    min_re = 0
    pos = 0

    for line in input_text.splitlines():
        d_text, n, rgb = line.split()
        d = directions[d_text]

        for __ in range(int(n)):
            trench.append((pos, d))
            lagoon.add(pos)
            pos += d
            re = pos.real
            min_re = min(re, min_re)

    # determine which orientation the loop is being traversed in
    top = 0

    for i in range(len(trench)):
        if trench[i][0].real == min_re:
            top = i
            break

    rot = trench[top][0] - trench[top+1][0]
    
    to_check = []

    for pos, v in trench:
        inside = pos + v * rot
        if inside not in lagoon:
            to_check.append(inside)
            lagoon.add(inside)

    # fill in the inside
    while to_check:
        pos = to_check.pop()

        for d in directions.values():
            new_pos = pos + d
            if new_pos not in lagoon:
                to_check.append(new_pos)
                lagoon.add(new_pos)

    return len(lagoon)


def part2(input_text: str):
    directions = {'1': 1, '0': 1j, '3': -1, '2': -1j}
    pos = 0
    trench_corners = [pos]
    re_set = set()
    im_set = set()

    for line in input_text.splitlines():
        _, _, rgb = line.split()
        n = int(rgb[2:7], 16)
        d = directions[rgb[7]]

        pos += n * d
        trench_corners.append(pos)
        re_set.add(pos.real)
        im_set.add(pos.imag)

    # Take the segments of the trench and extend them out into 
    # lines that form a grid. Either include or exclude the area 
    # of a grid cell based on whether it's inside or outside the loop. 
    # Careful with the edges.
    re_lines = sorted(re_set)
    re_lines.append(re_lines[-1] + 1.0)
    im_lines = sorted(im_set)
    im_lines.append(im_lines[-1] + 1.0)

    trench_points = {} # points where the trench intersects the grid
    counter = 0

    for p1, p2 in zip(trench_corners, trench_corners[1:]):
        if p1.real == p2.real:
            re = p1.real
            i1 = im_lines.index(p1.imag)
            i2 = im_lines.index(p2.imag)
            for im in im_lines[i1:i2:(1 if i1 < i2 else -1)]:
                trench_points[re + im*1j] = counter
                counter += 1
        else:
            im = p1.imag
            i1 = re_lines.index(p1.real)
            i2 = re_lines.index(p2.real)
            for re in re_lines[i1:i2:(1 if i1 < i2 else -1)]:
                trench_points[re + im*1j] = counter
                counter += 1

    max_count = counter - 1
    s = 0
    inside = False
    
    for re_u, re_d in zip(re_lines, re_lines[1:]):
        height = re_d - re_u
        for im_l, im_r in zip(im_lines, im_lines[1:]):
            width = im_r - im_l
            corner_ul = re_u + im_l*1j
            corner_dl = re_d + im_l*1j
            corner_ur = re_u + im_r*1j

            corner_incl = (corner_ul in trench_points)
            # gotta deal with edge cases where corner_ul and corner_dl aren't actually connected
            left_incl = (corner_incl and corner_dl in trench_points and \
                abs(trench_points[corner_ul] - trench_points[corner_dl]) in [1, max_count])
            up_incl = (corner_incl and corner_ur in trench_points and \
                abs(trench_points[corner_ul] - trench_points[corner_ur]) in [1, max_count])

            # because of the direction the grid is being scanned through, transitions from inside 
            # the loop to outside only occur when a vertical segment of the trench is crossed
            if left_incl:
                inside = not inside
            
            if inside:
                s += height * width
            else:
                s += corner_incl + (height - 1.0) * left_incl + (width - 1.0) * up_incl

    return int(s)


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2023_day18_input.txt') as f:
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
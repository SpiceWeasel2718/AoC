def part1(input_text: str):
    import re
    
    sensors = []
    beacons = set()
    
    for line in input_text.splitlines():
        sx, sy, bx, by = [int(s[1:]) for s in re.findall(r'=-?\d+', line)]
        sensors.append((sx + sy*1j, abs(bx-sx) + abs(by-sy)))
        beacons.add(bx + by*1j)
    
    y = 2000000
    min_x = int(min(s[0].real - s[1] for s in sensors))
    max_x = int(max(s[0].real + s[1] for s in sensors))
    count = 0
    
    for x in range(min_x, max_x + 1):
        pos = x + y*1j
        if pos in beacons:
            continue
        for s_pos, s_dist in sensors:
            diff = s_pos - pos
            if abs(diff.real) + abs(diff.imag) <= s_dist:
                count += 1
                break
    
    return count


def part2(input_text: str):
    import re
    
    sensors = []
    beacons = set()
    
    for line in input_text.splitlines():
        sx, sy, bx, by = [int(s[1:]) for s in re.findall(r'=-?\d+', line)]
        sensors.append((sx + sy*1j, abs(bx-sx) + abs(by-sy)))
        beacons.add(bx + by*1j)
    
    max_val = 4000000

    for s_pos, s_dist in sensors:
        for start, direction in [
                (s_pos + s_dist + 1, -1-1j),
                (s_pos - s_dist*1j - 1j, -1+1j),
                (s_pos - s_dist - 1, 1+1j),
                (s_pos + s_dist*1j + 1j, 1-1j),
                ]:
            pos = start
            for __ in range(s_dist + 1):
                if 0 <= pos.real <= max_val and 0 <= pos.imag <= max_val:
                    for test_pos, test_dist in sensors:
                        if test_pos == s_pos:
                            continue
                        diff = test_pos - pos
                        if abs(diff.real) + abs(diff.imag) <= test_dist:
                            break
                    else:
                        return int(pos.real * 4000000 + pos.imag)
                
                pos += direction


if __name__ == '__main__':
    with open('2022/input_files/AoC2022_day15_input.txt') as f:
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
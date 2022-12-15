def part1(input_text: str):
    import re
    
    intervals = set()
    beacons = set()
    y = 2000000
    
    for line in input_text.splitlines():
        sx, sy, bx, by = [int(s[0]) for s in re.finditer(r'-?\d+', line)]
        
        if by == y:
            beacons.add(bx)
        
        rad = abs(bx - sx) + abs(by - sy)
        dist = rad - abs(sy - y)
        if dist >= 0:
            left, right = sx - dist, sx + dist
            to_merge = []
            
            for interval in intervals:
                i_left, i_right = interval
                
                if any([i_left <= left <= i_right, 
                       i_left <= right <= i_right,
                       left <= i_left <= right,
                       left <= i_right <= right]):
                    
                    to_merge.append(interval)
            
            for interval in to_merge:
                intervals.remove(interval)
                i_left, i_right = interval
                left = min(left, i_left)
                right = max(right, i_right)
            
            intervals.add((left, right))
            
    return sum(r - l + 1 for l, r in intervals) - len(beacons)


def part2(input_text: str):
    import re
    
    sensors = []
    pos_slope = []
    neg_slope = []
    
    for line in input_text.splitlines():
        sx, sy, bx, by = [int(s[0]) for s in re.finditer(r'-?\d+', line)]
        dist = abs(bx - sx) + abs(by - sy) + 1
        sensors.append((sx, sy, dist))
        
        left = sx - dist
        pos_slope.append(left - sy)
        neg_slope.append(left + sy)
        right = sx + dist
        pos_slope.append(right - sy)
        neg_slope.append(right + sy)
        
    max_val = 4000000
    max_dist = 2 * max_val
    
    for pos in pos_slope:
        for neg in neg_slope:
            dist = abs(neg - pos)
            if dist <= max_dist and dist % 2 == 0:
                y = dist // 2
                x = min(pos, neg) + y
                if 0 <= x <= max_val:
                    for sx, sy, s_dist in sensors:
                        if abs(sx - x) + abs(sy - y) < s_dist:
                            break
                    else:
                        return x * 4000000 + y


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
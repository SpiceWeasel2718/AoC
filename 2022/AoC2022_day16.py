def part1(input_text: str):
    import re
    from itertools import combinations
    from collections import defaultdict
    
    rates = {}
    distances = {}

    for line in input_text.splitlines():
        words = re.split(r';?,? ', line)
        valve = words[1]
        rate = int(words[4][5:])
        nbrs = words[9:]
        
        rates[valve] = rate
        distances[valve] = {nbr: 1 for nbr in nbrs}
        
    zero = set()
    nonzero = set()
    for valve, rate in rates.items():
        if rate == 0:
            zero.add(valve)
        else:
            nonzero.add(valve)
    
    # trim the graph to remove all 0 nodes besides AA
    while zero:
        valve = zero.pop()
        for v1, v2 in combinations(distances[valve], 2):
            dist = distances[valve][v1] + distances[valve][v2]
            distances[v1].setdefault(v2, dist)
            distances[v1][v2] = min(distances[v1][v2], dist)
            distances[v2].setdefault(v1, dist)
            distances[v2][v1] = min(distances[v2][v1], dist)
        if valve != 'AA':
            for v in distances[valve]:
                del distances[v][valve]
            del distances[valve]

    # fill in all distances between nodes with Dijkstra
    eff_inf = len(rates)
    
    for valve in distances:
        unseen = set(distances)
        unseen.remove(valve)
        
        d = defaultdict(lambda : eff_inf)
        d[valve] = 0
        for v, dist in distances[valve].items():
            d[v] = dist
        
        while unseen:
            current = min(unseen, key=lambda x: d[x])
            for v in distances[current]:
                d[v] = min(d[v], d[current] + distances[current][v])
            unseen.remove(current)
        
        distances[valve] = d
    
    # brute force
    paths = []
    
    for v, dist in distances['AA'].items():
        current = v
        unseen = set(distances) - {'AA', v}
        time_left = 30 - dist - 1
        pressure = time_left * rates[v]
        paths.append((current, unseen, time_left, pressure))
    
    most_pressure = 0
    
    while paths:
        current, unseen, time_left, pressure = paths.pop()
        
        for v in unseen:
            new_time_left = time_left - distances[current][v] - 1
            
            if new_time_left >= 0:
                new_pressure = pressure + new_time_left * rates[v]
                most_pressure = max(most_pressure, new_pressure)
                if new_time_left > 0:
                    paths.append((v, unseen - {v}, new_time_left, new_pressure))

    return most_pressure
        
        
def part2(input_text: str):
    import re
    from itertools import combinations
    from collections import defaultdict
    
    rates = {}
    distances = {}

    for line in input_text.splitlines():
        words = re.split(r';?,? ', line)
        valve = words[1]
        rate = int(words[4][5:])
        nbrs = words[9:]
        
        rates[valve] = rate
        distances[valve] = {nbr: 1 for nbr in nbrs}
        
    zero = set()
    nonzero = set()
    for valve, rate in rates.items():
        if rate == 0:
            zero.add(valve)
        else:
            nonzero.add(valve)
    
    # trim the graph to remove all 0 nodes besides AA
    while zero:
        valve = zero.pop()
        for v1, v2 in combinations(distances[valve], 2):
            dist = distances[valve][v1] + distances[valve][v2]
            distances[v1].setdefault(v2, dist)
            distances[v1][v2] = min(distances[v1][v2], dist)
            distances[v2].setdefault(v1, dist)
            distances[v2][v1] = min(distances[v2][v1], dist)
        if valve != 'AA':
            for v in distances[valve]:
                del distances[v][valve]
            del distances[valve]

    # fill in all distances between nodes with Dijkstra
    eff_inf = len(rates)
    
    for valve in distances:
        unseen = set(distances)
        unseen.remove(valve)
        
        d = defaultdict(lambda : eff_inf)
        d[valve] = 0
        for v, dist in distances[valve].items():
            d[v] = dist
        
        while unseen:
            current = min(unseen, key=lambda x: d[x])
            for v in distances[current]:
                d[v] = min(d[v], d[current] + distances[current][v])
            unseen.remove(current)
        
        distances[valve] = d
    
    # brute force
    paths = []
    
    for u, e in combinations(distances['AA'].items(), 2):
        u_valve, u_dist = u
        e_valve, e_dist = e
        
        u_current = u_valve
        u_time_left = 26 - u_dist - 1
        e_current = e_valve
        e_time_left = 26 - e_dist - 1
        unseen = set(distances) - {'AA', u_valve, e_valve}
        pressure = u_time_left * rates[u_valve] + e_time_left * rates[e_valve]
        
        paths.append((u_current, e_current, u_time_left, e_time_left, unseen, pressure))
    
    most_pressure = 0
    
    while paths:
        u_current, e_current, u_time_left, e_time_left, unseen, pressure = paths.pop()
        
        for v in unseen:
            if u_time_left >= e_time_left:
                u_new_time_left = u_time_left - distances[u_current][v] - 1
                if u_new_time_left >= 0:
                    new_pressure = pressure + u_new_time_left * rates[v]
                    most_pressure = max(most_pressure, new_pressure)
                    if u_new_time_left > 0 and e_time_left > 0:
                        paths.append((v, e_current, u_new_time_left, e_time_left, unseen - {v}, new_pressure))
            else:
                e_new_time_left = e_time_left - distances[e_current][v] - 1
                if e_new_time_left >= 0:
                    new_pressure = pressure + e_new_time_left * rates[v]
                    most_pressure = max(most_pressure, new_pressure)
                    if e_new_time_left > 0 and u_time_left > 0:
                        paths.append((u_current, v, u_time_left, e_new_time_left, unseen - {v}, new_pressure))
            
    return most_pressure


if __name__ == '__main__':
    with open('2022/input_files/AoC2022_day16_input.txt') as f:
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
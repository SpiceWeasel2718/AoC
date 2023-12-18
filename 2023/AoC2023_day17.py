def part1(input_text: str):
    from itertools import count
    import heapq

    city = {}
    
    for a, line in enumerate(lines := input_text.splitlines()):
        for b, c in enumerate(line):
            city[a+b*1j] = int(c)
    
    end = len(lines)-1 + (len(lines[0])-1)*1j
    end_states = set()

    for v in [1, 1j]:
        for n in range(1, 4):
            end_states.add((end, v, n))

    # Time for Dijkstra
    counter = count() # needed so the heap can break ties
    seen = {}

    state = (1, 1, 1) # pos, last move direction, number of moves in that direction
    cost = city[1]
    element = [cost, next(counter), state]
    heap_elements = {state: element}
    heap = [element]

    state = (1j, 1j, 1)
    element = [city[1j], next(counter), state]
    heap_elements[state] = element
    heapq.heappush(heap, element)

    while heap and any(es not in seen for es in end_states):
        cost, __, state = heapq.heappop(heap)
        del heap_elements[state]
        pos, v, n = state
        seen[state] = cost
        
        valid_nbrs = [v*1j, -v*1j]
        if n < 3:
            valid_nbrs.append(v)

        for test_v in valid_nbrs:
            if (test_pos := pos + test_v) in city:
                test_state = (test_pos, test_v, (n + 1 if test_v == v else 1))

                if test_state not in seen:
                    test_cost = cost + city[test_pos]

                    if test_state not in heap_elements:
                        element = [test_cost, next(counter), test_state]
                        heap_elements[test_state] = element
                        heapq.heappush(heap, element)
                    elif test_cost < heap_elements[test_state][0]:
                        heap_elements[test_state][0] = test_cost
                        heapq.heapify(heap)
        
    return min(seen[state] for state in end_states)


def part2(input_text: str):
    from itertools import count
    import heapq

    city = {}
    
    for a, line in enumerate(lines := input_text.splitlines()):
        for b, c in enumerate(line):
            city[a+b*1j] = int(c)
    
    end = len(lines)-1 + (len(lines[0])-1)*1j
    end_states = set()

    for v in [1, 1j]:
        for n in range(4, 10):
            end_states.add((end, v, n))

    # Time for Dijkstra
    counter = count() # needed so the heap can break ties
    seen = {}

    state = (1, 1, 1) # pos, last move direction, number of moves in that direction
    cost = city[1]
    element = [cost, next(counter), state]
    heap_elements = {state: element}
    heap = [element]

    state = (1j, 1j, 1)
    element = [city[1j], next(counter), state]
    heap_elements[state] = element
    heapq.heappush(heap, element)

    while heap and any(es not in seen for es in end_states):
        cost, __, state = heapq.heappop(heap)
        del heap_elements[state]
        pos, v, n = state
        seen[state] = cost
        
        if n < 4:
            valid_nbrs = [v]
        elif 4 <= n < 10:
            valid_nbrs = [v, v*1j, -v*1j]
        else:
            valid_nbrs = [v*1j, -v*1j]

        for test_v in valid_nbrs:
            if (test_pos := pos + test_v) in city:
                test_state = (test_pos, test_v, (n + 1 if test_v == v else 1))

                if test_state not in seen:
                    test_cost = cost + city[test_pos]

                    if test_state not in heap_elements:
                        element = [test_cost, next(counter), test_state]
                        heap_elements[test_state] = element
                        heapq.heappush(heap, element)
                    elif test_cost < heap_elements[test_state][0]:
                        heap_elements[test_state][0] = test_cost
                        heapq.heapify(heap)
        
    return min(seen[state] for state in end_states if state in seen)


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2023_day17_input.txt') as f:
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
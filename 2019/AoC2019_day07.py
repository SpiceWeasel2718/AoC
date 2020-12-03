def part1(input_text):
    from intcode import IntComp
    from itertools import permutations

    computer = IntComp(input_text[0])
    
    maxval = 0

    for perm in permutations(range(5)):
        signal = 0
        
        for phase in perm:
            computer.reset()
            computer.append_inputs([phase, signal])
            computer.execute()
            signal = computer.outputs[-1]
        
        maxval = max(signal, maxval)
    
    return maxval


def part2(input_text):
    from intcode import IntComp
    from itertools import permutations
    import concurrent.futures

    amps = [IntComp(input_text[0]) for __ in range(5)]

    for i in range(5):
        amps[i].set_output_receiver(amps[(i+1) % 5])

    maxval = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for perm in permutations(range(5,10)):
            for amp, phase in zip(amps, perm):
                amp.reset()
                amp.append_inputs(phase)
            
            amps[0].append_inputs(0)
            
            results = [executor.submit(amp.execute) for amp in amps]
            
            maxval = max(results[4].result()[-1], maxval)
    
    return maxval


if __name__ == '__main__':
    from pathlib import Path
    with open(next(Path().glob('**/AoC2019_day07_input.txt'))) as f:
        input_text = f.read().split('\n')

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
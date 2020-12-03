import itertools
import math
import concurrent.futures

def repeat_time(positions, velocities):
    pairs = list(itertools.combinations(range(4), 2))

    state0 = [positions.copy(), velocities.copy()]
    t = 0

    while [positions, velocities] != state0 or t == 0:
        print(f'{positions}, {velocities}')
        t += 1
        grav = [0,0,0,0]

        for i, j in pairs:
            pos_i, pos_j = positions[i], positions[j]
            if pos_i < pos_j:
                grav[i] += 1
                grav[j] -= 1
            elif pos_i > pos_j:
                grav[i] -= 1
                grav[j] += 1
        
        for i in range(4):
            velocities[i] += grav[i]
            positions[i] += velocities[i]
    
    return t


def part1(input_text):
    positions = [[int(coord[2:]) for coord in line.strip('<>').split(', ')] for line in input_text]
    velocities = [[0]*3 for __ in range(4)]

    pairs = list(itertools.combinations(range(4), 2))
    
    for __ in range(1000):
        for coord in range(3):
            coord_positions = [pos[coord] for pos in positions]
            grav = [0,0,0,0]
            for i, j in pairs:
                pos_i, pos_j = coord_positions[i], coord_positions[j]
                if pos_i < pos_j:
                    grav[i] += 1
                    grav[j] -= 1
                elif pos_i > pos_j:
                    grav[i] -= 1
                    grav[j] += 1

            for i in range(4):
                velocities[i][coord] += grav[i]
                positions[i][coord] += velocities[i][coord]
    
    return sum(sum(abs(p) for p in pos)*sum(abs(v) for v in vel) for pos, vel in zip(positions, velocities))


def part2(input_text):
    positions = [[int(coord[2:]) for coord in line.strip('<>').split(', ')] for line in input_text]
    velocities = [[0]*3 for __ in range(4)]

    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        threads = [executor.submit(repeat_time, [pos[i] for pos in positions], [vel[i] for vel in velocities]) for i in range(3)]
        repeat_times = [thread.result() for thread in threads]
    
    result = 1
    for t in repeat_times:
        result = t * result // math.gcd(t, result)
    
    return result


if __name__ == '__main__':
    from pathlib import Path
    with open(next(Path().glob('**/AoC2019_day12_input.txt'))) as f:
        input_text = f.read().splitlines()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
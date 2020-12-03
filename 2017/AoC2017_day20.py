def part1(input_text):
    min_val = 100
    min_ind = 0
    for i, line in enumerate(input_text):
        a_modulus = sum(abs(int(n)) for n in line[line.rindex('a')+3 : -1].split(','))
        if a_modulus < min_val:
            min_val = a_modulus
            min_ind = i
        
    return min_ind


def part2(input_text):
    import collections

    input_text1 = """ p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>    
    p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
    p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
    p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0> """.splitlines()

    input_text2 = """ p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
    p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0> """.splitlines()
    

    def modulus(v):
        return sum(abs(coord) for coord in v)
    
    def pos(particle, t):
        return tuple(particle[i] + t*(particle[i+3] + t*particle[i+6]) for i in range(3))

    values = [tuple(int(n.strip('pva=<> ')) for n in line.split(',')) for line in input_text]
    particles = {v: v[:3] for v in values}
    
    t=1
    time_since_last_collision = 0

    while time_since_last_collision < 1000:
        count = collections.Counter(particles.values())

        if len(count) != len(particles):
            collisions = set(pos for pos, n in count.items() if n > 1)
            to_remove = set()
            for particle, pos in particles.items():
                if pos in collisions:
                    to_remove.add(particle)
            for particle in to_remove:
                particles.pop(particle)
            
            time_since_last_collision = 0
        
        for part, pos in particles.items():
            particles[part] = tuple(pos[i]+part[i+3]+t*part[i+6] for i in range(3))
        
        t += 1
        time_since_last_collision += 1
    
    return len(particles)
    

if __name__ == '__main__':
    from pathlib import Path
    with open(next(Path().glob('**/AoC2017_day20_input.txt'))) as f:
        input_text = f.read().splitlines()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    #print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    #print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
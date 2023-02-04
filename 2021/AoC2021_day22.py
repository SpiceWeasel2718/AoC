def part1(input_text):
    from collections import defaultdict
    
    instructions = []

    for line in input_text.splitlines():
        status = line.startswith('on')
        start_pt = []
        end_pt = []
        
        for dim in line.split(','):
            eq = dim.index('=')
            s, e = [int(n) for n in dim[eq+1:].split('..')]
            start_pt.append(s)
            end_pt.append(e)
        
        instructions.append((status, start_pt, end_pt))
    
    endpoint_sets = [set(), set(), set()]

    for inst in instructions:
        __, start_pt, end_pt = inst

        for s, e, pt_set in zip(start_pt, end_pt, endpoint_sets):
            if -50 <= s <= 50:
                pt_set.add(s)
            if -50 <= e <= 50:
                pt_set.add(e)
    
    endpoints = [sorted(p) for p in endpoint_sets]

    indices = []

    for dim in endpoints:
        d = {}
        
        for i, p in enumerate(dim):
            d[p] = i
        
        indices.append(d)
    


    for inst in instructions:
        pass

    breakpoint()

    return
    


def part2(input_text):
    pass


if __name__ == '__main__':
    with open('./input_files/AoC2021_day22_input.txt') as f:
        input_text = f.read()

    input_text = """on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
on x=967..23432,y=45373..81175,z=27513..53682"""

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    time_execution = 0

    if time_execution:
        import timeit
        for part in ['part1', 'part2']:
            timer = timeit.Timer(f'{part}(input_text)', globals=globals())
            n, time = timer.autorange()
            print(f'{part} took {time/n:.5f} seconds on average when run {n} times')
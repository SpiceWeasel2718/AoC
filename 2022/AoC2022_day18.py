def part1(input_text: str):
    droplet = set()
    
    surface = 0
    
    for line in input_text.splitlines():
        x, y, z = (int(n) for n in line.split(','))
        
        for nbr in [(x+1, y, z),
                    (x-1, y, z),
                    (x, y+1, z),
                    (x, y-1, z),
                    (x, y, z+1),
                    (x, y, z-1),]:
            
            surface += -1 if nbr in droplet else 1
        
        droplet.add((x, y, z))
        
    return surface
                

def part2(input_text: str):
    
    def get_nbrs(point):
        x, y, z = point
        return {(x+1, y, z),
                (x-1, y, z),
                (x, y+1, z),
                (x, y-1, z),
                (x, y, z+1),
                (x, y, z-1),}
    
    droplet = set()
    surface = 0
    
    for line in input_text.splitlines():
        point = tuple(int(n) for n in line.split(','))
        
        for nbr in get_nbrs(point):
            surface += -1 if nbr in droplet else 1
    
        droplet.add(point)
    
    boundary = set()
    
    for point in droplet:
        for nbr in get_nbrs(point):
            if nbr not in droplet:
                boundary.add(nbr)
    
    min_bounds = [len(droplet)] * 3
    max_bounds = [0] * 3
    
    for point in droplet:
        for i in range(3):
            min_bounds[i] = min(min_bounds[i], point[i])
            max_bounds[i] = max(max_bounds[i], point[i])
    
    interior = set()
    
    while boundary:
        start = next(iter(boundary))
        found_exterior = False
        component = set()
        queue = [start]
        
        while queue:
            point = queue.pop()
            nbrs = get_nbrs(point)
            
            if point in boundary or len(nbrs & boundary) > 0:
                component.add(point)
                queue.extend(nbr for nbr in nbrs if nbr not in component and nbr not in droplet)
                
                if not all(min_bounds[i] <= point[i] <= max_bounds[i] for i in range(3)):
                    found_exterior = True
        
        boundary_component = component & boundary
        boundary -= boundary_component
        
        if not found_exterior:
            interior |= boundary_component
            
    inner_surface = 0
        
    for point in interior:
        inner_surface += sum((nbr in droplet) for nbr in get_nbrs(point))
    
    return surface - inner_surface


if __name__ == '__main__':
    with open('2022/input_files/AoC2022_day18_input.txt') as f:
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
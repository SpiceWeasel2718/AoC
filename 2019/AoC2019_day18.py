import collections
import math

import numpy as np

def part1(input_text):
    
    def next_node(prev, pos):
        dist = 1
        

    # turn text into dict: {node_coords: {neighboring_node_coords: distance}}
    # nodes are points of interest: keys, doors, intersections, and dead ends    

    def build_maze(input_text):
        maze = {}
        seen = set()
        q = collections.deque()
        seen.add((1, 1))
        q.append([(1, 1), (1, 2)])

        while q:
            neighbor, dist, approach = next_node(*q.pop())



    

    for i, row in enumerate(input_text):
        for j, c in enumerate(row):
            if c == '#':
                continue
            
            elif c == '.':
                pass
            
            elif c.islower():
                pass
            
            elif c.isupper():
                pass
            
            elif c == '@':
                pos = (i, j)
            
        
    


        


def part2(input_text):
    pass


if __name__ == '__main__':
    from pathlib import Path
    with open(next(Path().glob('**/AoC2019_day18_input.txt'))) as f:
        input_text = f.read().splitlines()
        print(input_text)

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    #print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    #print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
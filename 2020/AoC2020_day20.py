from collections import defaultdict
import numpy as np

def part1(input_text):
    edges = defaultdict(list)
    tiles = {}

    for tile_text in input_text.rstrip().split('\n\n'):
        name, text = tile_text.split('\n', 1)
        edge_list = [text[:10], text[9::11], text[:-11:-1], text[-10::-11]]
        rev_edge_list = [edge[::-1] for edge in edge_list]
        tiles[name] = edge_list + rev_edge_list

        for edge in tiles[name]:
            edges[edge].append(name)
        
    product = 1
        
    for tile, edge_list in tiles.items():
        if sum(len(edges[e]) for e in edge_list) == 12:
            product *= int(tile[5:-1])
    
    return product
    

def part2(input_text):
    orig_tiles_to_edges = {}
    flipped_tiles_to_edges = {}
    orig_edges_to_tiles = defaultdict(list)
    flipped_edges_to_tiles = defaultdict(list)
    tile_contents = {}
    puzzle = {}

    for tile_text in input_text.rstrip().split('\n\n'):
        name, text = tile_text.split('\n', 1)
        orig_tiles_to_edges[name] = [text[:10], text[9::11], text[:-11:-1], text[-10::-11]]
        flipped_tiles_to_edges[name] = [text[9::-1], text[::11], text[-10:], text[::-11]]
        
        for edge in orig_tiles_to_edges[name]:
            orig_edges_to_tiles[edge].append(name)
        for edge in flipped_tiles_to_edges[name]:
            flipped_edges_to_tiles[edge].append(name)
        
        tile_contents[name] = np.array([[(c == '#') for c in line[1:-1]] for line in text.splitlines()[1:-1]])

    puzzle = None
    cur_col = tile_contents[name]
    top, right, bottom, left = orig_tiles_to_edges[name]
    top_name, right_name, bottom_name, left_name = name, name, name, name

    while right:
        while bottom:
            bottom = bottom[::-1]
            lo, lf = len(orig_edges_to_tiles[bottom]), len(flipped_edges_to_tiles[bottom])

            if lo + lf < 2:
                bottom = ''
            else:
                if lo == 2 or (lo == 1 and bottom_name not in orig_edges_to_tiles[bottom]):
                    bottom_name = [name for name in orig_edges_to_tiles[bottom] if name != bottom_name][0]
                    
                    new_edge_list = orig_tiles_to_edges[bottom_name]
                    turns = new_edge_list.index(bottom)
                    cur_col = np.concatenate((cur_col, np.rot90(tile_contents[bottom_name], turns)))
                    bottom = new_edge_list[(turns + 2) % 4]

                else:
                    bottom_name = [name for name in flipped_edges_to_tiles[bottom] if name != bottom_name][0]

                    new_edge_list = flipped_tiles_to_edges[bottom_name]
                    turns = new_edge_list.index(bottom)
                    cur_col = np.concatenate((cur_col, np.rot90(np.fliplr(tile_contents[bottom_name]), turns)))
                    bottom = new_edge_list[(turns + 2) % 4]

        while top:
            top = top[::-1]
            lo, lf = len(orig_edges_to_tiles[top]), len(flipped_edges_to_tiles[top])

            if lo + lf < 2:
                top = ''
            else:
                if lo == 2 or (lo == 1 and top_name not in orig_edges_to_tiles[top]):
                    top_name = [name for name in orig_edges_to_tiles[top] if name != top_name][0]
                    
                    new_edge_list = orig_tiles_to_edges[top_name]
                    turns = (new_edge_list.index(top) + 2) % 4
                    cur_col = np.concatenate((np.rot90(tile_contents[top_name], turns), cur_col))
                    top = new_edge_list[turns]

                else:
                    top_name = [name for name in flipped_edges_to_tiles[top] if name != top_name][0]

                    new_edge_list = flipped_tiles_to_edges[top_name]
                    turns = (new_edge_list.index(top) + 2) % 4
                    cur_col = np.concatenate((np.rot90(np.fliplr(tile_contents[top_name]), turns), cur_col))
                    top = new_edge_list[turns]

        puzzle = np.concatenate((puzzle, cur_col), 1) if puzzle is not None else cur_col

        right = right[::-1]
        lo, lf = len(orig_edges_to_tiles[right]), len(flipped_edges_to_tiles[right])

        if lo + lf < 2:
            right = ''
        else:
            if lo == 2 or (lo == 1 and right_name not in orig_edges_to_tiles[right]):
                right_name = [name for name in orig_edges_to_tiles[right] if name != right_name][0]
                top_name, bottom_name = right_name, right_name
                
                new_edge_list = orig_tiles_to_edges[right_name]
                turns = (new_edge_list.index(right) + 1) % 4
                top, right, bottom = [new_edge_list[(turns + i) % 4] for i in range(3)]
                cur_col = np.rot90(tile_contents[right_name], turns)
                right = new_edge_list[(turns + 1) % 4]

            else:
                right_name = [name for name in flipped_edges_to_tiles[right] if name != right_name][0]
                top_name, bottom_name = right_name, right_name
                
                new_edge_list = flipped_tiles_to_edges[right_name]
                turns = (new_edge_list.index(right) + 1) % 4
                top, right, bottom = [new_edge_list[(turns + i) % 4] for i in range(3)]
                cur_col = np.rot90(np.fliplr(tile_contents[right_name]), turns)
                right = new_edge_list[(turns + 1) % 4]
    
    while left:
        left = left[::-1]
        lo, lf = len(orig_edges_to_tiles[left]), len(flipped_edges_to_tiles[left])

        if lo + lf < 2:
            break
        else:
            if lo == 2 or (lo == 1 and left_name not in orig_edges_to_tiles[left]):
                left_name = [name for name in orig_edges_to_tiles[left] if name != left_name][0]
                top_name, bottom_name = left_name, left_name
                
                new_edge_list = orig_tiles_to_edges[left_name]
                turns = (new_edge_list.index(left) + 3) % 4
                bottom, left, top = [new_edge_list[(turns + i + 2) % 4] for i in range(3)]
                cur_col = np.rot90(tile_contents[left_name], turns)
                left = new_edge_list[(turns + 3) % 4]

            else:
                left_name = [name for name in flipped_edges_to_tiles[left] if name != left_name][0]
                top_name, bottom_name = left_name, left_name
                
                new_edge_list = flipped_tiles_to_edges[left_name]
                turns = (new_edge_list.index(left) + 3) % 4
                bottom, left, top = [new_edge_list[(turns + i + 2) % 4] for i in range(3)]
                cur_col = np.rot90(np.fliplr(tile_contents[left_name]), turns)
                left = new_edge_list[(turns + 3) % 4]

        while bottom:
            bottom = bottom[::-1]
            lo, lf = len(orig_edges_to_tiles[bottom]), len(flipped_edges_to_tiles[bottom])

            if lo + lf < 2:
                bottom = ''
            else:
                if lo == 2 or (lo == 1 and bottom_name not in orig_edges_to_tiles[bottom]):
                    bottom_name = [name for name in orig_edges_to_tiles[bottom] if name != bottom_name][0]
                    
                    new_edge_list = orig_tiles_to_edges[bottom_name]
                    turns = new_edge_list.index(bottom)
                    cur_col = np.concatenate((cur_col, np.rot90(tile_contents[bottom_name], turns)))
                    bottom = new_edge_list[(turns + 2) % 4]

                else:
                    bottom_name = [name for name in flipped_edges_to_tiles[bottom] if name != bottom_name][0]

                    new_edge_list = flipped_tiles_to_edges[bottom_name]
                    turns = new_edge_list.index(bottom)
                    cur_col = np.concatenate((cur_col, np.rot90(np.fliplr(tile_contents[bottom_name]), turns)))
                    bottom = new_edge_list[(turns + 2) % 4]

        while top:
            top = top[::-1]
            lo, lf = len(orig_edges_to_tiles[top]), len(flipped_edges_to_tiles[top])

            if lo + lf < 2:
                top = ''
            else:
                if lo == 2 or (lo == 1 and top_name not in orig_edges_to_tiles[top]):
                    top_name = [name for name in orig_edges_to_tiles[top] if name != top_name][0]
                    
                    new_edge_list = orig_tiles_to_edges[top_name]
                    turns = (new_edge_list.index(top) + 2) % 4
                    cur_col = np.concatenate((np.rot90(tile_contents[top_name], turns), cur_col))
                    top = new_edge_list[turns]

                else:
                    top_name = [name for name in flipped_edges_to_tiles[top] if name != top_name][0]

                    new_edge_list = flipped_tiles_to_edges[top_name]
                    turns = (new_edge_list.index(top) + 2) % 4
                    cur_col = np.concatenate((np.rot90(np.fliplr(tile_contents[top_name]), turns), cur_col))
                    top = new_edge_list[turns]

        puzzle = np.concatenate((cur_col, puzzle), 1) if puzzle is not None else cur_col
    
    sea_monster = '                  # \n#    ##    ##    ###\n #  #  #  #  #  #   '
    
    test = []
    t_h, t_w = 0, 0
    for i, line in enumerate(sea_monster.splitlines()):
        for j, c in enumerate(line):
            if c == '#':
                test.append((i, j))
                t_h = max(t_h, i+1)
                t_w = max(t_w, j+1)

    found = set()

    for __ in range(2):
        for ___ in range(4):
            for i in range(len(puzzle) - t_h):
                for j in range(len(puzzle[0]) - t_w):
                    if all([puzzle[i+x][j+y] for x, y in test]):
                        found.add((i, j))
            puzzle = np.rot90(puzzle)
        puzzle = np.fliplr(puzzle)

    return np.sum(puzzle) - len(found) * len(test)


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day20_input.txt') as f:
        input_text = f.read()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    time_execution = 1

    if time_execution:
        import timeit
        for part in ['part1', 'part2']:
            timer = timeit.Timer(f'{part}(input_text)', globals=globals())
            n, time = timer.autorange()
            print(f'{part} took {time/n:.5f} seconds on average when run {n} times')
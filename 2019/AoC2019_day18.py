from collections import deque, defaultdict
import itertools
import heapq
import math

def part1(input_text):
    class Node:
        def __init__(self, coords) -> None:
            self.coords = coords
            self.children = set()
            self.parents = set()
            self.keys = []
            self.gates = []
            self.cost = 0


    maze = {}
    gates = {}
    keys = {}
    start = 0

    for row, line in enumerate(input_text.rstrip().splitlines()):
        for col, c in enumerate(line.rstrip()):
            maze[(pos := row + col*1j)] = c
            if c.isalpha():
                if c.isupper():
                    gates[c] = pos
                else:
                    keys[c] = pos
            elif c == '@':
                start = pos

    directions = [1, 1j, -1, -1j]
    root = Node(start)
    nodes = {start: root}
    queue = deque([root])
    distances = defaultdict(dict)

    while queue:
        cur_node = queue.popleft()
        node_pos = cur_node.coords

        ways_out = [node_pos+d for d in directions if maze[node_pos+d] != '#']

        for pos in ways_out:
            prev_pos = node_pos
            nbrs = [pos+d for d in directions if maze[pos+d] != '#']
            dist = 1

            while maze[pos] == '.' and len(nbrs) == 2:
                prev_pos, pos = pos, nbrs[1] if nbrs[0] == prev_pos else nbrs[0] 
                nbrs = [pos+d for d in directions if maze[pos+d] != '#']
                
                dist += 1

            distances[node_pos][pos] = dist

            if pos in nodes:
                node = nodes[pos]
                cur_node.parents.add(node)
                node.children.add(cur_node)
            else:
                node = Node(pos)
                nodes[pos] = node
                cur_node.children.add(node)
                node.parents.add(cur_node)
                queue.append(node)

                if (c := maze[pos]).isalpha():
                    if c.isupper():
                        node.gates.append(c)
                    else:
                        node.keys.append(c)
    

    for pos in nodes:
        distances[pos][pos] = 0


    old_nodes = {}

    while len(nodes) != len(old_nodes):
        old_nodes = nodes.copy()

        for pos, node in old_nodes.items():
            if not node.children:
                if not node.keys:
                    for parent in node.parents:
                        nodes[parent.coords].children.discard(node)
                    del nodes[pos]

                elif len(node.parents) == 1:
                    parent_node = next(iter(node.parents))
                    if not node.gates or not parent_node.keys:
                        parent = parent_node.coords
                        
                        parent_node.gates.extend(node.gates)
                        parent_node.keys.extend(node.keys)
                        parent_node.cost += node.cost + 2 * distances[pos][parent]
                        parent_node.children.discard(node)
                        del nodes[pos]
        
            elif pos != start and len(node.parents) == 1 and len(node.children) == 1:
                parent_node = next(iter(node.parents))
                child_node = next(iter(node.children))
                
                if not node.keys:
                    parent = parent_node.coords
                    child = child_node.coords
                    
                    child_node.gates.extend(node.gates)

                    parent_node.children.discard(node)
                    child_node.parents.discard(node)
                    parent_node.children.add(child_node)
                    child_node.parents.add(parent_node)

                    distances[parent][child] = distances[pos][parent] + distances[pos][child]
                    distances[child][parent] = distances[parent][child]

                    del nodes[pos]
                    

    for pos in nodes:
        node_dists = distances[pos]
        seen = {pos}
        queue = deque(node_dists.keys() - seen)
        
        while queue:
            other_pos = queue.popleft()
            other_dists = distances[other_pos]
            seen.add(other_pos)

            for relation in other_dists:
                d = node_dists[other_pos] + other_dists[relation]
                node_dists.setdefault(relation, math.inf)
                node_dists[relation] = min(node_dists[relation], d)
                if relation not in seen:
                    queue.append(relation)
    
    
    paths = [(0, 0, set(), root, root.children, {root})]
    n_keys = len(keys)
    min_dist = math.inf
    count = 0
    seen = set()

    while paths:
        dist, ___, held_keys, node, next_nodes, path_seen = heapq.heappop(paths)
        pos = node.coords

        if len(held_keys) == n_keys:
            min_dist = min(dist, min_dist)
            continue
        
        for other_node in next_nodes:
            other_pos = other_node.coords
            if all(g.lower() in held_keys for g in other_node.gates) and other_node not in path_seen:
                d = dist + distances[pos][other_pos] + other_node.cost
                new_held_keys = held_keys.union(other_node.keys)
                new_path_seen = path_seen | {other_node}
                state = (d, other_pos, frozenset(new_held_keys))
                if d < min_dist and state not in seen:
                    count += 1
                    heapq.heappush(paths, (d, count, new_held_keys, other_node, (next_nodes | other_node.children) - new_path_seen, new_path_seen))
                    seen.add(state)

    return min_dist


def part2(input_text):
    class Node:
        def __init__(self, coords) -> None:
            self.coords = coords
            self.children = set()
            self.parents = set()
            self.keys = []
            self.gates = []
            self.cost = 0
        
        def __repr__(self) -> str:
            return f'Node({self.coords}, {self.keys}, {self.gates}, parents={[p.coords for p in self.parents]}, children={[c.coords for c in self.children]})'

    maze = {}
    gates = {}
    keys = {}
    starts = []

    for row, line in enumerate(input_text.rstrip().splitlines()):
        for col, c in enumerate(line.rstrip()):
            maze[(pos := row + col*1j)] = c
            if c.isalpha():
                if c.isupper():
                    gates[c] = pos
                else:
                    keys[c] = pos
            elif c == '@':
                starts.append(pos)

    start = starts.pop()
    for a, b in itertools.product([-1, 0, 1], [-1j, 0, 1j]):
        maze[start + a + b] = '#'
    for a, b in itertools.product([-1, 1], [-1j, 1j]):
        pos = start + a + b
        maze[pos] = '@'
        starts.append(pos)

    directions = [1, 1j, -1, -1j]
    roots = []
    nodes = {}
    distances = defaultdict(dict)

    for start in starts:
        root = Node(start)
        roots.append(root)
        nodes[start] = root
        queue = deque([root])

        while queue:
            cur_node = queue.popleft()
            node_pos = cur_node.coords

            ways_out = [node_pos+d for d in directions if maze[node_pos+d] != '#']

            for pos in ways_out:
                prev_pos = node_pos
                nbrs = [pos+d for d in directions if maze[pos+d] != '#']
                dist = 1

                while maze[pos] == '.' and len(nbrs) == 2:
                    prev_pos, pos = pos, nbrs[1] if nbrs[0] == prev_pos else nbrs[0] 
                    nbrs = [pos+d for d in directions if maze[pos+d] != '#']
                    
                    dist += 1

                distances[node_pos][pos] = dist

                if pos in nodes:
                    node = nodes[pos]
                    cur_node.parents.add(node)
                    node.children.add(cur_node)
                else:
                    node = Node(pos)
                    nodes[pos] = node
                    cur_node.children.add(node)
                    node.parents.add(cur_node)
                    queue.append(node)

                    if (c := maze[pos]).isalpha():
                        if c.isupper():
                            node.gates.append(c)
                        else:
                            node.keys.append(c)
    

    for pos in nodes:
        distances[pos][pos] = 0


    old_nodes = {}

    while len(nodes) != len(old_nodes):
        old_nodes = nodes.copy()

        for pos, node in old_nodes.items():
            if not node.children:
                if not node.keys:
                    for parent in node.parents:
                        nodes[parent.coords].children.discard(node)
                    del nodes[pos]

            elif pos not in starts and len(node.parents) == 1 and len(node.children) == 1:
                parent_node = next(iter(node.parents))
                child_node = next(iter(node.children))
                
                if not node.keys:
                    parent = parent_node.coords
                    child = child_node.coords
                    
                    child_node.gates.extend(node.gates)

                    parent_node.children.discard(node)
                    child_node.parents.discard(node)
                    parent_node.children.add(child_node)
                    child_node.parents.add(parent_node)

                    distances[parent][child] = distances[pos][parent] + distances[pos][child]
                    distances[child][parent] = distances[parent][child]

                    del nodes[pos]
                    
    
    for pos in nodes:
        node_dists = distances[pos]
        seen = {pos}
        queue = deque(node_dists.keys() - seen)
        
        while queue:
            other_pos = queue.popleft()
            other_dists = distances[other_pos]
            seen.add(other_pos)

            for relation in other_dists:
                d = node_dists[other_pos] + other_dists[relation]
                node_dists.setdefault(relation, math.inf)
                node_dists[relation] = min(node_dists[relation], d)
                if relation not in seen:
                    queue.append(relation)
    

    next_nodes = set()
    for root in roots:
        next_nodes |= root.children
    paths = [(0, 0, set(), tuple(roots), next_nodes, set(roots))]
    n_keys = len(keys)
    min_dist = math.inf
    count = 0
    seen = set()

    while paths:
        dist, ___, held_keys, cur_nodes, next_nodes, path_seen = heapq.heappop(paths)
        positions = [node.coords for node in cur_nodes]
        
        if len(held_keys) == n_keys:
            min_dist = min(dist, min_dist)
            continue
        
        for other_node in next_nodes:
            other_pos = other_node.coords
            if all(g.lower() in held_keys for g in other_node.gates) and other_node not in path_seen:
                for pos in positions:
                    if pos in distances[other_pos]:
                        d = dist + distances[pos][other_pos] + other_node.cost
                        break

                new_held_keys = held_keys.union(other_node.keys)
                new_path_seen = path_seen | {other_node}
                state = (d, other_pos, frozenset(new_held_keys))
                if d < min_dist and state not in seen:
                    count += 1
                    new_nodes = [nodes[p] for p in positions if p != pos]
                    new_nodes.append(other_node)
                    heapq.heappush(paths, (d, count, new_held_keys, new_nodes, (next_nodes | other_node.children) - new_path_seen, new_path_seen))
                    seen.add(state)

    return min_dist


if __name__ == '__main__':
    from pathlib import Path
    with open(next(Path().glob('**/AoC2019_day18_input.txt'))) as f:
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
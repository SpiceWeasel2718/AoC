def part1(input_text: str):
    
    class Blueprint:
        def __init__(self, bp_id=0, bots=(1, 0, 0, 0), resources=(0, 0, 0, 0), costs=None, time=0):
            self.id = bp_id
            self.bots = list(bots)
            self.resources = list(resources)
            self.costs = costs
            self.time = time
            self.build_bot = [
                self.build_ore_bot, 
                self.build_clay_bot, 
                self.build_obsid_bot, 
                self.build_geode_bot,
                ]
        
        def gather(self):
            self.time += 1
            for i in range(4):
                self.resources[i] += self.bots[i]
        
        def build_ore_bot(self):
            if self.resources[0] >= self.costs[0]:
                self.resources[0] -= self.costs[0]
                self.gather()
                self.bots[0] += 1
                return True
            else:
                self.gather()
                return False
        
        def build_clay_bot(self):
            if self.resources[0] >= self.costs[1]:
                self.resources[0] -= self.costs[1]
                self.gather()
                self.bots[1] += 1
                return True
            else:
                self.gather()
                return False
        
        def build_obsid_bot(self):
            if self.resources[0] >= self.costs[2][0] and self.resources[1] >= self.costs[2][1]:
                self.resources[0] -= self.costs[2][0]
                self.resources[1] -= self.costs[2][1]
                self.gather()
                self.bots[2] += 1
                return True
            else:
                self.gather()
                return False
        
        def build_geode_bot(self):
            if self.resources[0] >= self.costs[3][0] and self.resources[2] >= self.costs[3][1]:
                self.resources[0] -= self.costs[3][0]
                self.resources[2] -= self.costs[3][1]
                self.gather()
                self.bots[3] += 1
                return True
            else:
                self.gather()
                return False
        
        def copy(self):
            return Blueprint(self.id, tuple(self.bots), tuple(self.resources), self.costs, self.time)
        
    
    blueprints = []
    
    for line in input_text.splitlines():
        words = line.split()
        
        bp = Blueprint()
        bp.id = int(words[1][:-1])
        
        ore_cost = int(words[6])
        clay_cost = int(words[12])
        obsid_cost = (int(words[18]), int(words[21]))
        geode_cost = (int(words[27]), int(words[30]))
        
        bp.costs = (ore_cost, clay_cost, obsid_cost, geode_cost)
        
        blueprints.append(bp)
        
    total = 0
    
    for base_bp in blueprints:
        queue = [(base_bp.copy(), 0), (base_bp.copy(), 1)]
        
        ore_cost, clay_cost, obsid_cost, geode_cost = bp.costs
        max_bots = [
            max(ore_cost, clay_cost, obsid_cost[0], geode_cost[0]),
            obsid_cost[1],
            geode_cost[1],
            24
        ]
        
        max_geodes = 0
        
        while queue:
            bp, next_build = queue.pop()
            build_success = bp.build_bot[next_build]()
            
            if bp.time < 24:
                if build_success:
                    for i in range(4):
                        if bp.bots[i] < max_bots[i]:
                            queue.append((bp.copy(), i))
                else:
                    queue.append((bp, next_build))
            else:
                max_geodes = max(max_geodes, bp.resources[3])
        
        total += base_bp.id * max_geodes

    return total


def part2(input_text: str):
    from math import ceil
    import heapq
    
    class Blueprint:
        def __init__(self, bp_id=0, bots=(1, 0, 0, 0), resources=(0, 0, 0, 0), costs=None, time=32):
            self.id = bp_id
            self.bots = list(bots)
            self.resources = list(resources)
            self.costs = costs
            self.time = time
            self.finished = False
            
            self.build_bot = [
                self.build_ore_bot, 
                self.build_clay_bot, 
                self.build_obsid_bot, 
                self.build_geode_bot,
                ]
        
        def gather(self, t):
            self.time -= t
            for i in range(4):
                self.resources[i] += self.bots[i] * t
        
        def build_ore_bot(self):
            t = ceil(max(0, (self.costs[0] - self.resources[0])) / self.bots[0]) + 1
            
            if self.time >= t:
                self.gather(t)
                self.resources[0] -= self.costs[0]
                self.bots[0] += 1
            else:
                self.gather(self.time)
                self.finished = True
        
        def build_clay_bot(self):
            t = self.time_to_clay()
            
            if self.time >= t:
                self.gather(t)
                self.resources[0] -= self.costs[1]
                self.bots[1] += 1
            else:
                self.gather(self.time)
                self.finished = True
                
        def time_to_clay(self):
            return ceil(max(0, (self.costs[1] - self.resources[0])) / self.bots[0]) + 1
        
        def build_obsid_bot(self):
            t = self.time_to_obsid()
            
            if self.time >= t:
                self.gather(t)
                self.resources[0] -= self.costs[2][0]
                self.resources[1] -= self.costs[2][1]
                self.bots[2] += 1
            else:
                self.gather(self.time)
                self.finished = True
        
        def time_to_obsid(self):
            if self.bots[1] > 0:
                r1 = max(0, (self.costs[2][0] - self.resources[0])) / self.bots[0]
                r2 = max(0, (self.costs[2][1] - self.resources[1])) / self.bots[1]
                return ceil(max(r1, r2)) + 1
            else:
                return self.time_to_clay() + self.costs[2][1] + 1
        
        def build_geode_bot(self):
            t = self.time_to_geode()
            
            if self.time >= t:
                self.gather(t)
                self.resources[0] -= self.costs[3][0]
                self.resources[2] -= self.costs[3][1]
                self.bots[3] += 1
            else:
                self.gather(self.time)
                self.finished = True
        
        def time_to_geode(self):
            if self.bots[2] > 0:
                r1 = max(0, (self.costs[3][0] - self.resources[0])) / self.bots[0]
                r2 = max(0, (self.costs[3][1] - self.resources[2])) / self.bots[2]
                return ceil(max(r1, r2)) + 1
            else:
                return self.time_to_obsid() + self.costs[3][1] + 1
        
        def __lt__(self, other):
            return self.resources[3] > other.resources[3]
        
        def copy(self):
            return Blueprint(self.id, tuple(self.bots), tuple(self.resources), self.costs, self.time)
    
    
    blueprints = []
    
    for line in input_text.splitlines()[:3]:
        words = line.split()
        
        bp = Blueprint()
        bp.id = int(words[1][:-1])
        
        ore_cost = int(words[6])
        clay_cost = int(words[12])
        obsid_cost = (int(words[18]), int(words[21]))
        geode_cost = (int(words[27]), int(words[30]))
        
        bp.costs = (ore_cost, clay_cost, obsid_cost, geode_cost)
        
        blueprints.append(bp)
        
    total = 1
    
    for base_bp in blueprints:
        bp = base_bp.copy()
        queue = [bp]
        
        ore_cost, clay_cost, obsid_cost, geode_cost = bp.costs
        max_bots = [
            max(ore_cost, clay_cost, obsid_cost[0], geode_cost[0]) + 1,
            obsid_cost[1] + 1,
            geode_cost[1] + 1,
            32,
            ]
        
        max_geodes = 0
        
        while queue:
            bp = heapq.heappop(queue)
            
            for i in range(4):
                if (i == 0 or bp.bots[i-1] > 0) and bp.bots[i] < max_bots[i]:
                    next_bp = bp.copy()
                    next_bp.build_bot[i]()
                    
                    if next_bp.finished:
                        max_geodes = max(max_geodes, next_bp.resources[3])
                    else:
                        if next_bp.time < 6 and next_bp.bots[3] == 0:
                            continue
                        geode_est = next_bp.resources[3] + next_bp.bots[3] * next_bp.time
                        t = next_bp.time - next_bp.time_to_geode() // 2 + 1
                        geode_est += t * (t + 1) // 2
                        
                        if geode_est >= max_geodes:
                            heapq.heappush(queue, next_bp)
        
        total *= max_geodes

    return total


if __name__ == '__main__':
    with open('2022/input_files/AoC2022_day19_input.txt') as f:
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
class Solution:
    def __init__(self):
        self.input_text = 'xlqgujun'

    def knot_hash(self, key_string):
        lengths = [ord(c) for c in key_string] + [17, 31, 73, 47, 23]
        skip_size = 0
        start = 0
        loop = list(range(256))

        for i in range(64):
            for length in lengths:
                if length:
                    loop = loop[length:] + loop[length-1::-1]
                loop = loop[skip_size:] + loop[:skip_size]
                start = (start - length - skip_size) % 256
                skip_size = (skip_size+1) % 256
        
        loop = loop[start:] + loop[:start]
        knot_hash = ''

        for i in range(0,256,16):
            temp = loop[i]
            for j in range(1,16):
                temp ^= loop[i+j]
            knot_hash += ('0' + hex(temp)[2:])[-2:]

        return knot_hash


    def part1(self):
        key_string = self.input_text + '-'

        count = 0

        for i in range(128):
            for c in self.knot_hash(key_string + str(i)):
                for d in format(int(c, 16), 'b'):
                    if d == '1':
                        count += 1
        
        print(count)

        
    def part2(self):
        used = set()

        key_string = self.input_text + '-'

        for i in range(128):
            pos = 0
            for c in self.knot_hash(key_string + str(i)):
                for d in ('000' + format(int(c, 16), 'b'))[-4:]:
                    if d == '1':
                        used.add((i, pos))
                    pos += 1
        
        def get_neighbors(p):
            return {(p[0]+1, p[1]), (p[0]-1, p[1]), (p[0], p[1]+1), (p[0], p[1]-1)}

        def remove_group(p):
            queue = {p}
            while len(queue) > 0:
                cell = queue.pop()
                used.discard(cell)
                for neighbor in get_neighbors(cell):
                    if neighbor in used:
                        queue.add(neighbor)
        
        groups = 0
         
        while len(used) > 0:
            remove_group(used.pop())
            groups += 1
         
        print(groups)
        

Solution().part2()
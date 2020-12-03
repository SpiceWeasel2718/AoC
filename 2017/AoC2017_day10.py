class Solution:
    def __init__(self):
        self.input_text = '106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36'

    def part1(self):
        skip_size = 0
        start = 0
        loop = list(range(256))

        for length in [int(val) for val in self.input_text.split(',')]:
            if length:
                loop = loop[length:] + loop[length-1::-1]
            loop = loop[skip_size:] + loop[:skip_size]
            start = (start - length - skip_size) % 256
            skip_size += 1
        
        print(loop[start] * loop[(start+1) % 256])

        
    def part2(self):
        lengths = [ord(c) for c in self.input_text] + [17, 31, 73, 47, 23]
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

        print(knot_hash)
            

Solution().part2()
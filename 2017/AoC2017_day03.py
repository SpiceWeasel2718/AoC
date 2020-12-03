class Solution:
    def __init__(self):
        self.input_value = 347991

    def part1(self):
        import math

        """
        input_value lies just outside the edge of some square of odd side length centered at 1.
        Let inner_sqare be the side length of this square. max_dist is the least upper bound for the 
        distance from input_value to 1. Partition the edges of the smallest square containing 
        input_value into four segments of length pos_range, which stretch from each corner up to 
        but not containing the next corner, going counterclockwise. Let position be the index of 
        input_value within the segment containing it (the case where input_value is a perfect odd square 
        is handled differently). Calculating dist is then just counting.
        """

        inner_square = math.floor(math.sqrt(self.input_value))
        inner_square -= (inner_square + 1) % 2
        
        if self.input_value == inner_square ** 2:
            print(2 * (inner_square // 2))
            return

        max_dist = 2 * ((inner_square + 1) // 2)
        pos_range = inner_square + 1
        position = (self.input_value - inner_square ** 2) % pos_range
        dist = max_dist - min(position, pos_range // 2) + max(position - pos_range // 2, 0)
        
        print(dist)


    def part2(self):
        neighbors = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]

        def ptwise_sum(t1, t2):
            return tuple(t1[i] + t2[i] for i in range(2))
        
        def rotate(t):
            return (-t[1], t[0])

        values = {(0, 0): 1}
        current = (0, 0)
        value = 0
        direction = (1, 0)
        n = 1
        pos_count = 0
        seg_count = 0

        while value <= self.input_value:
            current = ptwise_sum(current, direction)
            
            pos_count += 1
            
            if pos_count == n:
                pos_count = 0
                seg_count += 1
                
                direction = rotate(direction)
                
                if seg_count == 2:
                    seg_count = 0
                    n += 1

            value = 0

            for neighbor in neighbors:
                try:
                    value += values[ptwise_sum(current, neighbor)]
                except KeyError:
                    continue

            values[current] = value

            print(f'\r{current}: {value}', end='')
            

Solution().part1()


    
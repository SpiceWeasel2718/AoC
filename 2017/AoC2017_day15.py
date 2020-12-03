class Solution:
    def __init__(self):
        self.input_text = 'Generator A starts with 512\nGenerator B starts with 191'

    def part1(self):
        def A():
            n = 512
            while True:
                n = (n*16807) % 2147483647
                yield n

        def B():
            n = 191
            while True:
                n = (n*48271) % 2147483647
                yield n
        
        judge = 0
        a = A()
        b = B()

        for i in range(40000000):
            judge += next(a) & 65535 == next(b) & 65535
        
        print(judge)

        
    def part2(self):
        def A():
            n = 512
            while True:
                n = (n*16807) % 2147483647
                if n % 4 == 0:
                    yield n

        def B():
            n = 191
            while True:
                n = (n*48271) % 2147483647
                if n % 8 == 0:
                    yield n
        
        judge = 0
        a = A()
        b = B()

        for i in range(5000000):
            judge += next(a) & 65535 == next(b) & 65535
        
        print(judge)
            

Solution().part2()
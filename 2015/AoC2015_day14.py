f = open("input_files/AoC2015_day14_input.txt")
input_text = f.read().split("\n")
f.close()

time_limit = 2503


class Reindeer:
    def __init__(self, string):
        data = string.split()
        self.name = data[0]
        self.speed = int(data[3])
        self.move_time = int(data[6])
        self.rest_time = int(data[13])
        self.dist = 0
        self.is_flying = 1
        self.fly_count = 0
        self.rest_count = 0
        self.score = 0


reindeer = [Reindeer(line) for line in input_text]
scores = len(reindeer)*[0]

for i in range(time_limit):
    for r in reindeer:
        if r.is_flying:
            r.dist += r.speed
        r.fly_count += r.is_flying
        r.rest_count += (r.is_flying + 1) % 2
        if r.fly_count == r.move_time:
            r.fly_count = 0
            r.is_flying = 0
        if r.rest_count == r.rest_time:
            r.rest_count = 0
            r.is_flying = 1

    max_dist = max([r.dist for r in reindeer])
    for r in reindeer:
        if r.dist == max_dist:
            r.score += 1


for r in reindeer:
    print(r.name, r.score)




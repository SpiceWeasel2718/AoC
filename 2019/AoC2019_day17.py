from intcode import IntComp
import concurrent.futures
import collections

def part1(input_text):
    computer = IntComp(input_text[0])
    output = computer.execute()

    line_len = output.index(10) + 1
    lines = []

    for i in range(len(output) // line_len):
        lines.append(output[i*line_len : (i+1)*line_len])

    total = 0

    for y in range(1, len(lines) - 1):
        for x in range(1, line_len - 2):
            if lines[y][x] == 35 and all(lines[y+dy][x+dx] == 35 for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]):
                total += x * y

    return total


def part2(input_text):
    computer = IntComp(input_text[0])
    computer.program[0] = 2


    def instructions(computer):
        # computer.waiting_on_input.wait()
        # output = computer.outputs
        # line_len = output.index(10) + 1

        # direction_vectors = {'^': (0, -1), '>': (1, 0), 'v': (0, -1), '<': (-1, 0)}

        # for c in direction_vectors:
        #     try:
        #         ind = output.index(ord(c))
        #         pos = (ind % line_len, ind // line_len)  # (x, y)
        #         direction = direction_vectors[c]
        #         break
        #     except ValueError:
        #         pass
        
        # path = collections.defaultdict(bool)
        # path[pos] = True

        # for i in range(len(output)):
        #     if output[i] == 35:
        #         path[(i % line_len, i // line_len)] = True
        

        # def vadd(v, w):
        #     return (v[0] + w[0], v[1] + w[1])

        # def get_nbrs(pos):
        #     return [vadd(pos, v) for v in [(0, -1), (1, 0), (0, -1), (-1, 0)]]

        # inputs = []
        # distance = 0

        # while True:
        #     if vadd(pos, direction) in path:
        #         distance += 1
        #         pos = vadd(pos, direction)
        #     else:
        #         if distance > 0:
        #             inputs.append(str(distance))
        #         distance = 0
        #         if vadd(pos, (direction[1], -direction[0])) in path:
        #             inputs.append('L')  # flipped because "up" is the -y direction
        #             direction = (direction[1], -direction[0])
        #         elif vadd(pos, (-direction[1], direction[0])) in path:
        #             inputs.append('R')
        #             direction = (-direction[1], direction[0])
        #         else:
        #             break
        
        # string = ''.join(inputs)
        
        # a_guess = inputs[:12]
        # while len(','.join(a_guess)) > 20:
        #     a_guess.pop()

        # solved = False

        # while not solved:
        #     remainder =''.join(string.split(''.join(a_guess)))

        



        # main
        M = [ord(c) for c in 'A,C,A,B,A,B,C,B,B,C\n']

        # A
        A = [ord(c) for c in 'L,4,L,4,L,10,R,4\n']

        # B
        B = [ord(c) for c in 'R,4,L,10,R,10\n']

        # C
        C = [ord(c) for c in 'R,4,L,4,L,4,R,8,R,10\nn\n']

        for code in M+A+B+C:
            computer.waiting_on_input.wait()
            computer.append_inputs(code)


    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(instructions, computer)
        return executor.submit(computer.execute).result()[-1]
    

if __name__ == '__main__':
    from pathlib import Path
    with open(next(Path().glob('**/AoC2019_day17_input.txt'))) as f:
        input_text = f.read().splitlines()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    #print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    #print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
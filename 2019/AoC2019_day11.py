from intcode import IntComp
import collections
import concurrent.futures

def part1(input_text):
    program = input_text[0]

    computer = IntComp(program)
    
    def run_robot(computer):
        panel = collections.defaultdict(int)
        pos = (0,0)
        direction = (0,1)

        while not computer.halted:
            computer.append_inputs(panel[pos])
            computer.waiting_on_input.wait()
            color, turn = computer.outputs[-2:]
            panel[pos] = color
            direction = (direction[1], -direction[0]) if turn else (-direction[1], direction[0])
            pos = (pos[0] + direction[0], pos[1] + direction[1])
        
        return len(panel)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(computer.execute)
        return executor.submit(run_robot, computer).result()
    

def part2(input_text):
    program = input_text[0]

    computer = IntComp(program)
    
    def run_robot(computer):
        panel = collections.defaultdict(int)
        pos = (0,0)
        direction = (0,1)
        panel[pos] = 1

        while not computer.halted:
            computer.append_inputs(panel[pos])
            computer.waiting_on_input.wait()
            color, turn = computer.outputs[-2:]
            panel[pos] = color
            direction = (direction[1], -direction[0]) if turn else (-direction[1], direction[0])
            pos = (pos[0] + direction[0], pos[1] + direction[1])
        
        return panel

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(computer.execute)
        panel = executor.submit(run_robot, computer).result()
    
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0

    for pos in panel:
        min_x = min(pos[0], min_x)
        min_y = min(pos[1], min_y)
        max_x = max(pos[0], max_x)
        max_y = max(pos[1], max_y)
    
    reps = {0: '.', 1: '#'}
    panel_string = [' ']
    for y in range(max_y, min_y-1, -1):
        line = [reps[panel[(x, y)]] for x in range(min_x, max_x+1)]
        panel_string.append(''.join(line))

    return '\n'.join(panel_string)


if __name__ == '__main__':
    from pathlib import Path
    with open(next(Path().glob('**/AoC2019_day11_input.txt'))) as f:
        input_text = f.read().splitlines()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
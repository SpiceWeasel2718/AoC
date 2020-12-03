import collections
from intcode import IntComp
import concurrent.futures
import time

def part1(input_text):
    computer = IntComp(input_text[0])
    outputs = computer.execute()

    count = 0

    for tile in outputs[2::3]:
        if tile == 2:
            count += 1
    
    return count


def part2(input_text):
    computer = IntComp(input_text[0])
    computer.program[0] = 2
    computer.set_event_timeout(2)

    display_screen = False

    def run_game(computer, display_screen=False):
        computer.waiting_on_input.wait()
        
        outputs = computer.outputs.copy()
        computer.outputs.clear()

        if display_screen == True:
            x_max = max(outputs[::3])
            y_max = max(outputs[1::3])
            screen = [['']*(x_max+1) for __ in range(y_max+1)]
            tiles = {0: '.', 1: 'X', 2: 'B', 3: '#', 4: '0'}
        
        score = 0

        while True:
            if display_screen == True:
                for x, y, tile in zip(outputs[::3], outputs[1::3], outputs[2::3]):
                    if x == -1 and y == 0:
                        score = tile
                    else:
                        screen[y][x] = tiles[tile]
                        if tile == 4:
                            ball_x = x
                        elif tile == 3:
                            paddle_x = x
                
                print(' ')
                for row in screen:
                    print(''.join(row))
                print('Score:', score)
                time.sleep(0.1)

            else:
                for x, tile in zip(outputs[::3], outputs[2::3]):
                    if x == -1:
                        score = tile
                    elif tile == 3:
                        paddle_x = x
                    elif tile == 4:
                        ball_x = x

            if computer.halted == True:
                break

            if ball_x > paddle_x:
                joystick = 1
            elif ball_x < paddle_x:
                joystick = -1
            else:
                joystick = 0

            computer.append_inputs(joystick)

            computer.waiting_on_input.wait()

            outputs = computer.outputs.copy()
            computer.outputs.clear()
        
        return score
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(computer.execute)
        res = executor.submit(run_game, computer, display_screen)
    
    return res.result()
            

if __name__ == '__main__':
    from pathlib import Path
    with open(next(Path().glob('**/AoC2019_day13_input.txt'))) as f:
        input_text = f.read().splitlines()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    import timeit
    p1_timer = timeit.Timer('part1(input_text)', globals=globals())
    p2_timer = timeit.Timer('part2(input_text)', globals=globals())
    print(f'part1 took at least {min(p1_timer.repeat(number=1)) :.5f} seconds')
    print(f'part2 took at least {min(p2_timer.repeat(number=1)) :.5f} seconds')
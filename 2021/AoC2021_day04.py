def part1(input_text):
    draw_text, *board_text = input_text.split('\n\n')
    draws = [int(n) for n in draw_text.split(',')]
    boards = [[int(n) for n in board.split()] for board in board_text]
    
    def check_win(board, draw_set):
        for offset in range(5):
            if all((board[i] in draw_set) for i in range(5*offset, 5*(offset+1))):
                return True
            if all((board[i] in draw_set) for i in range(offset, offset+21, 5)):
                return True
        return False
    
    right = len(draws)
    left = 1
    winners = boards

    while right - left > 1:
        mid = (left + right) // 2
        draw_set = set(draws[:mid])
        new_winners = [board for board in winners if check_win(board, draw_set)]
        
        if new_winners:
            winners = new_winners
            right = mid
        else:
            left = mid

    scores = []
    
    for board in winners:
        scores.append(draws[right-1] * sum(n for n in board if n not in set(draws[:right])))
    
    return max(scores)


def part2(input_text):
    draw_text, *board_text = input_text.split('\n\n')
    draws = [int(n) for n in draw_text.split(',')]
    boards = [[int(n) for n in board.split()] for board in board_text]
    
    def check_loss(board, draw_set):
        for offset in range(5):
            if all((board[i] in draw_set) for i in range(5*offset, 5*(offset+1))):
                return False
            if all((board[i] in draw_set) for i in range(offset, offset+21, 5)):
                return False
        return True
    
    right = len(draws)
    left = 1
    losers = boards

    while right - left > 1:
        mid = (left + right) // 2
        draw_set = set(draws[:mid])
        new_losers = [board for board in losers if check_loss(board, draw_set)]
        
        if new_losers:
            losers = new_losers
            left = mid
        else:
            right = mid

    last_board = losers[0]

    return draws[right-1] * sum(n for n in last_board if n not in draw_set)


if __name__ == '__main__':
    with open('./input_files/AoC2021_day04_input.txt') as f:
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
def part1(input_text: str):
    s = 0

    for line in input_text.splitlines():
        win_text, have_text = line[10:].split(' | ')
        wins = set(win_text.split())
        haves = set(have_text.split())
        have_wins = wins & haves
        if have_wins:
            s += 2 ** (len(have_wins) - 1)
    
    return s


def part2(input_text: str):
    card_wins = []

    for line in input_text.splitlines():
        win_text, have_text = line[10:].split(' | ')
        wins = set(win_text.split())
        haves = set(have_text.split())
        card_wins.append(len(wins & haves))

    effective_cards = [1] * len(card_wins)

    for i, n in zip(range(len(card_wins)-1, -1, -1), card_wins[::-1]):
        for j in range(n):
            effective_cards[i] += effective_cards[i+j+1]
    
    return sum(effective_cards)


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2023_day04_input.txt') as f:
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
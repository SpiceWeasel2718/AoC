from collections import deque
from itertools import islice

def part1(input_text):
    player_1, player_2 = input_text.split('\n\n')
    deck_1, deck_2 = deque(), deque()

    for line in player_1.splitlines()[1:]:
        deck_1.append(int(line))
    for line in player_2.splitlines()[1:]:
        deck_2.append(int(line))

    while deck_1 and deck_2:
        card_1 = deck_1.popleft()
        card_2 = deck_2.popleft()

        if card_1 > card_2:
            deck_1.extend([card_1, card_2])
        else:
            deck_2.extend([card_2, card_1])
    
    winning_deck = deck_1 if deck_1 else deck_2

    return sum(i*card for i, card in enumerate(reversed(winning_deck), 1))


def part2(input_text):
    player_1, player_2 = input_text.split('\n\n')
    deck_1, deck_2 = deque(), deque()

    for line in player_1.splitlines()[1:]:
        deck_1.append(int(line))
    for line in player_2.splitlines()[1:]:
        deck_2.append(int(line))

    def recursive_combat(deck_1, deck_2):
        history = set()

        while deck_1 and deck_2:
            card_1 = deck_1.popleft()
            card_2 = deck_2.popleft()

            if len(deck_1) >= card_1 and len(deck_2) >= card_2:
                sub_deck_1 = deque(islice(deck_1, card_1))
                sub_deck_2 = deque(islice(deck_2, card_2))
                if recursive_combat(sub_deck_1, sub_deck_2)[0]:
                    deck_1.extend([card_1, card_2])
                else:
                    deck_2.extend([card_2, card_1])
            else:
                if card_1 > card_2:
                    deck_1.extend([card_1, card_2])
                else:
                    deck_2.extend([card_2, card_1])
            
            state = (tuple(deck_1), tuple(deck_2))
            if state in history:
                return True, deck_1
            else:
                history.add(state)

        if deck_1:
            return True, deck_1
        else:
            return False, deck_2

    winning_deck = recursive_combat(deck_1, deck_2)[1]

    return sum(i*card for i, card in enumerate(reversed(winning_deck), 1))


if __name__ == '__main__':
    with open('./2020/input_files/AoC2020_day22_input.txt') as f:
        input_text = f.read()

    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    time_execution = 1

    if time_execution:
        import timeit
        for part in ['part1', 'part2']:
            timer = timeit.Timer(f'{part}(input_text)', globals=globals())
            n, time = timer.autorange()
            print(f'{part} took {time/n:.5f} seconds on average when run {n} times')
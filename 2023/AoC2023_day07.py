def part1(input_text: str):
    from collections import Counter
    from itertools import chain

    bids = {}
    
    for line in input_text.splitlines():
        hand, bid = line.split()
        bids[hand] = int(bid)
    
    def hand_type(hand):
        labels = Counter(hand)
        match max(labels.values()):
            case 5:
                return 6
            case 4:
                return 5
            case 3:
                return 4 if len(labels) == 2 else 3
            case 2:
                return 2 if len(labels) == 3 else 1
            case 1:
                return 0
    
    card_values = {'A': 'e', 'K': 'd', 'Q': 'c', 'J': 'b', 'T': 'a'}

    def hexify(hand):
        hex_str = '0x'
        for c in hand:
            hex_str += card_values[c] if c in card_values else c
        return int(hex_str, base=16)
    
    hands = []
    for __ in range(7):
        hands.append([])
    
    for hand in bids:
        hands[hand_type(hand)].append(hand)
    
    for hand_list in hands:
        hand_list.sort(key=hexify)
    
    s = 0

    for rank, hand in enumerate(chain(*hands), start=1):
        s += rank * bids[hand]
    
    return s
            

def part2(input_text: str):
    from collections import Counter
    from itertools import chain

    bids = {}
    
    for line in input_text.splitlines():
        hand, bid = line.split()
        bids[hand] = int(bid)
    
    def hand_type(hand):
        labels = Counter(hand)
        m = max(labels.values())

        if 'J' in labels:
            nj = labels['J']
            if nj == 5: return 6
            del labels['J']
            m = max(labels.values())
            for k, v in labels.items():
                if v == m:
                    labels[k] += nj
                    break
            m += nj

        match m:
            case 5:
                return 6
            case 4:
                return 5
            case 3:
                return 4 if len(labels) == 2 else 3
            case 2:
                return 2 if len(labels) == 3 else 1
            case 1:
                return 0
    
    card_values = {'A': 'e', 'K': 'd', 'Q': 'c', 'J': '1', 'T': 'a'}

    def hexify(hand):
        hex_str = '0x'
        for c in hand:
            hex_str += card_values[c] if c in card_values else c
        return int(hex_str, base=16)
    
    hands = []
    for __ in range(7):
        hands.append([])
    
    for hand in bids:
        hands[hand_type(hand)].append(hand)
    
    for hand_list in hands:
        hand_list.sort(key=hexify)
    
    s = 0

    for rank, hand in enumerate(chain(*hands), start=1):
        s += rank * bids[hand]
    
    return s


if __name__ == '__main__':
    from pathlib import Path

    path = Path(__file__).parent

    with open(path / 'input_files/AoC2023_day07_input.txt') as f:
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
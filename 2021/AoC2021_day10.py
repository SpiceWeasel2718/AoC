def part1(input_text):
    from collections import deque

    queue = deque()
    lefts = {'(', '[', '{', '<'}
    closers = {')': '(', ']': '[', '}': '{', '>': '<'}
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0

    for line in input_text.splitlines():
        for char in line:
            if char in lefts:
                queue.append(char)
            else:
                candidate = queue.pop()
                if candidate != closers[char]:
                    score += points[char]
                    break
    
    return score
                

def part2(input_text):
    from collections import deque

    queue = deque()
    closers = {')': '(', ']': '[', '}': '{', '>': '<'}
    points = {'(': 1, '[': 2, '{': 3, '<': 4}
    scores = []

    for line in input_text.splitlines():
        queue.clear()

        for char in line:
            if char in points:
                queue.append(char)
            else:
                candidate = queue.pop()
                if candidate != closers[char]:
                    break
        
        else:
            score = 0
            
            for c in reversed(queue):
                score = 5 * score + points[c]
            
            scores.append(score)
    
    return sorted(scores)[len(scores) // 2]


if __name__ == '__main__':
    with open('./input_files/AoC2021_day10_input.txt') as f:
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
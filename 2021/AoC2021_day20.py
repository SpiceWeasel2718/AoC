def part1(input_text):
    from collections import defaultdict

    algorithm_text, __, *image_text = input_text.splitlines()

    algorithm = [(c == '#') for c in algorithm_text]

    factories = [
        lambda: 0,
        (lambda: 1) if algorithm[0] else lambda: 0
    ]

    image = defaultdict(factories[0])

    for x, line in enumerate(image_text):
        for y, ch in enumerate(line):
            image[x+y*1j] = (ch == '#')

    xmax = len(image_text)
    ymax = len(image_text[0])

    
    def new_pixel(image, pos):
        i = 0

        for rel_pos in [-1-1j, -1+0j, -1+1j, -1j, 0j, 1j, 1-1j, 1+0j, 1+1j]:
            i <<= 1
            i += image[pos+rel_pos]
        
        return algorithm[i]

    
    def display_image(image, r):
        lights = {0: '.', 1: '#'}
        out = []

        for x in range(-r-5, xmax+r+5):
            out.append(''.join(lights[image[x+y*1j]] for y in range(-r-5, ymax+r+5)))
        
        return '\n'.join(out)

    
    for r in range(1,2+1):
        new_image = defaultdict(factories[r%2])

        for x in range(-r, xmax+r):
            for y in range(-r, ymax+r):
                new_image[x+y*1j] = new_pixel(image, x+y*1j)
        
        image = new_image

    return sum(image.values())


def part2(input_text):
    from collections import defaultdict

    algorithm_text, __, *image_text = input_text.splitlines()

    algorithm = [(c == '#') for c in algorithm_text]

    factories = [
        lambda: 0,
        (lambda: 1) if algorithm[0] else lambda: 0
    ]

    image = defaultdict(factories[0])

    for x, line in enumerate(image_text):
        for y, ch in enumerate(line):
            image[x+y*1j] = (ch == '#')

    xmax = len(image_text)
    ymax = len(image_text[0])

    
    def new_pixel(image, pos):
        i = 0

        for rel_pos in [-1-1j, -1+0j, -1+1j, -1j, 0j, 1j, 1-1j, 1+0j, 1+1j]:
            i <<= 1
            i += image[pos+rel_pos]
        
        return algorithm[i]

    
    def display_image(image, r):
        lights = {0: '.', 1: '#'}
        out = []

        for x in range(-r-5, xmax+r+5):
            out.append(''.join(lights[image[x+y*1j]] for y in range(-r-5, ymax+r+5)))
        
        return '\n'.join(out)

    
    for r in range(1,50+1):
        new_image = defaultdict(factories[r%2])

        for x in range(-r, xmax+r):
            for y in range(-r, ymax+r):
                new_image[x+y*1j] = new_pixel(image, x+y*1j)
        
        image = new_image

    return sum(image.values())


if __name__ == '__main__':
    with open('./input_files/AoC2021_day20_input.txt') as f:
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
def part1(input_text: str):
    import re
    from math import prod

    WIDTH, HEIGHT = 101, 103
    SECONDS = 100

    quadrants = [[0, 0], [0, 0]]
    x_cutoff = WIDTH // 2
    y_cutoff = HEIGHT // 2

    for line in input_text.splitlines():
        px, py, vx, vy = map(int, re.findall(r"-?\d+", line))
        dest_x = (px + vx * SECONDS) % WIDTH
        dest_y = (py + vy * SECONDS) % HEIGHT

        if dest_x != x_cutoff and dest_y != y_cutoff:
            quadrants[dest_x > x_cutoff][dest_y > y_cutoff] += 1

    return prod(quadrants[0] + quadrants[1])


def part2(input_text: str):
    import re

    from PIL import Image, ImageDraw

    WIDTH, HEIGHT = 101, 103

    p_lst, v_lst = [], []

    for line in input_text.splitlines():
        px, py, vx, vy = map(int, re.findall(r"-?\d+", line))
        p_lst.append([px, py])
        v_lst.append([vx, vy])

    seconds = 0
    img_width, img_height = WIDTH + 15, HEIGHT + 15

    def draw_state(seconds):
        img = Image.new("1", (img_width, img_height))
        draw = ImageDraw.Draw(img)

        for p, v in zip(p_lst, v_lst):
            px, py = p
            vx, vy = v
            draw.point(((px + seconds * vx) % WIDTH, (py + seconds * vy) % HEIGHT), 1)

        draw.text((WIDTH // 2, HEIGHT + 2), f"{seconds}", 1)

        return img

    x_tiles, y_tiles = 20, 20
    img_block = Image.new("1", (img_width * x_tiles, img_height * y_tiles))

    for y in range(0, img_height * y_tiles, img_height):
        for x in range(0, img_width * x_tiles, img_width):
            seconds += 1
            img_block.paste(draw_state(seconds), (x, y))

    img_block.show()

    h0 = int(input("First horizontal line image: "))
    v0 = int(input("First vertical line image: "))
    h1 = int(input("Second horizontal line image: "))
    v1 = int(input("Second vertical line image: "))

    dh = h1 - h0
    dv = v1 - v0
    n0 = v0 - h0
    n = 0

    while (n0 + n * dv) % dh != 0:
        n += 1

    tree_seconds = v0 + dv * n

    draw_state(tree_seconds).show()

    return tree_seconds


if __name__ == "__main__":
    from pathlib import Path

    current_file = Path(__file__)
    input_file = (
        current_file.parent / "input_files" / (current_file.stem + "_input.txt")
    )

    with open(input_file) as fp:
        input_text = fp.read()

    print("Part 1:")
    print(p1 := part1(input_text))
    print("Part 2:")
    print(part2(input_text))

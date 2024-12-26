def part1(input_text: str):
    from collections import deque
    from itertools import islice

    def triangle(n):
        return n * (n + 1) // 2

    files = deque(
        (idx, int(n)) for idx, n in enumerate(islice(input_text.strip(), 0, None, 2))
    )
    spaces = deque(int(n) for n in islice(input_text.strip(), 1, None, 2))

    checksum = 0
    block_pos = 0
    blocks_remaining = 0

    while files:
        file_id, file_size = files.popleft()
        checksum += file_id * (block_pos * file_size + triangle(file_size - 1))
        block_pos += file_size

        space = spaces.popleft()
        while space:
            if not blocks_remaining:
                if files:
                    moving_id, blocks_remaining = files.pop()
                else:
                    break
            chunk_size = min(space, blocks_remaining)
            checksum += moving_id * (block_pos * chunk_size + triangle(chunk_size - 1))
            block_pos += chunk_size
            space -= chunk_size
            blocks_remaining -= chunk_size

    if blocks_remaining:
        checksum += moving_id * (
            block_pos * blocks_remaining + triangle(blocks_remaining - 1)
        )

    return checksum


def part2(input_text: str):
    import heapq
    from collections import defaultdict, deque
    from itertools import islice, zip_longest

    def triangle(n):
        return n * (n + 1) // 2

    disk = []  # (file position, file id, file size); doesn't need to be in order
    files = deque()
    spaces = defaultdict(list)  # {space size: heap of positions of spaces of that size}
    block_pos = 0

    for file_info, space_size in zip_longest(
        enumerate(int(n) for n in islice(input_text.strip(), 0, None, 2)),
        [int(m) for m in islice(input_text.strip(), 1, None, 2)],
    ):
        if file_info is not None:
            file_id, file_size = file_info
            files.append((block_pos, file_id, file_size))
            block_pos += file_size

        if space_size is not None:
            heapq.heappush(spaces[space_size], block_pos)
            block_pos += space_size

    while files:
        file_pos, file_id, file_size = files.pop()
        if file_size <= max(spaces):
            target_size = min(
                (s for s in spaces if s >= file_size), key=lambda k: spaces[k][0]
            )
            target_pos = spaces[target_size][0]
            if target_pos < file_pos:
                disk.append((target_pos, file_id, file_size))
                heapq.heappop(spaces[target_size])
                if not spaces[target_size]:
                    del spaces[target_size]
                space_left = target_size - file_size
                if space_left:
                    heapq.heappush(spaces[space_left], target_pos + file_size)
                continue

        disk.append((file_pos, file_id, file_size))

    checksum = 0

    for file_pos, file_id, file_size in disk:
        checksum += file_id * (file_pos * file_size + triangle(file_size - 1))

    return checksum


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

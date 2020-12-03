tiles = ["......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^.."]

width = len(tiles[0])


def trapped(lcr):
    if lcr in ["^^.", ".^^", "^..", "..^"]:
        return "^"
    else:
        return "."


for i in range(1,400000):
    tiles.append("")
    for j in range(width):
        if j == 0:
            tiles[i] += trapped("." + tiles[i - 1][:2])
        elif j == width-1:
            tiles[i] += trapped(tiles[i - 1][-2:] + ".")
        else:
            tiles[i] += trapped(tiles[i - 1][j-1:j+2])

safe = 0
for row in tiles:
    for c in row:
        if c == ".":
            safe += 1

print(safe)


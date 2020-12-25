import re
from collections import Counter
from functools import reduce


def canonical(t):
    r = t[::-1]
    return t if t < r else r


def edges(tile):
    top = canonical(tile[0])
    bottom = canonical(tile[-1])
    left = canonical(''.join(row[0] for row in tile))
    right = canonical(''.join(row[-1] for row in tile))
    return top, bottom, left, right


matching = Counter()

with open('input') as infile:
    tiles = re.findall(r'Tile (\d+):((?:\n(?:#|\.)+)*)', infile.read())
    tiles = [(int(i), tile.strip().split('\n')) for i, tile in tiles]

for num, tile in tiles:
    n = edges(tile)
    matching.update(n)

sides_of_map = {side for side, count in matching.items() if count == 1}
corners = []
for num, tile in tiles:
    n = edges(tile)
    amount_in_side_map = sum((side in sides_of_map) for side in n)
    if amount_in_side_map == 2:
        corners.append(num)

print(reduce((lambda x, y: x*y), corners, 1))

# I'm not doing part 2

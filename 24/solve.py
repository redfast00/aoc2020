import re

commands = []
with open('input') as infile:
    for line in infile:
        commands.append(re.findall(r'se|sw|nw|ne|e|w', line.strip()))

# https://www.redblobgames.com/grids/hexagons/#coordinates-axial

direction_to_vector = {
    'nw': (0, -1),
    'w': (-1, 0),
    'sw': (-1, 1),
    'se': (0, 1),
    'e': (1, 0),
    'ne': (1, -1)
}

flipped_tiles = set()
for commandlist in commands:
    cx, cy = 0, 0
    for command in commandlist:
        dx, dy = direction_to_vector[command]
        cx, cy = cx + dx, cy + dy
    current = (cx, cy)
    if current in flipped_tiles:
        flipped_tiles.remove(current)
    else:
        flipped_tiles.add(current)
print(len(flipped_tiles))


def ajacent_tiles(coordinate):
    x, y = coordinate
    for dx, dy in direction_to_vector.values():
        yield (x + dx, y + dy)


def step(current_black_tiles):
    new_black_tiles = set()
    evaluated = set()
    for tile_coordinate in current_black_tiles:
        neighbouring_black_tiles = sum((ajacent_tile in current_black_tiles) for ajacent_tile in ajacent_tiles(tile_coordinate))
        if 0 < neighbouring_black_tiles <= 2:
            new_black_tiles.add(tile_coordinate)
        for ajacent_tile in ajacent_tiles(tile_coordinate):
            # check if white tile we haven't seen before
            if ajacent_tile not in evaluated and ajacent_tile not in current_black_tiles:
                black_tile_neighbours = sum((t in current_black_tiles) for t in ajacent_tiles(ajacent_tile))
                if black_tile_neighbours == 2:
                    new_black_tiles.add(ajacent_tile)
                evaluated.add(ajacent_tile)
    return new_black_tiles


current = flipped_tiles
for i in range(1, 100+1):
    current = step(current)

print(len(current))
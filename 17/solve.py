from itertools import product


two_dimensional_coords = set()

with open('input') as infile:
    for idx, line in enumerate(infile):
        for jdx, char in enumerate(line.strip()):
            if char == '#':
                two_dimensional_coords.add((idx, jdx))


def range_3d(point):
    x, y, z = point
    for (offset_x, offset_y, offset_z) in product((-1, 0, 1), repeat=3):
        if offset_x == 0 and offset_y == 0 and offset_z == 0:
            pass
        else:
            yield (x + offset_x, y + offset_y, z + offset_z)

def range_4d(point):
    x, y, z, w = point
    for (offset_x, offset_y, offset_z, offset_w) in product((-1, 0, 1), repeat=4):
        if offset_x == 0 and offset_y == 0 and offset_z == 0 and offset_w == 0:
            pass
        else:
            yield (x + offset_x, y + offset_y, z + offset_z, w + offset_w)

def iteration(active_points, range_function=range_3d):
    new_active = set()
    for active_point in active_points:
        for compute_point in range_function(active_point):
            alive_neighbour_amount = sum((neighbour_point in active_points) for neighbour_point in range_function(compute_point))
            if compute_point in active_points:
                if alive_neighbour_amount in (2, 3):
                    new_active.add(compute_point)
            else:
                if alive_neighbour_amount == 3:
                    new_active.add(compute_point)
    return new_active

current_active_3d = {(x, y, 0) for (x, y) in two_dimensional_coords}

for _ in range(6):
    current_active_3d = iteration(current_active_3d)

print(len(current_active_3d))

current_active_4d = {(x, y, 0, 0) for (x, y) in two_dimensional_coords}

for _ in range(6):
    current_active_4d = iteration(current_active_4d, range_function=range_4d)

print(len(current_active_4d))
import itertools
from copy import deepcopy


SEAT = 'L'

with open('input') as infile:
    lines = [line.strip() for line in infile]

height = len(lines)
width = len(lines[0])
max_wh = max(height, width)

# map of tile coordinate tuples to neighbours
first_board = {}
for x, boardline in enumerate(lines):
    for y, tile in enumerate(boardline):
        if tile == SEAT:
            neighbours = []
            for offset_x, offset_y in itertools.product((-1, 0, 1), repeat=2):
                if (offset_x, offset_y) != (0, 0):
                    neighbour_x, neighbour_y = (x + offset_x, y + offset_y)
                    if neighbour_x in range(height) and neighbour_y in range(width) and lines[neighbour_x][neighbour_y] == SEAT:
                        neighbours.append((neighbour_x, neighbour_y))
            first_board[(x, y)] = neighbours

second_board = {}
for x, boardline in enumerate(lines):
    for y, tile in enumerate(boardline):
        if tile == SEAT:
            neighbours = []
            for offset_x, offset_y in itertools.product((-1, 0, 1), repeat=2):
                if (offset_x, offset_y) != (0, 0):
                    for multiplier in range(1, max_wh + 1):
                        neighbour_x, neighbour_y = (x + offset_x * multiplier, y + offset_y * multiplier)
                        if neighbour_x not in range(height) or neighbour_y not in range(width):
                            break
                        if lines[neighbour_x][neighbour_y] == SEAT:
                            neighbours.append((neighbour_x, neighbour_y))
                            break
            second_board[(x, y)] = neighbours


def next_board_first(current, board):
    new = {}
    for location, occupied in current.items():
        if occupied:
            new[location] = sum(current[neighbour] for neighbour in first_board[location]) < 4
        else:
            new[location] = sum(current[neighbour] for neighbour in first_board[location]) == 0
    return new

def next_board_second(current, board):
    new = {}
    for location, occupied in current.items():
        if occupied:
            new[location] = sum(current[neighbour] for neighbour in second_board[location]) < 5
        else:
            new[location] = sum(current[neighbour] for neighbour in second_board[location]) == 0
    return new


def board_string(board):
    tiles = [['.' for _ in range(width)] for _ in range(height)]
    for location, occupied in board.items():
        tiles[location[0]][location[1]] = '#' if occupied else 'L'
    return '\n'.join((''.join(line)) for line in tiles)

def solve_first():
    current_status = {k: False for k in first_board}
    new_status = next_board_first(current_status, first_board)

    while current_status != new_status:
        current_status = new_status
        new_status = next_board_first(current_status, first_board)
    print(list(current_status.values()).count(True))

def solve_second():
    current_status = {k: False for k in second_board}
    new_status = next_board_second(current_status, second_board)

    while current_status != new_status:
        current_status = new_status
        new_status = next_board_second(current_status, second_board)
    print(list(current_status.values()).count(True))

solve_first()
solve_second()

import math


with open('input') as infile:
    commands = [(lambda l: (l[0], int(l[1:])))(line.strip()) for line in infile]


x, y = 0, 0
angle = 0


for (command, arg) in commands:
    if command == 'N':
        y += arg
    elif command == 'E':
        x += arg
    elif command == 'S':
        y -= arg
    elif command == 'W':
        x -= arg
    elif command == 'L':
        angle = (angle + arg) % 360
    elif command == 'R':
        angle = (angle - arg) % 360
    elif command == 'F':
        dx = round(math.cos(math.radians(angle))) * arg
        dy = round(math.sin(math.radians(angle))) * arg
        x += dx
        y += dy
    # print(x, y, command, arg)

print(abs(x) + abs(y))
del x, y, angle

x, y = 0, 0
waypoint_x, waypoint_y = 10, 1
for (command, arg) in commands:
    if command == 'N':
        waypoint_y += arg
    elif command == 'E':
        waypoint_x += arg
    elif command == 'S':
        waypoint_y -= arg
    elif command == 'W':
        waypoint_x -= arg
    elif command == 'L':
        n_x = round(math.cos(math.radians(arg))) * waypoint_x - round(math.sin(math.radians(arg))) * waypoint_y
        n_y = round(math.cos(math.radians(arg))) * waypoint_y + round(math.sin(math.radians(arg))) * waypoint_x
        waypoint_x, waypoint_y = n_x, n_y
    elif command == 'R':
        n_x = round(math.cos(math.radians(360 - arg))) * waypoint_x - round(math.sin(math.radians(360 - arg))) * waypoint_y
        n_y = round(math.cos(math.radians(360 - arg))) * waypoint_y + round(math.sin(math.radians(360 - arg))) * waypoint_x
        waypoint_x, waypoint_y = n_x, n_y
    elif command == 'F':
        x += waypoint_x * arg
        y += waypoint_y * arg
    # print(waypoint_x, waypoint_y, command, arg)

print(abs(x) + abs(y))





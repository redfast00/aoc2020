import math


with open('input') as infile:
    goal = int(infile.readline().strip())
    stations = [None if e == 'x' else int(e) for e in infile.readline().strip().split(',')]
arrival_time, bus_id = min((math.ceil(goal / interval) * interval, interval) for interval in stations if interval is not None)
print((arrival_time - goal) * bus_id)

current = 0
curadd = 1
for offset, station in enumerate(stations):
    if station is not None:
        current = next(current + curadd * i for i in range(station) if (current + curadd * i + offset) % station == 0)
        curadd *= station
print(current)

# print(current > 100000000000000)
# for offset, station in enumerate(stations):
#     if station is not None:
#         print(station, (current + offset) % station == 0)

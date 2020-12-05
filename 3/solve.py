from operator import mul
from functools import reduce
import math

class Map:
    def __init__(self, map):
        self.map = map
        self.height = len(map)
        self.width = len(map[0])

    def get(self, x, y):
        return self.map[x][y % self.width]

    def amount(self, right, down):
        ctr = 0
        for i in range(math.ceil(self.height / down)):
            if self.get(down*i, right*i) == '#':
                ctr +=1
        return ctr

with open('input') as infile:
    treemap = Map([line.strip() for line in infile.readlines()])

print(treemap.amount(3, 1))

amounts = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

mapped = list(map((lambda t: treemap.amount(t[0], t[1])), amounts))
print(treemap.height)
print(mapped)
print(reduce(mul, mapped, 1))

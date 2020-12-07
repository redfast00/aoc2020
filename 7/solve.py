import re
import functools


def parse(line):
    # shiny purple bags contain 2 pale blue bags, 1 wavy fuchsia bag, 5 pale salmon bags.
    # faded olive bags contain no other bags.
    outer, inner = line.strip('.').split(' bags contain ')
    if inner == 'no other bags':
        return (outer, {})
    else:
        innerparts = inner.split(', ')
        innerdict = {}
        for part in innerparts:
            part = re.sub(r' bags?$', '', part, count=1)
            amount, name = part.split(' ', maxsplit=1)
            innerdict[name] = int(amount)
        return (outer, innerdict)


rules = {}

with open('input') as infile:
    for line in infile:
        outer, inner = parse(line.strip())
        rules[outer] = inner


changed = True
reachable = {'shiny gold'}

only_sets = {outer: set(inner.keys()) for outer, inner in rules.items()}

while changed:
    changed = False
    for outer, inner in only_sets.items():
        if outer in reachable:
            continue
        if inner & reachable:
            reachable.add(outer)
            changed = True
print(len(reachable) - 1)


@functools.lru_cache(maxsize=None)
def count(outer):
    '''Count how many bags are in the outer bag, not counting itself.'''
    inner = rules[outer]
    if not inner:
        return 0
    total = 0
    for innername, amount in inner.items():
        total += amount + amount * count(innername)
    return total


print(count('shiny gold'))

import itertools
from functools import reduce


with open('input') as infile:
    all_sets = []
    current_lines = []
    for line in infile:
        cleaned_line = line.strip()
        if cleaned_line:
            current_lines.append(cleaned_line)
        else:
            all_sets.append(current_lines)
            current_lines = []
    all_sets.append(current_lines)

first_ctr = 0
second_ctr = 0
for s in all_sets:
    first_ctr += len(set(itertools.chain.from_iterable(s)))
    second_ctr += len(reduce((lambda x, y: x & y), (set(sub) for sub in s)))


print(first_ctr)
print(second_ctr)
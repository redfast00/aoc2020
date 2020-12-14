from collections import defaultdict
from itertools import product
import re


with open('input') as infile:
    lines = [line.strip() for line in infile]


def to_masks(mask_string):
    one_mask = int(mask_string.replace('X', '0'), 2)
    zero_mask = int(mask_string.replace('X', '1'), 2)
    return zero_mask, one_mask

memory = defaultdict(lambda x: 0)

zero_mask, one_mask = None, None

for line in lines:
    if line.startswith('mask'):
        mask_string = line.split(' ')[-1]
        zero_mask, one_mask = to_masks(mask_string)
    else:
        match = re.match(r"mem\[(?P<address>\d+)\] = (?P<value>\d+)", line)
        memory[int(match.group('address'))] = (int(match.group('value')) | one_mask) & zero_mask

print(sum(memory.values()))

# part 2

def mask_permute(mask, address):
    result = []
    binary_address = "{0:036b}".format(address)
    new_base_address = [old if maskbit == '0' else '1' for old, maskbit in zip(binary_address, mask)]
    hole_indices = [idx for idx, bit in enumerate(mask) if bit == "X"]
    for replacements in product('01', repeat=len(hole_indices)):
        for hole_idx, replacement in zip(hole_indices, replacements):
            new_base_address[hole_idx] = replacement
            result.append(int(''.join(new_base_address), 2))
    return result

memory = defaultdict(lambda x: 0)
mask = None

for line in lines:
    if line.startswith('mask'):
        mask = line.split(' ')[-1]
    else:
        match = re.match(r"mem\[(?P<address>\d+)\] = (?P<value>\d+)", line)
        addresses = mask_permute(mask, int(match.group('address')))
        for address in addresses:
            memory[address] = int(match.group('value'))

print(sum(memory.values()))
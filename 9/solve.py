def valid(preamble, goal, preamble_len=25):
    assert len(preamble) == preamble_len
    sorted_preamble = sorted(preamble)
    i = 0
    j = len(preamble) - 1
    s = sorted_preamble[i] + sorted_preamble[j]
    while s != goal:
        if s < goal:
            i += 1
        else:
            j -= 1
        if j not in range(len(sorted_preamble)) or i not in range(len(sorted_preamble)) or i >= j:
            return None
        s = sorted_preamble[i] + sorted_preamble[j]
    return sorted_preamble[i] != sorted_preamble[j]

def find_first_error(lst, preamble_len=25):
    for offset in range(len(lst) - preamble_len):
        if not valid(lst[offset:offset+preamble_len], lst[offset + preamble_len], preamble_len=preamble_len):
            return offset + preamble_len

def find_subrange(lst, goal):
    # assumes that all numbers in lst are positive
    current = 0
    i = 0
    j = 0
    while current != goal:
        if current < goal:
            current += lst[j]
            j += 1
        elif current > goal:
            current -= lst[i]
            i += 1
    return lst[i:j]


preamble_len = 25

with open('input') as infile:
    numbers = [int(line.strip()) for line in infile]

error_idx = find_first_error(numbers, preamble_len=preamble_len)
first_solution = numbers[error_idx]
print(first_solution)

subrange = find_subrange(numbers, first_solution)
assert(sum(subrange) == first_solution)
subrange.sort()
print(subrange[0] + subrange[-1])


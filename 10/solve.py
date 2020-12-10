from collections import Counter


with open('input') as infile:
    adapters = [int(line.strip()) for line in infile]


wall = 0
my_joltage = max(adapters) + 3

adapters.sort()
# 7
# [0, 1, 2, 4]
#
# [1, 2, 4, 7]

differences = Counter((upper - lower) for upper, lower in zip(adapters + [my_joltage], [wall] + adapters))

print(differences[1] * differences[3])

adapter_to_idx = {adapter: idx for idx, adapter in enumerate(adapters)}


allowed_differences = (1, 2, 3)
diff_matrix = {k: [0 for _ in adapters] for k in allowed_differences}


for idx, adapter in enumerate(adapters):
    for adapter_difference in allowed_differences:
        targeted_adapter = adapter - adapter_difference
        if targeted_adapter == 0:
            diff_matrix[adapter_difference][idx] = 1
        elif targeted_adapter in adapter_to_idx:
            targeted_adapter_idx = adapter_to_idx[targeted_adapter]
            diff_matrix[adapter_difference][idx] = sum(diff_matrix[i][targeted_adapter_idx] for i in (1, 2, 3))
print(sum(diff_matrix[i][-1] for i in (1, 2, 3)))
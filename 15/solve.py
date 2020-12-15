from collections import defaultdict, deque

with open('input') as infile:
    numbers = [int(number) for number in infile.read().strip().split(',')]


last_said = defaultdict(lambda: deque(maxlen=2))
sequence = []

for i in range(2020):
    if i in range(len(numbers)):
        sequence.append(numbers[i])
    else:
        last_number = sequence[-1]
        if len(last_said[last_number]) == 2:
            sequence.append(last_said[last_number][1] - last_said[last_number][0])
        else:
            sequence.append(0)
    last_said[sequence[i]].append(i)
print(sequence[-1])

last_said = defaultdict(lambda: deque(maxlen=2))
sequence = deque(maxlen=5)

for i in range(30000000):
    if i in range(len(numbers)):
        sequence.append(numbers[i])
    else:
        last_number = sequence[-1]
        if len(last_said[last_number]) == 2:
            sequence.append(last_said[last_number][1] - last_said[last_number][0])
        else:
            sequence.append(0)
    last_said[sequence[-1]].append(i)
print(sequence[-1])
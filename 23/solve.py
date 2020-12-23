with open('input') as infile:
    inputcircle = [int(i) for i in infile.read().strip()]


def insert_selector(size, current, pickup):
    insert = current - 1
    if insert < 1:
        insert = size
    while insert in pickup:
        insert -= 1
        if insert < 1:
            insert = size
    return insert



def first_move(circle, current_idx):
    current = circle[current_idx]
    size = len(circle)
    pickup = []
    # print(f'{circle=}')
    pickup_idx = (current_idx + 1) % len(circle)
    for _ in range(3):
        pickup.append(circle.pop(pickup_idx))
        if pickup_idx not in range(len(circle)):
            pickup_idx = 0
    # print(f'{current=}')
    # print(f'{pickup=}')
    # print()
    insert_value = insert_selector(size, current, pickup)
    insert_idx = circle.index(insert_value)
    for cup in reversed(pickup):
        circle.insert(insert_idx + 1, cup)
    current_idx = circle.index(current)
    return circle, (current_idx + 1) % len(circle)


def linked_list_move(circle, current):
    # assumes a dict where every circle[k] = v means that v is clockwise to k
    fst = circle[current]
    snd = circle[fst]
    thd = circle[snd]

    circle[current] = circle[thd]

    destination = insert_selector(len(circle), current, (fst, snd, thd))

    circle[destination], circle[thd] = fst, circle[destination]
    return circle, circle[current]


current_idx = 0
circle = inputcircle.copy()
for _ in range(100):
    circle, current_idx = first_move(circle, current_idx)
one_idx = circle.index(1)
solution_first = circle[one_idx + 1:] + circle[:one_idx]
print(''.join(str(i) for i in solution_first))


linked_circle = {}
for idx in range(1_000_000):
    if idx < (len(inputcircle) - 1):
        linked_circle[inputcircle[idx]] = inputcircle[idx+1]
    elif idx == len(inputcircle) - 1:
        linked_circle[inputcircle[idx]] = len(inputcircle) + 1
    else:
        linked_circle[idx+1] = idx + 2
linked_circle[len(linked_circle)] = inputcircle[0]

circle = linked_circle
current = inputcircle[0]
for _ in range(10_000_000):
    circle, current = linked_list_move(circle, current)

fst = circle[1]
snd = circle[fst]
print(fst*snd)

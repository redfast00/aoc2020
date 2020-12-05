with open('input') as infile:
    challenge = [int(i) for i in infile.read().strip().split()]

challenge = sorted(challenge)

def find_indices(challenge, goal):
    i = 0
    j = len(challenge) - 1



    s = challenge[i] + challenge[j]


    while s != goal:
        if s < goal:
            i += 1
        else:
            j -= 1
        if j not in range(len(challenge)) or i not in range(len(challenge)) or i > j:
            return None
        s = challenge[i] + challenge[j]
    return (i,j)

for k in challenge:
    res = find_indices(challenge, 2020 - k)
    if res is not None:
        print(res, k)


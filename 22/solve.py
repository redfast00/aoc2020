import re
from collections import deque


with open('input') as infile:
    content = infile.read()
m = re.match(r'Player 1:\n((?:\d+\n)+)\nPlayer 2:\n((?:\d+\n)+)', content, re.MULTILINE)
fst = [int(i) for i in m.group(1).strip().split('\n')]
snd = [int(i) for i in m.group(2).strip().split('\n')]


def combat(fst, snd):
    player_1, player_2 = deque(fst), deque(snd)

    while player_1 and player_2:
        f, s = player_1.popleft(), player_2.popleft()
        if f > s:
            player_1.append(f)
            player_1.append(s)
        else:
            player_2.append(s)
            player_2.append(f)

    winner = player_1 if player_1 else player_2
    return winner


def recursive_combat(fst, snd, depth=1):
    '''Returns (player_1_wins, winning_deck)'''
    seen_before = set()
    player_1, player_2 = deque(fst), deque(snd)
    while player_1 and player_2:
        state_tuple = (tuple(player_1), tuple(player_2))
        if state_tuple in seen_before:
            return True, list(player_1)
        seen_before.add(state_tuple)
        f, s = player_1.popleft(), player_2.popleft()
        if f <= len(player_1) and s <= len(player_2):
            player_1_wins, _ = recursive_combat(tuple(list(player_1)[:f]), tuple(list(player_2)[:s]), depth=depth+1)
        else:
            player_1_wins = f > s
        winner = player_1 if player_1_wins else player_2
        winner.append(f if player_1_wins else s)
        winner.append(s if player_1_wins else f)
    return bool(player_1), list(player_1 if player_1 else player_2)


winner_1 = combat(fst, snd)
print(sum(a * b for a, b in zip(winner_1, range(len(winner_1), 0, -1))))

_, winner_2 = recursive_combat(tuple(fst), tuple(snd))
print(sum(a * b for a, b in zip(winner_2, range(len(winner_2), 0, -1))))


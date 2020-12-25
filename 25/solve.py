MOD = 20201227  # prime
SUBJECT_NUMBER = 7

with open('input') as infile:
    card_public = int(infile.readline().strip())
    door_public = int(infile.readline().strip())

# card_public = 5764801
# door_public = 17807724

print(card_public, door_public)


def crack_loop_size(subject_number, desired_result):
    value = 1
    for idx in range(MOD):
        value *= subject_number
        value = value % MOD
        if value == desired_result:
            return idx + 1
    raise ValueError('impossible')


def transform(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= subject_number
        value = value % MOD
    return value


card_loop_size = crack_loop_size(SUBJECT_NUMBER, card_public)
print(transform(door_public, card_loop_size))

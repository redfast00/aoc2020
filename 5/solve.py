def to_seat_id(boarding):
    binary = boarding.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    return int(binary, 2)

with open('input') as infile:
    seats = {to_seat_id(line.strip()) for line in infile}
    print(max(seats))
    missing = set(range(2**10)) - seats
    for i in range(2**10):
        if i in missing:
            missing.remove(i)
        else:
            break
    for i in range(2**10 - 1, 0, -1):
        if i in missing:
            missing.remove(i)
        else:
            break
    print(missing.pop())

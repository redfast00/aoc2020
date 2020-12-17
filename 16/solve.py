import re
from collections import defaultdict

def does_apply(rule, field):
    for (begin, end) in rule:
        if field in range(begin, end+1):
            return True
    return False

parse_state = 0

rules = {}
my_ticket = None
nearby_tickets = []
with open('input') as infile:
    for line in infile:
        line = line.strip()
        if not line:
            parse_state += 1
            continue
        if parse_state == 0: # rules
            m = re.match(r'^([\w ]+): ([\d]+)-([\d]+) or ([\d]+)-([\d]+)$', line)
            rules[m.group(1)] = [(int(m.group(2)),int(m.group(3))), (int(m.group(4)),int(m.group(5)))]
        elif parse_state == 1:
            assert line == 'your ticket:'
            parse_state += 1
        elif parse_state == 2:
            my_ticket = [int(n) for n in line.split(',')]
        elif parse_state == 3:
            assert line == 'nearby tickets:'
            parse_state += 1
        elif parse_state == 4:
            nearby_tickets.append([int(n) for n in line.split(',')])
        assert parse_state <= 4

invalid_field_ctr = 0

for ticket in nearby_tickets:
    for field in ticket:
        for rule in rules.values():
            if does_apply(rule, field):
                break
        else:
            invalid_field_ctr += field

print(invalid_field_ctr)

valid_tickets = []

for ticket in nearby_tickets:
    for field in ticket:
        for rule in rules.values():
            if does_apply(rule, field):
                break
        else:
            break
    else:
        valid_tickets.append(ticket)

possible = defaultdict(lambda: set(rules.keys()))

for ticket in valid_tickets:
    for idx, field in enumerate(ticket):
        for name, rule in rules.items():
            if not does_apply(rule, field):
                possible[idx].discard(name)

changing = True
while changing:
    changing = False
    for possible_set in possible.values():
        if len(possible_set) == 1:
            only_val = next(iter(possible_set))
            for other_set in possible.values():
                if len(other_set) > 1 and only_val in other_set:
                    other_set.discard(only_val)
                    changing = True


prod = 1
for idx, fieldset in possible.items():
    assert len(fieldset) == 1
    fieldname = next(iter(fieldset))
    if fieldname.startswith('departure'):
        prod *= my_ticket[idx]

print(prod)

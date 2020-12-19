import re
from itertools import chain

parse_state = 0
rules = {}
lines = []

with open('input') as infile:
    for line in infile:
        line = line.strip()
        if not line:
            parse_state += 1
        elif parse_state == 0:
            parts = re.match(r'(\d+): (.*)', line)
            rule_in = int(parts.group(1))
            if literal := re.match('"(.*)"', parts.group(2)):
                rules[rule_in] = literal.group(1)
            else:
                groups = parts.group(2).split(' | ')
                rules[rule_in] = [[int(r) for r in group.split(' ')] for group in groups]
        else:
            lines.append(line)



def recursive_match(rules, num, remaining_string):
    rule = rules[num]
    if isinstance(rule, str):
        if remaining_string.startswith(rule):
            yield remaining_string[len(rule):]
    else:
        for possible_alternative in rule:
            possible_remaining = {remaining_string}
            for rulenum in possible_alternative:
                possible_remaining = set(chain.from_iterable(recursive_match(rules, rulenum, r) for r in possible_remaining))
            for r in possible_remaining:
                yield r


first_ctr = 0
for line in lines:
    first_ctr += any((not m) for m in recursive_match(rules, 0, line))
print(first_ctr)

# part 2
rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

second_ctr = 0
for line in lines:
    second_ctr += any((not m) for m in recursive_match(rules, 0, line))
print(second_ctr)

import re


with open('input') as infile:
    passports = []
    current_passport = {}
    for line in infile:
        cleaned_line = line.strip()
        if cleaned_line:
            current_passport.update((k, v) for k, v in map(lambda x: x.split(':'), cleaned_line.split(' ')))
        else:
            passports.append(current_passport)
            current_passport = {}
    passports.append(current_passport)

# Part 1
required = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    # 'cid'
}

firstctr = 0
for passport in passports:
    if required <= set(passport.keys()):
        firstctr += 1
print(firstctr)


def validate_passport(passport):
    if not (required <= set(passport.keys())):
        return False
    if (not re.fullmatch(r'\d{4}', passport['byr'])) or not (1920 <= int(passport['byr']) <= 2002):
        return False
    if (not re.fullmatch(r'\d{4}', passport['iyr'])) or not (2010 <= int(passport['iyr']) <= 2020):
        return False
    if (not re.fullmatch(r'\d{4}', passport['eyr'])) or not (2020 <= int(passport['eyr']) <= 2030):
        return False
    cm_match = re.fullmatch(r'(\d+)cm', passport['hgt'])
    if cm_match:
        if not 150 <= int(cm_match[1]) <= 193:
            return False
    else:
        in_match = re.fullmatch(r'(\d+)in', passport['hgt'])
        if not in_match:
            return False
        if not 59 <= int(in_match[1]) <= 76:
            return False
    if not re.fullmatch(r'#[0-9a-f]{6}', passport['hcl']):
        return False
    if passport['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        return False
    if not re.fullmatch(r'\d{9}', passport['pid']):
        return False
    return True


secondctr = 0
for passport in passports:
    if validate_passport(passport):
        secondctr += 1
print(secondctr)

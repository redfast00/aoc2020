import re
import itertools
foods = []

with open('input') as infile:
    for line in infile:
        m = re.match(r'(\w+(?: \w+)*) \(contains (\w+(?:, \w+)*)\)', line)
        ingredients = set(m.group(1).split(' '))
        allergens = set(m.group(2).split(', '))
        foods.append((ingredients, allergens))

all_allergens = set(itertools.chain.from_iterable(allergens for (ingredients, allergens) in foods))
all_ingredients = set(itertools.chain.from_iterable(ingredients for (ingredients, allergens) in foods))

allergen_map = {}

for allergen in all_allergens:
    possible_foods = all_ingredients.copy()
    for ingredients_in_food, allergens_in_food in foods:
        if allergen in allergens_in_food:
            possible_foods.intersection_update(ingredients_in_food)
    allergen_map[allergen] = possible_foods

safe_ingredients = all_ingredients - set(itertools.chain.from_iterable(allergen_map.values()))
first_ctr = 0
for ingredients, _ in foods:
    first_ctr += len(safe_ingredients & ingredients)
print(first_ctr)

active_foods = [(ingredients.difference(safe_ingredients), allergens) for ingredients, allergens in foods]

found_allergen_map = {}
found_allergens = set()


still_progress = True
while still_progress:
    new_allergen_map = {}
    still_progress = False
    for allergen, possible_foods in allergen_map.items():
        new_allergen_map[allergen] = possible_foods.difference(found_allergens)
        if len(possible_foods) == 1:
            still_progress = True
            found_allergen_map[allergen] = next(iter(possible_foods))
            found_allergens.add(next(iter(possible_foods)))
    allergen_map = new_allergen_map

assert len(found_allergen_map) == len(all_allergens)

solution_2 = ','.join(found_allergen_map[allergen] for allergen in sorted(found_allergen_map))
print(solution_2)

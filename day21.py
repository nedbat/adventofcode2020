# https://adventofcode.com/2020/day/21

import collections
import re

TEST = """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""".splitlines()

def parse(lines):
    ingred_lists = []
    allergen_map = collections.defaultdict(list)
    for line in lines:
        line = re.sub(r"[(),]", "", line.strip())
        ingredients, _, allergens = line.partition(" contains ")
        ingredients = ingredients.split()
        ingred_lists.append(ingredients)
        for allergen in allergens.split():
            allergen_map[allergen].append(ingredients)
    return ingred_lists, allergen_map

def determine_allergens(allergen_map):
    determined = set()
    allergens = {}
    while len(determined) < len(allergen_map):
        for aller, ingred_lists in allergen_map.items():
            possibles = set.intersection(*map(set, ingred_lists)) - determined
            if len(possibles) == 1:
                the_one = next(iter(possibles))
                determined.add(the_one)
                allergens[the_one] = aller
    return allergens


def part1(lines):
    ingred_lists, allergen_map = parse(lines)
    allergens = determine_allergens(allergen_map)

    counts = collections.Counter()
    for ingreds in ingred_lists:
        counts.update(ingreds)

    ans = sum(counts[ing] for ing in counts if ing not in allergens) 
    return ans

def test_part1():
    assert part1(TEST) == 5

if __name__ == '__main__':
    ans = part1(open("day21_input.txt"))
    print(f"Part 1: {ans}")

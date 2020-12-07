# https://adventofcode.com/2020/day/7

import re

def parse_bags(lines):
    bags = {}
    for line in lines:
        contain_color, _, contain = line.strip().partition(" bags contain ")
        contents = []
        if contain == "no other bags.":
            pass
        else:
            for bag in contain.split(", "):
                num, color = re.fullmatch(r"(\d+) (.*) bags?.?", bag).groups()
                contents.append((int(num), color))
        bags[contain_color] = contents
    return bags

def test_parse_bags():
    with open("day07_test.txt") as f:
        assert parse_bags(f) == {
            "bright white": [(1, "shiny gold")],
            "dark olive": [(3, "faded blue"), (4, "dotted black")],
            "dark orange": [(3, "bright white"), (4, "muted yellow")],
            "dotted black": [],
            "faded blue": [],
            "light red": [(1, "bright white"), (2, "muted yellow")],
            "muted yellow": [(2, "shiny gold"), (9, "faded blue")],
            "shiny gold": [(1, "dark olive"), (2, "vibrant plum")],
            "vibrant plum": [(5, "faded blue"), (6, "dotted black")],
        }

def can_contain(bags, color):
    containers = set()
    for outside, insides in bags.items():
        for num, in_color in insides:
            if color == in_color:
                containers.add(outside)
    return containers

def test_can_contain():
    with open("day07_test.txt") as f:
        bags = parse_bags(f)
    assert can_contain(bags, "shiny gold") == {"bright white", "muted yellow"}

def can_contain_deep(bags, color):
    deep_containers = set()
    goals = {color}
    tried = set()
    while True:
        next_containers = set()
        for goal in goals:
            next_containers.update(can_contain(bags, goal))
            tried.add(goal)
        if not (next_containers - deep_containers):
            break
        deep_containers.update(next_containers)
        goals = next_containers
    return deep_containers

def test_can_contain_deep():
    with open("day07_test.txt") as f:
        bags = parse_bags(f)
    assert can_contain_deep(bags, "shiny gold") == {"bright white", "muted yellow", "dark orange", "light red"}

def part1():
    with open("day07_input.txt") as f:
        bags = parse_bags(f)
    gold_holders = can_contain_deep(bags, "shiny gold")
    print(f"Part 1: {len(gold_holders)} bag colors can eventually contain at least one shiny gold bag")

if __name__ == "__main__":
    part1()

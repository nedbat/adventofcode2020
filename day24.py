# https://adventofcode.com/2020/day/24

import collections
import re

# Map the hex grid onto a skewed square grid:
#
#   nw  ne  __
#   w   @@  e
#   __  sw  se

DIRS = {
    "nw": (-1, -1),
    "ne": (0, -1),
    "w": (-1, 0),
    "e": (1, 0),
    "sw": (0, 1),
    "se": (1, 1),
}

def steps(text):
    return re.findall(r"[ns]?[ew]", text)

def test_steps():
    assert list(steps("sesenwnenenewsee")) == "se se nw ne ne ne w se e".split()

def flip_tiles(fname):
    floor = collections.defaultdict(int)
    with open(fname) as f:
        for line in f:
            x = y = 0
            for step in steps(line):
                dx, dy = DIRS[step]
                x += dx
                y += dy
            floor[x, y] = 1 - floor[x, y]
    return floor

def part1(fname):
    floor = flip_tiles(fname)
    return sum(floor.values())

def test_part1():
    assert part1("day24_test.txt") == 10

if __name__ == "__main__":
    ans = part1("day24_input.txt")
    print(f"Part 1: {ans} tiles are black")

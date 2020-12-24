# https://adventofcode.com/2020/day/24

import collections
import re

import numpy as np
from scipy.signal import convolve

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

def points_to_array(points):
    lx = min(x for x, _ in points)
    ly = min(y for _, y in points)
    hx = max(x for x, _ in points)
    hy = max(y for _, y in points)
    arr = np.zeros((hx-lx+1, hy-ly+1), dtype=np.uint8)
    for x, y in points:
        arr[x - lx, y - ly] = points[x, y]
    return arr

def print_hex(floor):
    for y in range(floor.shape[1]):
        print(" " * (y), end="")
        for x in range(floor.shape[0]):
            print("·@"[floor[x,y]], end=" ")
        print()

def evolve(floor, gens):
    neighbors = np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
    for _ in range(gens):
        counts = convolve(floor, neighbors)
        floor = np.pad(floor, 1)
        flip_black = floor & ((counts == 0) | (counts > 2))
        flip_white = (~floor) & (counts == 2)
        flip = flip_black | flip_white
        floor = floor ^ flip
    return floor

def part2(fname):
    points = flip_tiles(fname)
    floor = points_to_array(points)
    floor = evolve(floor, gens=100)
    return floor.sum()

def test_part2():
    assert part2("day24_test.txt") == 2208

if __name__ == "__main__":
    ans = part2("day24_input.txt")
    print(f"Part 2: {ans} black tiles")

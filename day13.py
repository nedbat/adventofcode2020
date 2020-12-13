# https://adventofcode.com/2020/day/13

import functools

import pytest

from helpers import lcm, modular_inverse, product

x = None

TEST = (
    939,
    [7,13,x,x,59,x,31,19]
)

def part1(time_now, bus_ids):
    bus_ids = set(filter(None, bus_ids))
    best_bus = min(bus_ids, key=lambda b: b - (time_now % b))
    return best_bus * (best_bus - (time_now % best_bus))

def test_part1():
    assert part1(*TEST) == 295

INPUT = (
    1001612,
    [19,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,821,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,463,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23]
)

if __name__ == '__main__':
    ans = part1(*INPUT)
    print(f"Part 1: {ans}")

# Part 2:
# For the TEST input, we need to find x such that:
#   x % 7 == 0
#   x % 13 == 13 - 1
#   x % 59 == 59 - 4
#   x % 31 == 31 - 6
#   x % 19 == 19 - 7
#
#   (x * minv(x,m)) % m == 1
# 
# https://en.wikipedia.org/wiki/Modular_multiplicative_inverse

def part2(bus_ids):
    base_mods = [(b, m) for m, b in enumerate(bus_ids) if b is not None]
    bases = [b for b, _ in base_mods]
    p = product(bases)
    x = 0
    for b, m in base_mods:
        pp = p // b
        x += modular_inverse(pp, b) * pp * (b - m)
    return x % lcm(bases)


@pytest.mark.parametrize("bus_ids, ans", [
    (TEST[1], 1068781),
    ([17,x,13,19], 3417),
    ([67,7,59,61], 754018),
    ([67,x,7,59,61], 779210),
    ([67,7,x,59,61], 1261476),
    ([1789,37,47,1889], 1202161486),
])
def test_part2(bus_ids, ans):
    assert part2(bus_ids) == ans

if __name__ == '__main__':
    ans = part2(INPUT[1])
    print(f"Part 2: {ans}")

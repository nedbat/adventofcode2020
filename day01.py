# https://adventofcode.com/2020/day/1

import itertools

def pair_with_sum(nums, goal):
    for a, b in itertools.product(nums, repeat=2):
        if a + b == goal:
            return a, b

TEST = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]

def test_pair_with_sum():
    assert pair_with_sum(TEST, 2020) == (1721, 299)


def part1():
    with open("day01_input.txt") as f:
        data = list(map(int, f))

    a, b = pair_with_sum(data, 2020)
    print(f"Part 1: {a * b}")

part1()

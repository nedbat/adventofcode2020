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


def my_input():
    with open("day01_input.txt") as f:
        return list(map(int, f))

def part1():
    a, b = pair_with_sum(my_input(), 2020)
    print(f"Part 1: {a * b}")


def three_with_sum(nums, goal):
    snums = set(nums)
    for a, b in itertools.product(nums, repeat=2):
        needed = goal - (a + b)
        if needed in snums:
            return set([a, b, needed])

def test_three_with_sum():
    assert three_with_sum(TEST, 2020) == {979, 366, 675}


def part2():
    a, b, c = three_with_sum(my_input(), 2020)
    print(f"Part 2: {a * b * c}")

if __name__ == "__main__":
    part1()
    part2()

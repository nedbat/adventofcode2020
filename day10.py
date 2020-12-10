# https://adventofcode.com/2020/day/10

import pytest

def numbers(fname):
    with open(fname) as f:
        return list(map(int, f))

def part1(fname):
    nums = sorted(numbers(fname))
    jolts = 0
    diff1 = diff3 = 0
    for num in nums:
        if num - jolts == 1:
            diff1 += 1
        elif num - jolts == 3:
            diff3 += 1
        else:
            raise Exception(f"{jolts=}, {num=}")
        jolts = num
    diff3 += 1
    return diff1 * diff3

@pytest.mark.parametrize("fname, ans", [
    ("day10_test1.txt", 35),
    ("day10_test2.txt", 220),
])
def test_part1(fname, ans):
    assert part1(fname) == ans

if __name__ == '__main__':
    ans = part1("day10_input.txt")
    print(f"Part 1: the number of 1-jolt differences multiplied by the number of 3-jolt differences is {ans}")

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

def arrangements(nums):
    nums = sorted(nums, reverse=True) + [0]
    ways = [1]
    for i in range(1, len(nums)):
        this_way = 0
        for back in [1,2,3]:
            backi = i - back
            if backi >= 0:
                if 1 <= nums[backi] - nums[i] <= 3:
                    this_way += ways[backi]
        ways.append(this_way)
    return ways[-1]

def part2(fname):
    return arrangements(numbers(fname))

@pytest.mark.parametrize("fname, ans", [
    ("day10_test1.txt", 8),
    ("day10_test2.txt", 19208),
])
def test_arrangements(fname, ans):
    assert part2(fname) == ans

if __name__ == '__main__':
    ans = part2("day10_input.txt")
    print(f"Part 2: the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device is {ans}")

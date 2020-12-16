# https://adventofcode.com/2020/day/15

import itertools

import pytest

def memory_game(start_nums):
    when = {}
    for turn, num in enumerate(start_nums, start=1):
        when[num] = turn
        yield num

    num = 0
    for turn in itertools.count(start=turn + 1):
        yield num
        if num in when:
            next_num = turn - when[num]
        else:
            next_num = 0
        when[num] = turn
        num = next_num

def nth(seq, n):
    for i, val in enumerate(seq, start=1):
        if i == n:
            return val

def part1(start):
    return nth(memory_game(start), 2020)

@pytest.mark.parametrize("start, ans", [
    ([0, 3, 6], 436),
    ([1, 3, 2], 1),
    ([2, 1, 3], 10),
    ([1, 2, 3], 27),
    ([2, 3, 1], 78),
    ([3, 2, 1], 438),
    ([3, 1, 2], 1836),
])
def test_part1(start, ans):
    assert part1(start) == ans

if __name__ == "__main__":
    ans = part1([1,0,18,10,19,6])
    print(f"Part 1: {ans}")

def part2(start):
    return nth(memory_game(start), 30_000_000)

@pytest.mark.parametrize("start, ans", [
    ([0, 3, 6], 175594),
    ([1, 3, 2], 2578),
    ([2, 1, 3], 3544142),
    ([1, 2, 3], 261214),
    ([2, 3, 1], 6895259),
    ([3, 2, 1], 18),
    ([3, 1, 2], 362),
])
def test_part2(start, ans):
    assert part2(start) == ans

if __name__ == "__main__":
    ans = part2([1,0,18,10,19,6])
    print(f"Part 2: {ans}")

# https://adventofcode.com/2020/day/15

import collections
import itertools

import pytest

def memory_game(start_nums):
    when = collections.defaultdict(list)
    for turn, num in enumerate(start_nums, start=1):
        when[num].append(turn)
        yield num

    for turn in itertools.count(start=turn + 1):
        num_turns = when[num]
        if len(num_turns) == 1:
            num = 0
        else:
            num = num_turns[-1] - num_turns[-2]
        when[num].append(turn)
        yield num

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

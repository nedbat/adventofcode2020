# https://adventofcode.com/2020/day/9

import collections
import itertools
import pathlib


def is_sum_of_two(nums, total):
    for a, b in itertools.combinations(nums, 2):
        if a + b == total:
            return True
    return False

def bad_numbers(nums, window):
    deq = collections.deque()
    numit = iter(nums)
    for _ in range(window):
        deq.append(next(numit))

    for num in numit:
        if not is_sum_of_two(deq, num):
            yield num
        deq.popleft()
        deq.append(num)

def numbers_from_file(fname):
    return map(int, pathlib.Path(fname).read_text().splitlines())

def test_bad_numbers():
    assert list(bad_numbers(numbers_from_file("day09_test.txt"), 5)) == [127]

def part1():
    bad = list(bad_numbers(numbers_from_file("day09_input.txt"), 25))
    print(f"Part 1: The first bad number is {bad[0]}")

if __name__ == '__main__':
    part1()

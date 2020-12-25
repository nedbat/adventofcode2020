# https://adventofcode.com/2020/day/25

import itertools

from helpers import nth

TEST = [5764801, 17807724]

INPUT = [17607508, 15065270]

def transformed_values(subject):
    val = 1
    while True:
        yield val
        val = (val * subject) % 20201227

def transform(subject, loop_size):
    return nth(transformed_values(subject), loop_size)

def find_loop_size(pubkey):
    for loop_size, val in enumerate(transformed_values(7)):
        if val == pubkey:
            return loop_size

def test_find_loop_size():
    assert find_loop_size(5764801) == 8
    assert find_loop_size(17807724) == 11

def part1(*keys):
    loop1 = find_loop_size(keys[0])
    loop2 = find_loop_size(keys[1])
    ekey1 = transform(keys[0], loop2)
    ekey2 = transform(keys[1], loop1)
    assert ekey1 == ekey2
    return ekey1

def test_part1():
    assert part1(*TEST) == 14897079

if __name__ == "__main__":
    ans = part1(*INPUT)
    print(f"Part 1: {ans}")

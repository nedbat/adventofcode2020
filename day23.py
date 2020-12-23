# https://adventofcode.com/2020/day/23

import itertools

from helpers import iterate, nth

def move(circle):
    pick = circle[1:4]
    new = circle[0:1] + circle[4:]
    lo = min(new)
    hi = max(new)

    dest = new[0] - 1
    while True:
        if dest < lo:
            dest = hi
        try:
            where = new.index(dest) + 1
        except ValueError:
            dest -= 1
        else:
            break
    new[where:where] = pick
    new = new[1:] + new[0:1]
    return new

def nums(s):
    return list(map(int, s))

def strs(n):
    return "".join(map(str, n))

def labels_after_1(circle):
    where = circle.index(1)
    rotated = circle[where+1:] + circle[:where]
    return strs(rotated)

def test_move():
    start = nums("389125467")
    assert labels_after_1(nth(iterate(move, start), 10)) == "92658374"
    assert labels_after_1(nth(iterate(move, start), 100)) == "67384529"

if __name__ == '__main__':
    start = nums("469217538")
    ans = labels_after_1(nth(iterate(move, start), 100))
    print(f"Part 1: labels after 1 are {ans}")

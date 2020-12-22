# https://adventofcode.com/2020/day/22

import collections

TEST = [[9, 2, 6, 3, 1], [5, 8, 4, 7, 10]]

INPUT = [
    [43, 36, 13, 11, 20, 25, 37, 38, 4, 18, 1, 8, 27, 23, 7, 22, 10, 5, 50, 40, 45, 26, 15, 32, 33],
    [21, 29, 12, 28, 46, 9, 44, 6, 16, 39, 19, 24, 17, 14, 47, 48, 42, 34, 31, 3, 41, 35, 2, 30, 49]
]

def part1(deck1, deck2):
    dq1 = collections.deque(deck1)
    dq2 = collections.deque(deck2)
    while dq1 and dq2:
        p1 = dq1.popleft()
        p2 = dq2.popleft()
        if p1 > p2:
            dq1.extend([p1, p2])
        else:
            dq2.extend([p2, p1])
    winner = dq1 or dq2
    score = sum((len(winner) - i) * card for i, card in enumerate(winner))
    return score

def test_part1():
    assert part1(*TEST) == 306

if __name__ == "__main__":
    print(f"Part 1: {part1(*INPUT)}")

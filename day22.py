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
        c1 = dq1.popleft()
        c2 = dq2.popleft()
        if c1 > c2:
            dq1.extend([c1, c2])
        else:
            dq2.extend([c2, c1])
    winner = dq1 or dq2
    score = sum((len(winner) - i) * card for i, card in enumerate(winner))
    return score

def test_part1():
    assert part1(*TEST) == 306

if __name__ == "__main__":
    print(f"Part 1: {part1(*INPUT)}")

# Part 2.

def play_game(deck1, deck2):
    """Returns (1 or 2 (winner), dq1, dq2)"""
    seen = set()
    dq1 = collections.deque(deck1)
    dq2 = collections.deque(deck2)
    while dq1 and dq2:
        c1 = dq1.popleft()
        c2 = dq2.popleft()
        if c1 <= len(dq1) and c2 <= len(dq2):
            # Recursive game
            winner, _, _ = play_game(list(dq1)[:c1], list(dq2)[:c2])
        else:
            winner = 1 if c1 > c2 else 2

        if winner == 1:
            dq1.extend([c1, c2])
        else:
            dq2.extend([c2, c1])

        fp = (tuple(dq1), tuple(dq2))
        if fp in seen:
            return 1, dq1, dq2
        seen.add(fp)

    return (1 if dq1 else 2), dq1, dq2

def part2(deck1, deck2):
    _, dq1, dq2 = play_game(deck1, deck2)
    winner = dq1 or dq2
    score = sum((len(winner) - i) * card for i, card in enumerate(winner))
    return score

def test_inifinite_prevention():
    play_game([43, 19], [2, 29, 14])[0] == 1

def test_part2():
    assert part2(*TEST) == 291

if __name__ == "__main__":
    print(f"Part 2: {part2(*INPUT)}")

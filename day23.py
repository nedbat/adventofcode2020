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

# Part 2: let's try just running it.

def nums_1m(s, n=1_000_000):
    start = nums(s)
    next1 = max(start) + 1
    start.extend(range(next1, next1 + (n - len(start))))
    return start

def test_nums_1m():
    n1m = nums_1m("469217538")
    assert len(n1m) == 1_000_000
    assert max(n1m) == 1_000_000

def part2_answer(circle):
    where = circle.index(1)
    return circle[where+1] * circle[where+2]

def part2(start):
    circle = nums_1m(nums(start))
    for i in range(10_000):
        circle = nth(iterate(move, circle), 1000)
        print(i)
    return part2_answer(circle)

def nope_test_part2():
    assert part2("389125467") == 149245887792

# Nope, it takes WAAAAY too long.

# Part 2 with an idea from Reddit:
# The circle is a dict mapping a label onto the label next to it in the circle.

def make_circle(s, circle_size=1_000_000):
    circle = {}
    ns = nums(s)
    last = ns[0]
    for n in ns[1:]:
        circle[last] = n
        last = n
    next1 = max(ns) + 1
    for n in range(next1, next1 + (circle_size - len(ns))):
        circle[last] = n
        last = n
    circle[last] = ns[0]
    return circle

class Game:
    def __init__(self, s, n=None):
        self.circle = make_circle(s, n or len(s))
        self.current = nums(s)[0]
        self.lo = min(self.circle)
        self.hi = max(self.circle)

    def move(self):
        pick1 = self.circle[self.current]
        pick2 = self.circle[pick1]
        pick3 = self.circle[pick2]
        picked = {pick1, pick2, pick3}
        self.circle[self.current] = self.circle[pick3]
        dest = self.current - 1
        while True:
            if dest < self.lo:
                dest = self.hi
            if dest not in picked:
                break
            dest -= 1
        self.circle[pick3] = self.circle[dest]
        self.circle[dest] = pick1
        self.current = self.circle[self.current]

    def str(self):
        s = ""
        cur = 1
        while True:
            cur = self.circle[cur]
            if cur == 1:
                break
            s += str(cur)
        return s

    def two_after_1(self):
        a = self.circle[1]
        b = self.circle[a]
        print(a, b)
        return a * b

def part1_again(start):
    game = Game(start)
    for _ in range(100):
        game.move()
    return game.str()

def test_part1_again():
    assert part1_again("389125467") == "67384529"
    
def part2(start):
    game = Game(start, 1_000_000)
    assert len(game.circle) == 1_000_000
    for _ in range(10_000_000):
        game.move()
    return game.two_after_1()

def test_part2():
    assert part2("389125467") == 149245887792

if __name__ == '__main__':
    ans = part2("469217538")
    print(f"Part 2: {ans}")

# https://adventofcode.com/2020/day/12

import dataclasses

def read_steps(fname):
    with open(fname) as f:
        return [(l[0], int(l[1:])) for l in f]

DIRS = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
}

DIRV = list(DIRS.values())

RTURNS = {v: nextv for v, nextv in zip(DIRV, DIRV[1:] + DIRV[:1])}
LTURNS = {v: nextv for nextv, v in RTURNS.items()}

@dataclasses.dataclass
class Ship:
    x: int = 0
    y: int = 0
    dirx: int = 1
    diry: int = 0

    def step(self, op, num):
        x, y, dirx, diry = dataclasses.astuple(self)
        if op in DIRS:
            dx, dy = DIRS[op]
            x += dx * num
            y += dy * num
        elif op == "F":
            x += dirx * num
            y += diry * num
        else:
            assert op in "LR"
            assert num in [90, 180, 270]
            if num == 180:
                dirx *= -1
                diry *= -1
            elif (op, num) in [("R", 90), ("L", 270)]:
                dirx, diry = RTURNS[dirx, diry]
            elif (op, num) in [("L", 90), ("R", 270)]:
                dirx, diry = LTURNS[dirx, diry]

        return self.__class__(x, y, dirx, diry)

def distance(steps):
    ship = Ship()
    for step in steps:
        ship = ship.step(*step)
    return abs(ship.x) + abs(ship.y)

def test_distance():
    ans = distance(read_steps("day12_test.txt"))
    assert ans == 25

if __name__ == '__main__':
    ans = distance(read_steps("day12_input.txt"))
    print(f"Part 1: the ship's distance is {ans}")

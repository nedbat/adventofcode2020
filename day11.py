# https://adventofcode.com/2020/day/11

def read_seats(fname):
    seats = {}
    with open(fname) as f:
        for irow, row in enumerate(f):
            for ichar, char in enumerate(row):
                if char in "L#":
                    seats[(irow, ichar)] = char
    return seats

def dxdy():
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == dy == 0:
                continue
            yield dx, dy

def neighbors(x, y):
    for dx, dy in dxdy():
        yield x + dx, y + dy

def next_gen(seats):
    nseats = {}
    for (irow, ichar), char in seats.items():
        occupied = sum(seats.get((nx, ny), ".") == "#" for nx, ny in neighbors(irow, ichar))
        if char == "L":
            nseats[irow, ichar] = "#" if occupied == 0 else "L"
        elif char == "#":
            nseats[irow, ichar] = "L" if occupied >= 4 else "#"
    return nseats

def num_occupied(seats):
    return sum(1 for ch in seats.values() if ch == "#")

def run_until_stable(seats):
    while True:
        next_seats = next_gen(seats)
        if next_seats == seats:
            return seats
        seats = next_seats

def test_part1():
    seats = run_until_stable(read_seats("day11_test.txt"))
    assert num_occupied(seats) == 37

if __name__ == '__main__':
    seats = run_until_stable(read_seats("day11_input.txt"))
    ans = num_occupied(seats)
    print(f"Part 1: {ans} seats are occupied")


import dataclasses
from typing import Dict, Tuple

@dataclasses.dataclass
class Seats:
    width: int
    height: int
    seats: Dict[Tuple[int, int], str]

    @classmethod
    def from_file(cls, fname):
        seats = read_seats(fname)
        width = max(ichar for (irow, ichar) in seats.keys()) + 1
        height = max(irow for (irow, ichar) in seats.keys()) + 1
        return cls(width, height, seats)

    def in_bounds(self, r, c):
        return (0 <= r < self.height) and (0 <= c < self.width)

    def seats_visible(self, r, c):
        for dx, dy in dxdy():
            r2 = r + dy
            c2 = c + dx
            while self.in_bounds(r2, c2):
                ch = self.seats.get((r2, c2), ".")
                if ch != ".":
                    yield ch
                    break
                r2 += dy
                c2 += dx

    def next(self):
        nseats = {}
        for (irow, ichar), char in self.seats.items():
            occupied = sum(1 for ch in self.seats_visible(irow, ichar) if ch == "#")
            if char == "L":
                nseats[irow, ichar] = "#" if occupied == 0 else "L"
            elif char == "#":
                nseats[irow, ichar] = "L" if occupied >= 5 else "#"
        return self.__class__(self.width, self.height, nseats)

    def ascii(self):
        chars = []
        for irow in range(self.height):
            for ichar in range(self.width):
                chars.append(self.seats.get((irow, ichar), "."))
            chars.append("\n")
        return "".join(chars)

def test_from_file():
    seats = Seats.from_file("day11_test.txt")
    assert seats.width == 10
    assert seats.height == 10
    assert num_occupied(seats.seats) == 0

def test_next():
    seats = Seats.from_file("day11_test.txt")
    for _ in range(3):
        print(seats.ascii())
        print("-" * 40)
        seats = seats.next()

def iterate(fn, val):
    while True:
        yield val
        val = fn(val)

def fix_point(seq):
    last = None
    for val in seq:
        if val == last:
            return last
        last = val

def part2(fname):
    seats = Seats.from_file(fname)
    final = fix_point(iterate(Seats.next, seats))
    return num_occupied(final.seats)

def test_part2():
    assert part2("day11_test.txt") == 26

if __name__ == '__main__':
    ans = part2("day11_input.txt")
    print(f"Part 2: {ans} seats are occupied")

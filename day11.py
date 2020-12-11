# https://adventofcode.com/2020/day/11

def read_seats(fname):
    seats = {}
    with open(fname) as f:
        for irow, row in enumerate(f):
            for ichar, char in enumerate(row):
                if char != ".":
                    seats[(irow, ichar)] = char
    return seats

def neighbors(x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == dy == 0:
                continue
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

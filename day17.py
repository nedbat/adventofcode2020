# https://adventofcode.com/2020/day/17

INPUT = """\
...#..#.
.....##.
##..##.#
#.#.##..
#..#.###
...##.#.
#..##..#
.#.#..#.
"""

TEST = """\
.#.
..#
###
"""

import itertools

from helpers import iterate, nth

def cells_from_text(text):
    cells = set()
    for y, row in enumerate(text.splitlines()):
        for x, cell in enumerate(row):
            if cell == "#":
                cells.add((x, y, 0))
    return cells

dxdydz = set(itertools.product((-1, 0, 1), repeat=3))
dxdydz.remove((0, 0, 0))

def neighbors(x, y, z):
    for dx, dy, dz in dxdydz:
        yield x+dx, y+dy, z+dz

def rangexyz(startx, endx, starty, endy, startz, endz):
    for x in range(startx, endx):
        for y in range(starty, endy):
            for z in range(startz, endz):
                yield x, y, z
    
def next_gen(cells):
    ncells = set()
    minx = min(x for x,y,z in cells)
    maxx = max(x for x,y,z in cells)
    miny = min(y for x,y,z in cells)
    maxy = max(y for x,y,z in cells)
    minz = min(z for x,y,z in cells)
    maxz = max(z for x,y,z in cells)
    for x, y, z in rangexyz(minx-1, maxx+2, miny-1, maxy+2, minz-1, maxz+2):
        ncount = sum(1 for nx, ny, nz in neighbors(x, y, z) if (nx, ny, nz) in cells)
        if (x, y, z) in cells:
            if ncount in (2, 3):
                ncells.add((x, y, z))
        else:
            if ncount == 3:
                ncells.add((x, y, z))
    return ncells

def generations(cells):
    return iterate(next_gen, cells)

def part1(cells):
    cells6 = nth(generations(cells), 6)
    return len(cells6)

def test_part1():
    assert part1(cells_from_text(TEST)) == 112

if __name__ == '__main__':
    ans = part1(cells_from_text(INPUT))
    print(f"Part 1: {ans} cubes")

# Part 2: copy everything and add a fourth dimension!?

def cells_from_text2(text):
    cells = set()
    for x,y,z in cells_from_text(text):
        cells.add((x, y, z, 0))
    return cells

dxdydzdw = set(itertools.product((-1, 0, 1), repeat=4))
dxdydzdw.remove((0, 0, 0, 0))

def neighbors2(x, y, z, w):
    for dx, dy, dz, dw in dxdydzdw:
        yield x+dx, y+dy, z+dz, w+dw

def rangexyzw(startx, endx, starty, endy, startz, endz, startw, endw):
    for x in range(startx, endx):
        for y in range(starty, endy):
            for z in range(startz, endz):
                for w in range(startw, endw):
                    yield x, y, z, w

def next_gen2(cells):
    ncells = set()
    minx = min(x for x,y,z,w in cells)
    maxx = max(x for x,y,z,w in cells)
    miny = min(y for x,y,z,w in cells)
    maxy = max(y for x,y,z,w in cells)
    minz = min(z for x,y,z,w in cells)
    maxz = max(z for x,y,z,w in cells)
    minw = min(w for x,y,z,w in cells)
    maxw = max(w for x,y,z,w in cells)
    for x, y, z, w in rangexyzw(minx-1, maxx+2, miny-1, maxy+2, minz-1, maxz+2, minw-1, maxw+2):
        ncount = sum(1 for nx, ny, nz, nw in neighbors2(x, y, z, w) if (nx, ny, nz, nw) in cells)
        if (x, y, z, w) in cells:
            if ncount in (2, 3):
                ncells.add((x, y, z, w))
        else:
            if ncount == 3:
                ncells.add((x, y, z, w))
    return ncells

def generations2(cells):
    return iterate(next_gen2, cells)

def part2(cells):
    cells6 = nth(generations2(cells), 6)
    return len(cells6)

def test_part2():
    assert part2(cells_from_text2(TEST)) == 848

if __name__ == '__main__':
    ans = part2(cells_from_text2(INPUT))
    print(f"Part 2: {ans} cubes")

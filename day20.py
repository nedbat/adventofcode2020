# https://adventofcode.com/2020/day/20

import collections
import re

from helpers import product, range2d

def zyx(s):
    """Reverse a string"""
    return "".join(reversed(s))

def test_zyx():
    assert zyx("Hello") == "olleH"

def andzyx(s):
    """Produce a string and its reverse"""
    yield s
    yield zyx(s)

def andzyxes(lines):
    yield lines
    yield [zyx(l) for l in lines]

def orientations(lines):
    """Produce all eight orientations of a character matrix."""
    yield from andzyxes(lines)
    yield from andzyxes(lines[::-1])
    assert len(lines) == len(lines[0])
    sidelen = len(lines)
    rotated = ["".join(l[i] for l in lines) for i in range(sidelen)]
    yield from andzyxes(rotated)
    yield from andzyxes(rotated[::-1])


class Tile:
    def __init__(self, id, lines):
        self.id = id
        self.lines = lines

    def __repr__(self):
        return f"<Tile {self.id}>"

    @classmethod
    def from_text(cls, text):
        lines = text.splitlines()
        id = int(re.search(r"Tile (\d+):", lines[0])[1])
        return cls(id, lines[1:])

    def edges(self):
        yield from andzyx(self.lines[0])
        yield from andzyx(self.lines[-1])
        left = "".join(l[0] for l in self.lines)
        yield from andzyx(left)
        right = "".join(l[-1] for l in self.lines)
        yield from andzyx(right)

    def top_edge(self):
        return self.lines[0]

    def left_edge(self):
        return "".join(l[0] for l in self.lines)

    def bottom_edge(self):
        return self.lines[-1]

    def right_edge(self):
        return "".join(l[-1] for l in self.lines)

    def orientations(self):
        for oriented_lines in orientations(self.lines):
            yield self.__class__(self.id, oriented_lines)

    def inner_lines(self):
        for l in self.lines[1:-1]:
            yield l[1:-1]

def tiles_from_file(fname):
    with open(fname) as f:
        text = f.read()
    for chunk in text.split("\n\n"):
        if chunk:
            yield Tile.from_text(chunk)

def test_edges():
    tiles = list(tiles_from_file("day20_test.txt"))
    edges = list(tiles[0].edges())
    assert edges == [
        "..##.#..#.",
        ".#..#.##..",
        "..###..###",
        "###..###..",
        ".#####..#.",
        ".#..#####.",
        "...#.##..#",
        "#..##.#...",
        ]

class TileSet:
    def __init__(self, tiles):
        self.tiles = tiles
        self.edgemap = collections.defaultdict(list)
        for t in self.tiles:
            for edge in t.edges():
                self.edgemap[edge].append(t)

    @classmethod
    def from_file(cls, fname):
        return cls(list(tiles_from_file(fname)))

    def corners(self):
        c = collections.Counter()
        for t in self.tiles:
            c.update(t.edges())

        for t in self.tiles:
            counts = [c[edge] for edge in t.edges()]
            if sum(counts) == 12:
                yield t

    def tiles_with_edge(self, edge):
        return self.edgemap[edge]

def part1(fname):
    # Find the four corner tiles. Both the test data and the real input have
    # unique matching, so we can just look for the four tiles that have two
    # matching edges and two non-matching edges.
    tileset = TileSet.from_file(fname)
    return product(corner.id for corner in tileset.corners())

def test_part1():
    assert part1("day20_test.txt") == 20899048083289

if __name__ == '__main__':
    ans = part1("day20_input.txt")
    print(f"Part 1: {ans}")

# Part 2

class Stitcher:
    def __init__(self, tileset):
        self.tileset = tileset
        self.stitched = None

    def stitch(self):
        # Start with a corner tile.
        corner0 = next(self.tileset.corners())

        # Find an orientation so the right and bottom edges have a match.
        for corner0o in corner0.orientations():
            to_left = self.tileset.tiles_with_edge(corner0o.right_edge())
            below = self.tileset.tiles_with_edge(corner0o.bottom_edge())
            if len(to_left) == 2 and len(below) == 2:
                break

        self.stitched = [[corner0o]]
        while True:
            while True:
                latest = self.stitched[-1][-1]
                next_tiles = self.tileset.tiles_with_edge(latest.right_edge())
                if len(next_tiles) == 1:
                    # We are at the end of a row, nothing matches.
                    break
                next_tile = next(tile for tile in next_tiles if tile.id != latest.id)
                # Find the orientation of next_tile that fits
                for nexto in next_tile.orientations():
                    if nexto.left_edge() == latest.right_edge():
                        break
                self.stitched[-1].append(nexto)

            # Find the tile that starts the next row.
            above = self.stitched[-1][0]
            next_tiles = self.tileset.tiles_with_edge(above.bottom_edge())
            if len(next_tiles) == 1:
                # No next row, we are done.
                break
            # Find the orientation of next_tile that fits
            next_tile = next(tile for tile in next_tiles if tile.id != above.id)
            for nexto in next_tile.orientations():
                if nexto.top_edge() == above.bottom_edge():
                    break
            self.stitched.append([nexto])

    def stitched_lines(self):
        for row in self.stitched:
            yield from ("".join(t) for t in zip(*(tile.inner_lines() for tile in row)))


def hashes_without_pattern(lines, pattern):
    linew = len(lines[0])
    lineh = len(lines)
    patw = len(pattern[0])
    path = len(pattern)

    lines_xy = set(((x, y) for x, y in range2d(linew, lineh) if lines[y][x] == "#"))
    pattern_xy = set(((x, y) for x, y in range2d(patw, path) if pattern[y][x] == "#"))

    without = set(lines_xy)
    for sx, sy in range2d(linew - patw + 1, lineh - path + 1):
        if all((sx+px,sy+py) in lines_xy for px,py in pattern_xy):
            for px, py in pattern_xy:
                without.remove((sx+px, sy+py))

    return len(without)

MONSTER = """\
..................#.
#....##....##....###
.#..#..#..#..#..#...
""".splitlines()

def part2(fname):
    stitcher = Stitcher(TileSet.from_file(fname))
    stitcher.stitch()
    counts = []
    for stitchedo in orientations(list(stitcher.stitched_lines())):
        counts.append(hashes_without_pattern(stitchedo, MONSTER))
    return min(counts)

def test_part2():
    assert part2("day20_test.txt") == 273

if __name__ == '__main__':
    ans = part2("day20_input.txt")
    print(f"Part 2: {ans}")

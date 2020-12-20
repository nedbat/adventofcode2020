# https://adventofcode.com/2020/day/20

import collections
import re

from helpers import product

def zyx(s):
    """Reverse a string"""
    return "".join(reversed(s))

def test_zyx():
    assert zyx("Hello") == "olleH"

def andzyx(s):
    """Produce a string and its reverse"""
    yield s
    yield zyx(s)

class Tile:
    def __init__(self, id, lines):
        self.id = id
        self.lines = lines

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

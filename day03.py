# https://adventofcode.com/2020/day/3

import dataclasses

class Trees:
    def __init__(self, width, height, trees):
        self.width = width
        self.height = height
        self.trees = trees

    @classmethod
    def parse_trees(cls, lines):
        trees = set()
        for l, line in enumerate(lines):
            line = line.strip()
            width = len(line)
            for c, char in enumerate(line):
                if char == "#":
                    trees.add((c, l))

        return cls(width, l, trees)

    @classmethod
    def from_file(cls, fname):
        with open(fname) as f:
            return cls.parse_trees(f)

    def __getitem__(self, coords):
        x, y = coords
        return (x % self.width, y) in self.trees

def diagonal_points(right, down):
    x = y = 0
    while True:
        yield x, y
        x += right
        y += down

def trees_encountered(trees, right, down):
    for x, y in diagonal_points(right, down):
        if y > trees.height:
            break
        if trees[x, y]:
            yield x, y

def seq_len(seq):
    return sum(1 for _ in seq)

def test_trees_encountered():
    trees = Trees.from_file("day03_test.txt")
    assert seq_len(trees_encountered(trees, 3, 1)) == 7

def part1():
    trees = Trees.from_file("day03_input.txt")
    num_trees = seq_len(trees_encountered(trees, 3, 1))
    print(f"Part 1: encountered {num_trees} trees")

if __name__ == '__main__':
    part1()

def part2_calc(fname):
    trees = Trees.from_file(fname)
    total = 1
    for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        num_trees = seq_len(trees_encountered(trees, right, down))
        total *= num_trees
    return total

def test_part2():
    assert part2_calc("day03_test.txt") == 336

if __name__ == '__main__':
    print(f"Part 2: answer: {part2_calc('day03_input.txt')}")

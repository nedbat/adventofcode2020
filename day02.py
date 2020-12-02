# https://adventofcode.com/2020/day/2

import re

def parse_input(lines):
    for line in lines:
        if m := re.fullmatch(r"(\d+)-(\d+) (\w): (\w+)", line.strip()):
            lo, hi, char, password = m.groups()
            yield int(lo), int(hi), char, password

TEST = """\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

def is_valid_password(lo, hi, char, password):
    return lo <= password.count(char) <= hi

def test_is_valid_password():
    answers = [True, False, True]
    for args, answer in zip(parse_input(TEST.splitlines()), answers):
        assert is_valid_password(*args) == answer

def part1():
    valid = 0
    with open("day02_input.txt") as f:
        for lo, hi, char, password in parse_input(f):
            if is_valid_password(lo, hi, char, password):
                valid += 1
    print(f"Part 1: There are {valid} valid passwords")

if __name__ == "__main__":
    part1()

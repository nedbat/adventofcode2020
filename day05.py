# https://adventofcode.com/2020/day/5

import re
import pytest

def letter_binary(val, chars):
    return int(val.strip().replace(chars[0], "0").replace(chars[1], "1"), 2)

def boarding_pass_location(boarding_pass):
    row = letter_binary(boarding_pass[:7], "FB")
    col = letter_binary(boarding_pass[7:10], "LR")
    return row, col, row * 8 + col

@pytest.mark.parametrize("example", [
    "BFFFBBFRRR: row 70, column 7, seat ID 567.",
    "FFFBBBFRRR: row 14, column 7, seat ID 119.",
    "BBFFBBFRLL: row 102, column 4, seat ID 820.",
])
def test_boarding_pass_location(example):
    boarding_pass, row, col, seat_id = re.match(r"(\w+): row (\d+), column (\d+), seat ID (\d+)\.", example).groups()
    assert boarding_pass_location(boarding_pass) == tuple(map(int, (row, col, seat_id)))

def part1():
    with open("day05_input.txt") as f:
        seat_ids = [boarding_pass_location(boarding_pass)[2] for boarding_pass in f]
    print(f"Part 1: the highest seat ID is {max(seat_ids)}.")

if __name__ == '__main__':
    part1()

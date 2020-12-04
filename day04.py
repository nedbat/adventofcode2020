# https://adventofcode.com/2020/day/4

import re

def clauses_from_lines(lines):
    clause = []
    for line in lines:
        line = line.strip()
        if not line:
            if clause:
                yield "\n".join(clause)
                clause = []
        else:
            clause.append(line)
    if clause:
        yield "\n".join(clause)


def passports_from_file(fname):
    with open(fname) as f:
        for clause in clauses_from_lines(f):
            yield dict(m.groups() for m in re.finditer(r"(\w+):(\S+)", clause))

def test_passports_from_file():
    assert list(passports_from_file("day04_test.txt")) == [
        {
            "ecl": "gry",
            "pid": "860033327",
            "eyr": "2020",
            "hcl": "#fffffd",
            "byr": "1937",
            "iyr": "2017",
            "cid": "147",
            "hgt": "183cm",
        },
        {
            "iyr": "2013",
            "ecl": "amb",
            "cid": "350",
            "eyr": "2023",
            "pid": "028048884",
            "hcl": "#cfa07d",
            "byr": "1929",
        },
        {
            "hcl": "#ae17e1",
            "iyr": "2013",
            "eyr": "2024",
            "ecl": "brn",
            "pid": "760753108",
            "byr": "1931",
            "hgt": "179cm",
        },
        {
            "hcl": "#cfa07d",
            "eyr": "2025",
            "pid": "166559648",
            "iyr": "2011",
            "ecl": "brn",
            "hgt": "59in",
        },
    ]

def valid_passport(pp):
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return all(k in pp for k in required)

def num_valid_in_file(fname):
    return sum(1 for pp in passports_from_file(fname) if valid_passport(pp))
    
def test_valid_passport():
    assert num_valid_in_file("day04_test.txt") == 2

def part1():
    print(f"Part 1: There are {num_valid_in_file('day04_input.txt')} valid passports")

if __name__ == "__main__":
    part1()

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

def valid_byr(val):
    return len(val) == 4 and (1920 <= int(val) <= 2002)

def valid_iyr(val):
    return len(val) == 4 and (2010 <= int(val) <= 2020)

def valid_eyr(val):
    return len(val) == 4 and (2020 <= int(val) <= 2030)

def valid_hgt(val):
    if m := re.fullmatch(r"(\d+)(cm|in)", val):
        num = int(m[1])
        if m[2] == "cm":
            return 150 <= num <= 193
        else:
            return 59 <= num <= 76
    return False

def valid_hcl(val):
    return bool(re.fullmatch(r"#[0-9a-f]{6}", val))

def valid_ecl(val):
    return val in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def valid_pid(val):
    return bool(re.fullmatch(r"\d{9}", val))

def valid_passport_2(pp):
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for key in required:
        if key not in pp:
            return False
        if not globals()[f"valid_{key}"](pp[key]):
            return False
    return True

def num_valid2_in_file(fname):
    return sum(1 for pp in passports_from_file(fname) if valid_passport_2(pp))
    
def part2():
    print(f"Part 2: There are {num_valid2_in_file('day04_input.txt')} valid passports")

if __name__ == "__main__":
    part2()

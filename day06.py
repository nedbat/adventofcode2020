# https://adventofcode.com/2020/day/6

import itertools
import textwrap

def clauses_from_lines(lines):
    clause = []
    for line in itertools.chain(lines, [""]):
        line = line.strip()
        if not line:
            if clause:
                yield "\n".join(clause)
                clause = []
        else:
            clause.append(line)

def test_clauses_from_lines():
    lines = textwrap.dedent("""\
        abc
        abc

        def


        end
        bye
        """).splitlines()
    assert list(clauses_from_lines(lines)) == [
        "abc\nabc", "def", "end\nbye"
        ]

def part1():
    total = 0
    with open("day06_input.txt") as f:
        for answers in clauses_from_lines(f):
            total += len(set(answers.replace("\n", "")))
    print(f"Part 1: The sum of the number of questions is {total}")

if __name__ == '__main__':
    part1()

def part2():
    total = 0
    with open("day06_input.txt") as f:
        for answers in clauses_from_lines(f):
            all_answered = set.intersection(*(set(a) for a in answers.splitlines()))
            total += len(all_answered)
    print(f"Part 2: The sum of the number of questions is {total}")

if __name__ == '__main__':
    part2()

# https://adventofcode.com/2020/day/18

import re

import pytest


def eval(expr):
    toks = iter(re.findall(r"(\d+|\S)", expr) + ["eof"])
    return _eval(toks)

def _eval(toks):
    t = next(toks)
    if t == "(":
        val = _eval(toks)
    else:
        val = int(t)

    while True:
        t = next(toks)
        if t == ")" or t == "eof":
            return val
        elif t in "+*":
            op = t
            t = next(toks)
            if t == "(":
                num = _eval(toks)
            else:
                num = int(t)
            if op == "+":
                val += num
            else:
                val *= num


@pytest.mark.parametrize("expr, ans", [
    ("17", 17),
    ("1 + 2 * 3 + 4 * 5 + 6", 71),
    ("1 + (2 * 3) + (4 * (5 + 6))", 51),
    ("2 * 3 + (4 * 5)", 26),
    ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
    ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
    ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632),
])
def test_eval(expr, ans):
    assert eval(expr) == ans

if __name__ == "__main__":
    with open("day18_input.txt") as f:
        ans = sum(eval(line) for line in f)
    print(f"Part 1: {ans}")


# Part 2 needs a real parser

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.eat()

    def eat(self):
        self.token = next(self.tokens, "eof")

    def expect(self, tok):
        if self.token == tok:
            self.eat()
        else:
            raise Exception(f"Expected {tok!r}, had {self.token!r}")

    def star(self):
        val = self.plus()
        while self.token == "*":
            self.eat()
            val *= self.plus()
        return val

    def plus(self):
        val = self.value()
        while self.token == "+":
            self.eat()
            val += self.value()
        return val

    def value(self):
        if self.token == "(":
            self.eat()
            val = self.star()
            self.expect(")")
        else:
            val = int(self.token)
            self.eat()
        return val

def eval2(expr):
    toks = iter(re.findall(r"(\d+|\S)", expr))
    val = Parser(toks).star()
    return val

@pytest.mark.parametrize("expr, ans", [
    ("17", 17),
    ("1 + 2 * 3 + 4 * 5 + 6", 231),
    ("1 + (2 * 3) + (4 * (5 + 6))", 51),
    ("2 * 3 + (4 * 5)", 46),
    ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445),
    ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060),
    ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340),
])
def test_eval2(expr, ans):
    assert eval2(expr) == ans

if __name__ == "__main__":
    with open("day18_input.txt") as f:
        ans = sum(eval2(line) for line in f)
    print(f"Part 2: {ans}")

# https://adventofcode.com/2020/day/8

from enum import Enum

import pytest


class Op(Enum):
    acc = 1
    jmp = 2
    nop = 3

def read_program(fname):
    program = []
    with open(fname) as f:
        for line in f:
            op, num = line.split()
            program.append((Op.__members__[op], int(num)))
    return program

class Cpu:
    def __init__(self, program, tweaks=None):
        self.program = program
        self.tweaks = tweaks or {}
        self.ip = 0
        self.acc = 0
        self.ips_executed = set()

    def step(self):
        op, num = self.tweaks.get(self.ip, self.program[self.ip])
        self.ips_executed.add(self.ip)
        if op == Op.acc:
            self.acc += num
        elif op == Op.jmp:
            self.ip += num - 1
        elif op == Op.nop:
            pass
        self.ip += 1

    def about_to_repeat(self):
        return self.ip in self.ips_executed

    def part1(self):
        while not self.about_to_repeat():
            self.step()
        return self.acc

    def done(self):
        return self.ip == len(self.program)

    def part2(self):
        while True:
            if self.about_to_repeat():
                return None
            if self.done():
                return self.acc
            self.step()


def test_part1():
    cpu = Cpu(read_program("day08_test.txt"))
    assert cpu.part1() == 5

if __name__ == "__main__":
    cpu = Cpu(read_program("day08_input.txt"))
    acc = cpu.part1()
    print(f"Part 1: Immediately before any instruction is executed a second time, {acc} is in the accumulator.")

def part2(fname):
    program = read_program(fname)
    for i, (op, num) in enumerate(program):
        if op == Op.jmp:
            tweaks = {i: (Op.nop, num)}
        elif op == Op.nop:
            tweaks = {i: (Op.jmp, num)}
        elif op == Op.acc:
            continue
        cpu = Cpu(program, tweaks)
        acc = cpu.part2()
        if acc is not None:
            return acc

def test_part2():
    assert part2("day08_test.txt") == 8

if __name__ == "__main__":
    acc = part2("day08_input.txt")
    print(f"Part 2: {acc} is in the accumulator.")

# https://adventofcode.com/2020/day/14

import itertools
import re

def read_steps(fname):
    with open(fname) as f:
        for line in f:
            yield re.findall(r"\w+", line)

def mask_to_and_or(mask):
    return (
        int(mask.replace("X", "1"), 2),
        int(mask.replace("X", "0"), 2)
    )

def run_steps(fname):
    mem = {}
    amask = omask = 0
    for steps in read_steps(fname):
        if steps[0] == "mask":
            amask, omask = mask_to_and_or(steps[1])
        elif steps[0] == "mem":
            addr = int(steps[1])
            val = int(steps[2])
            mem[addr] = val & amask | omask
    return mem

def part1():
    mem = run_steps("day14_input.txt")
    ans = sum(mem.values())
    print(f"{len(mem)=}")
    print(f"Part 1: {ans}")

if __name__ == '__main__':
    part1()

def addresses(start, mask):
    omask = int(mask.replace("X", "0"), 2)
    amask = int(mask.replace("0", "1").replace("X", "0"), 2)
    nx = mask.count("X")
    exponents = [len(mask) - m.start() - 1 for m in re.finditer("X", mask)]
    for bits in itertools.product((0, 1), repeat=nx):
        value = start & amask | omask
        for exp, bit in zip(exponents, bits):
            if bit:
                value |= 2 ** exp
        yield value

def test_addresses():
    assert list(addresses(42, "000000000000000000000000000000X1001X")) == [26, 27, 58, 59]

def run_steps_2(fname):
    mem = {}
    for steps in read_steps(fname):
        if steps[0] == "mask":
            mask = steps[1]
        elif steps[0] == "mem":
            for addr in addresses(int(steps[1]), mask):
                mem[addr] = int(steps[2])
    return mem

if __name__ == '__main__':
    mem = run_steps_2("day14_input.txt")
    ans = sum(mem.values())
    print(f"{len(mem)=}")
    print(f"Part 2: {ans}")

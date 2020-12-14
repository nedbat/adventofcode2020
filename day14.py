# https://adventofcode.com/2020/day/14

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
    print(f"Part 1: {ans}")

if __name__ == '__main__':
    part1()

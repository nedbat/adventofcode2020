import functools
import math

def iterate(fn, val):
    while True:
        yield val
        val = fn(val)

def fix_point(seq):
    last = None
    for val in seq:
        if val == last:
            return last
        last = val

def product(nums):
    return functools.reduce((lambda a, b: a * b), nums)

def lcm2(a, b):
    return int(a * b / math.gcd(a, b))

def lcm(nums):
    return functools.reduce(lcm2, nums)

def modular_inverse(a, m):
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        # q is quotient
        if m == 0:
            return None
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if x < 0:
        x += m0

    return x

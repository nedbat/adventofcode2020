# https://adventofcode.com/2020/day/13

x = None

TEST = (
    939,
    {7,13,x,x,59,x,31,19}
)

def part1(time_now, bus_ids):
    bus_ids = set(filter(None, bus_ids))
    best_bus = min(bus_ids, key=lambda b: b - (time_now % b))
    return best_bus * (best_bus - (time_now % best_bus))

def test_part1():
    assert part1(*TEST) == 295

INPUT = (
    1001612,
    {19,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,821,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,463,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23}
)

if __name__ == '__main__':
    ans = part1(*INPUT)
    print(f"Part 1: {ans}")

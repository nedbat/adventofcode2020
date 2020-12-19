# https://adventofcode.com/2020/day/19

def read_rules(lines):
    rules = {}
    for line in lines:
        num, _, rule = line.partition(": ")
        if rule.startswith('"'):
            rules[num] = rule[1]
        else:
            rules[num] = [part.split() for part in rule.split("|")]
    return rules

TEST_RULES = read_rules("""\
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"
""".splitlines())

TEST_MESSAGES = """\
ababbb
bababa
abbbab
aaabbb
aaaabbb
""".splitlines()

def match_rule(rules, rule_name, message, start):
    """Yields up_to values, where it matches to."""
    rule = rules[rule_name]
    if isinstance(rule, str):
        if message.startswith(rule, start):
            yield start + len(rule)
    else:
        yield from match_alternatives(rules, rule, message, start)

def match_alternatives(rules, rule_alts, message, start):
    for rule_seq in rule_alts:
        yield from match_sequence(rules, rule_seq, message, start)

def match_sequence(rules, rule_seq, message, start):
    if not rule_seq:
        yield start
    else:
        for up_to in match_rule(rules, rule_seq[0], message, start):
            yield from match_sequence(rules, rule_seq[1:], message, up_to)

def matches(rules, message):
    for up_to in match_rule(rules, "0", message, 0):
        if up_to == len(message):
            return True
    return False

def num_matches(rules, messages):
    return sum(matches(rules, m.strip()) for m in messages)

def test_matches():
    assert num_matches(TEST_RULES, TEST_MESSAGES) == 2

RULES = read_rules(open("day19_rules.txt"))
MESSAGES = list(open("day19_messages.txt"))

if __name__ == "__main__":
    ans = num_matches(RULES, MESSAGES)
    print(f"Part 1: {ans}")

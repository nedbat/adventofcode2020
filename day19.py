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

TEST_RULES_2 = read_rules("""\
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1
""".splitlines())

TEST_MESSAGES_2 = """\
abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
""".splitlines()

def updated_rules(rules):
    rules = dict(rules)
    rules["8"] = [["42"], ["42", "8"]]
    rules["11"] = [["42", "31"], ["42", "11", "31"]]
    return rules

def test_part2():
    assert num_matches(TEST_RULES_2, TEST_MESSAGES_2) == 3
    assert num_matches(updated_rules(TEST_RULES_2), TEST_MESSAGES_2) == 12

if __name__ == "__main__":
    ans = num_matches(updated_rules(RULES), MESSAGES)
    print(f"Part 2: {ans}")

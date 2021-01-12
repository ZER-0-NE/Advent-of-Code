# credits to sophiebits

# HARD 
import re
import sys

rules, strings = [l.rstrip('\n') for l in sys.stdin.read().split('\n\n')]

rules = dict([rule.split(': ', 1) for rule in rules.split('\n')])
def getre(rulenum):
    # for part 1, delete these two rules:
    if rulenum == '8':
        return getre('42') + '+'
    elif rulenum == '11':
        a = getre('42')
        b = getre('31')
        return '(?:' + '|'.join(f'{a}{{{n}}}{b}{{{n}}}' for n in range(1, 100)) + ')'

    rule = rules[rulenum]
    if re.fullmatch(r'"."', rule):
        return rule[1]
    else:
        parts = rule.split(' | ')
        res = []
        for part in parts:
            nums = part.split(' ')
            res.append(''.join(getre(num) for num in nums))
        return '(?:' + '|'.join(res) + ')'


z = getre('0')
ct = 0
for string in strings.split('\n'):
    ct += bool(re.fullmatch(z, string))
print(ct)

# another sol

def test(s, seq):
	# given string s and list of rules seq, is there a way to produce s using seq?
	if s == '' or seq == []:
		return s == '' and seq == [] # if both are empty, True. if only one, false
	r = rules[seq[0]]
	print(r, s[0])
	if '"' in r:
		if s[0] in r:
			return test(s[1:], seq[1:]) # strip first character
		else:
			return False # wrong first character
	else:
		return any(test(s, t+seq[1:]) for t in r) #expand first term



def parse_rule(s):
	n, e = s.split(": ")
	if '"' not in e:
		e = [[int(r) for r in t.split()] for t in e.split("|")]
	return (int(n), e)

rule_text, messages = [x.splitlines() for x in open('data.txt').read().split('\n\n')]
rules = dict(parse_rule(s) for s in rule_text)
# print(rules)
print("Part 1:", sum(test(m,[0]) for m in messages))

rule_text += ["8: 42 | 42 8","11: 42 31 | 42 11 31"]
rules = dict(parse_rule(s) for s in rule_text)
print("Part 2:", sum(test(m,[0]) for m in messages)) 
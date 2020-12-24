from functools import reduce

with open ('data.txt', 'r') as f:
	lines = f.read().strip().split('\n')

def trigger(x, y):
	if not x:
		return False
	else:
		return abs(ord(x[-1]) - ord(y)) == 32

def react(polymer):
	return reduce((lambda x, y: x[:-1] if trigger(x,y) else x+y), polymer)

print(f"1. {len(react(lines[0]))}")

# another solution for part1

alphabet = "abcdefghijklmnopqrstuvwxyz"
pairs = [c + c.upper() for c in alphabet]
pairs += [c.upper() + c for c in alphabet]


def react(s):
	for p in pairs:
		s = s.replace(p,"")
	return s

def full_react(s):
	ps = data
	s = data

	while True:
		s = react(ps)
		if s == ps:
			break
		ps = s
	return s

data = lines[0]
print(f"1. {len(full_react(data))}")
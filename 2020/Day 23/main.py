inp = "398254716"
N = 0

def shift_three(s):
	c1 = next_cup[s]
	c2 = next_cup[c1]
	c3 = next_cup[c2]

	d = s-1 if current>1 else N

	while d in [c1, c2, c3]:
		d = d-1 if d>1 else N
	assert d not in [c1, c2, c3] and s not in [c1, c2, c3]
	next_cup[s] = next_cup[c3]
	next_cup[c3] = next_cup[d]
	next_cup[d] = c1


def part1():
	c = 1
	s = ""
	for _ in range(N-1):
		c = next_cup[c]
		s += str(c)

	print(f"1. {s}")

def part2():
	result = next_cup[1] * next_cup[next_cup[1]]
	print(f"2. {result}")

# part 1
cups = list(map(int, list(inp)))
next_cup = {c:n for c, n in zip(cups, cups[1:] + [cups[0]])}
# print(next_cup)
N = len(cups)

current = cups[0]

for _ in range(100):
	shift_three(current)
	current = next_cup[current]

part1()

# part 2
cups = list(map(int, list(inp))) + list(range(10, 1000001))
next_cup = {c:n for c, n in zip(cups, cups[1:] + [cups[0]])}
N = len(cups)

current = cups[0]

for _ in range(10000000):
	shift_three(current)
	current = next_cup[current]

part2()
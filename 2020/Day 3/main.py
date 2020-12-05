with open('data.txt', 'r') as f:
	rows = f.read().strip().split('\n')

# print(rows)


def part1(data , r, d):
	tree = 0
	n, m = len(data), len(data[0]) # 323, 31
	j = 0
	for i in range(0, n, d):
		if data[i][j] == '#':
			tree += 1
		j = (j+r)%m
	return tree



print(f"Part 1: {part1(rows, 3, 1)}")
print(f"Part 2: {part1(rows, 3, 1) * part1(rows, 1, 1) * part1(rows, 5, 1) * part1(rows, 7, 1) * part1(rows, 1, 2)}")
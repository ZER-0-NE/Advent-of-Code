from itertools import combinations

with open('data.txt', 'r') as f:
	rows = f.read().strip().split('\n')


res = []
for x, y in combinations(rows, 2):
	if int(x) + int(y) == 2020:
		res.append(int(x) * int(y))

print(res[0])

for x, y, z in combinations(rows, 3):
	if int(x) + int(y) + int(z) == 2020:
		res.append(int(x) * int(y) * int(z))

print(res[1])
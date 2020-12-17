with open('data.txt', 'r') as f:
	rows = f.read().strip().split('\n')

from collections import Counter


twice, thrice = 0, 0

for num in rows:
	c = Counter(Counter(num).values())
	if 2 in c:
		twice+=1
	if 3 in c:
		thrice +=1

print(f"1. {twice * thrice}")

from itertools import combinations

for one, two in combinations(rows, 2):
	diff = [i for i, j in zip(one, two) if i == j]
	print(diff)
	if len(two) - len(diff) == 1:
		print(f"2. {''.join(diff)}")
		break



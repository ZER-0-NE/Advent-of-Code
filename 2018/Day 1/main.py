with open('data.txt', 'r') as f:
	rows = f.read().strip().split('\n')

print(f"1. {sum(int(i) for i in rows)}")

import itertools

seen = set()
res = 0
for num in itertools.cycle(rows):
	res += int(num)
	if res in seen:
		print(f"2. {res}")
		break
	seen.add(res)
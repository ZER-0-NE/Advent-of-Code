import math

with open('data.txt', 'r') as f:
	rows = f.read().strip().split('\n')

# part 1

res = 0

for num in rows:
	res += math.floor(int(num)/3) - 2

print(res)

# part 2
n = 0

for num in rows:
	res = math.floor(int(num)/3) - 2
	n += res
	while (int(res/3) - 2) > 0:
		res = math.floor(int(res)/3) - 2
		n+= res

print(n)
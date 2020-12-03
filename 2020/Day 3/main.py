from itertools import combinations
from collections import Counter

with open('data.txt', 'r') as f:
	rows = f.read().strip().split('\n')

# part 1
count1 = 0

for i in rows:
	num, c, s = i.split()
	n, m = map(int, num.split('-'))
	counter = Counter(s)
	if counter[c[0]] >= n and counter[c[0]] <= m:
		count1+=1

print(count1)


# part 2

count2 = 0

for i in rows:
	num, c, s = i.split()
	n, m = map(int, num.split('-'))
	if (c[0] == s[n-1]) + (c[0] == s[m-1]) == 1:
		count2+=1


print(count2)
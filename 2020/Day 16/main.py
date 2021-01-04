import re
import math
# departure location: 47-874 or 885-960
# departure station: 25-616 or 622-964
# departure platform: 42-807 or 825-966
# departure track: 36-560 or 583-965
# departure date: 37-264 or 289-968
# departure time: 27-325 or 346-954
# arrival location: 37-384 or 391-950
# arrival station: 35-233 or 244-963
# arrival platform: 26-652 or 675-949
# arrival track: 41-689 or 710-954
# class: 27-75 or 81-952
# duration: 45-784 or 807-967
# price: 40-350 or 374-970
# route: 30-892 or 904-968
# row: 47-144 or 151-957
# seat: 28-750 or 773-973
# train: 30-456 or 475-950
# type: 34-642 or 648-968
# wagon: 42-486 or 498-970
# zone: 37-152 or 167-973

# your ticket:
# 83,137,101,73,67,61,103,131,151,127,113,107,109,89,71,139,167,97,59,53

# nearby tickets:
# 191,477,199,428,5,724,512,212


#PART 1
with open('data.txt', 'r') as f:
	data = f.read().split('\n\n')

# print(data[0])

rule_pattern = re.compile(r'([ a-z]+): (\d+)-(\d+) or (\d+)-(\d+)')
rules = {}

for match in rule_pattern.finditer(data[0]):
	name, a, b, c, d = match.groups()
	# print(a, b, c,d)
	rules[name] = set.union(set(range(int(a), int(b)+1)), range(int(c), int(d)+1))
	# print(rules)

all_fields = set.union(*rules.values())

my_ticket = [int(n) for n in data[1].splitlines()[1].split(',')]

nearby_tickets = [[int(n) for n in line.split(',')] for line in data[2].splitlines()[1:]]

# print(my_ticket, nearby_tickets)

print(f"1. {sum(num for ticket in nearby_tickets for num in ticket if num not in all_fields)}")




# another solution: (credits to r0f1 on github)

import numpy as np

with open('data.txt', 'r') as f:
	lines = [x.strip() for x in f]

# print(lines)

sep1 = 'your ticket:'
sep2 = 'nearby tickets:'

part1 = lines[:lines.index(sep1)-1]

your_tickets = [int(n) for n in lines[lines.index(sep1)+1].split(',')]

part3 = lines[lines.index(sep2)+1:]

allowed = []

for line in part1:
	a = set()
	ranges = line.split(':')[1]
	for r in ranges.split(' or '):
		lb, ub = int(r.split('-')[0]), int(r.split('-')[1])
		for i in range(lb, ub+1):
			a.add(i)
	allowed.append(a) # get all allowed numbers 


score = []
c = len(part1)

#create a 1's matrix where each 0 position would indicate discarded tickets with invalid values from part 1
poss_mat = np.ones((c,c), dtype=np.uint8) 

for line in part3:
	okay = True
	numbers = [int(n) for n in line.split(',')]
	for n in numbers:
		if not any(n in a for a in allowed):
			score.append(n)
			okay = False
	if okay:
		for field_x, n in enumerate(numbers):
			for j, a in enumerate(allowed):
				if n not in a:
					poss_mat[field_x][j] = 0

print(f"1. {sum(score)}")

# print(poss_mat)

change = True
seen = set()

while change:
	change = False
	for i, row in enumerate(poss_mat):
		if sum(row) == 1 and i not in seen:
			seen.add(i)
			change = True
			col = np.argmax(row)
			poss_mat[:, col] = 0
			poss_mat[i, col] = 1

res = 1
for j, row in enumerate(poss_mat):
	if np.argmax(row)<6:
		# print(row)
		res *= your_tickets[j]

print(f"2. {res}")
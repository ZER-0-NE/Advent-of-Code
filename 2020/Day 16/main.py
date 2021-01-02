import re

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

with open('data.txt', 'r') as f:
	data = f.read().split('\n\n')

# print(data[0])

rule_pattern = re.compile(r'([a-z]+): (\d+)-(\d+) or (\d+)-(\d+)')
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



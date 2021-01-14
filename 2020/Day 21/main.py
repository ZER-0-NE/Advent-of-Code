with open('data.txt', 'r') as f:
	data = f.read().splitlines()

allergens = {}
ingredients = []

for e in data:
	a,b = e.rstrip(')').split('(contains ')
	# print(a, b)
	ingr = a.split()
	ingredients.append(ingr)
	for a in b.split(", "):
		if a not in allergens:
			allergens[a] = set(ingr)
		else:
			allergens[a] &= set(ingr)
# print(allergens)
all_allergs = set(e for a in allergens.values() for e in a)
print(f"1. {sum(i not in all_allergs for ingr in ingredients for i in ingr)}")

def remove(a, allergs):
	s = set()
	for k in allergs:
		
		if len(allergs[k])>1 and a in allergs[k]:
			allergs[k].remove(a)
			if len(allergs[k]) == 1:
				s |= allergs[k]
	return s

r = next(list(v) for v in allergens.values() if len(v) == 1)

while r:
	r += list(remove(r.pop(), allergens))

print(f"2. {','.join(str(i.pop()) for a,i in sorted((k,v) for k, v in allergens.items()))}")
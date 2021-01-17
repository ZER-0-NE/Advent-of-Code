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

# another sol

import re

pat = re.compile(r"^([a-z\s]+) \(contains ([a-z,\s]+)\)$")

ingredients = []
allergen_reference = dict()

for i, line in enumerate(open('data.txt')):
	ing, allerg = pat.match(line).groups()
	ingredients.append(ing.split())
	for al in allerg.split(", "):
		this_list = allergen_reference.get(al, list())
		this_list.append(i)
		allergen_reference[al] = this_list

allergen_candidates = {
	key: set.intersection(*[set(ingredients[k]) for k in allergen_reference[key]])
	for key, value in allergen_reference.items()
}

no_ingredient = set(i for l in ingredients for i in l).difference(set.union(*(allergen_candidates.values())))

print(f"1. {len([i for l in ingredients for i in l if i in no_ingredient])}")

visited = set()
while any(len(s) > 1 for s in allergen_candidates.values()):
    for key, value in allergen_candidates.items():
        if len(value) == 1 and key not in visited:
            visited.add(key)
            break
    for key2, value2 in allergen_candidates.items():
        if key2 != key:
            value2.difference_update(value)
    
print(",".join(next(iter(v)) for _, v in sorted(allergen_candidates.items(), key=lambda v: v[0])))
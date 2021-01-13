with open('data.txt', 'r') as f:
	data = f.read().split()

data = [int(x) for x in data]

def parse(data):
	children, metas = data[:2]
	data = data[2:]
	scores = []
	totals = 0

	for i in range(children):
		total, score, data = parse(data)
		totals += total
		scores.append(score)

	totals += sum(data[:metas])

	if children == 0:
		return (totals, sum(data[:metas]), data[metas:])
	else:
		return (totals,
			sum(scores[k-1] for k in data[:metas] if k>0 and k<=len(scores)),
			data[metas:])
total, value, remaining = parse(data)

print(f"1: {total}")
print(f"2: {value}")

# another sol; credits to michaelmarsalek


def sumtree(t):
	ch = t.pop(0)
	md = t.pop(0)
	return sum(sumtree(t) for _ in range(ch)) + sum(t.pop(0) for _ in range(md))

print(f"1. {sumtree(data)}")

def val(t):
	ch = t.pop(0)
	md = t.pop(0)
	vals = [val(t) for _ in range(ch)]
	mdata = [t.pop(0) for _ in range(md)]

	if ch == 0:
		return sum(mdata)
	return sum(vals[i-1] for i in mdata if i-1 in range(ch))

print(f"2. {val(data)}")


# another sol; credits to mastermedo

def solve(child, meta):
	if child == 0:
		return sum(next(dta) for _ in range(meta))

	value = 0
	children = {}

	for i in range(1, child+1):
		value += solve(next(dta), next(dta)) # comment for pt2
		# children[i] = solve(next(dta), next(dta))

	for _ in range(meta):
		value += next(dta)# comment for pt2
		# value += children.get(next(dta), 0)

	return value


dta = iter(map(int, open('data.txt').read().split()))

print(f"1. {solve(next(dta), next(dta))}")
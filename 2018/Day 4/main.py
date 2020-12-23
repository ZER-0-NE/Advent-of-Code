# inspired from jonathon_paulson on reddit

from collections import defaultdict

with open ('data.txt', 'r') as f:
	lines = f.read().split('\n')
	lines.sort()

def parseTime(line):
	words = line.split()
	date, time = words[0][1:], words[1][:-1]
	return int(time.split(':')[1])

asleep, guard = None, None

C = defaultdict(int)
CM = defaultdict(lambda: defaultdict(int))
CMM = defaultdict(int)

for line in lines:
	if line:
		time = parseTime(line)
		if 'begins shift' in line:
			guard = int(line.split()[3][1:])
			asleep = None
		elif 'falls asleep' in line:
			asleep = time
		elif 'wakes up' in line:
			for t in range(asleep, time):
				CMM[(guard,t)] += 1
				CM[guard][t] +=1
				C[guard] += 1
# print(CM)

def argmax(d):
	best = None
	for k,v in d.items():
		if best is None or v > d[best]:
			best = k
	return best

best_guard = argmax(C)
best_min = argmax(CM[best_guard])

best_g, best_m = argmax(CMM)

print(f"1. {best_guard*best_min}")

print(f"2. {best_g*best_m}")
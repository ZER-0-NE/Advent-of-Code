with open('data.txt') as f:
    data = f.read().strip().split('\n')
# print(data)

# part 1
acc = 0
seen = set()
pc = 0
while True:
	if pc == len(data) or pc in seen:
		break
	seen.add(pc)
	
	line = data[pc]
	op, arg = line.split(" ")
	# print(op, arg, acc)
	
	if op == 'nop':
		pass
	elif op == 'acc':
		acc += int(arg)
	elif op == "jmp":
		pc += int(arg)
		continue
	
	pc+=1

print(acc)


# part 2

# part 2

def prog(data):
	acc = 0
	seen = set()
	pc = 0
	while True:
		if pc == len(data):
			return acc
		if pc in seen:
			return None
		seen.add(pc)
		
		line = data[pc]
		op, arg = line.split(" ")
		# print(op, arg, acc)
		
		if op == 'nop':
			pass
		elif op == 'acc':
			acc += int(arg)
		elif op == "jmp":
			pc += int(arg)
			continue
		
		pc+=1

	return acc

for i in range(len(data)):
	line = data[:]

	if line[i].startswith('jmp'):
		line[i] = line[i].replace('jmp', 'nop')
	elif line[i].startswith('nop'):
		line[i] = line[i].replace('nop', 'jmp')

	x = prog(line)

	if x:
		print(x)

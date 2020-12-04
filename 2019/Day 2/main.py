with open('data.txt', 'r') as f:
	rows = f.read().strip().split(',')

# part 1

res = 0

# print(rows)

for i in range(len(rows)):
    rows[i] = int(rows[i])

for i in range(0, len(rows)-1, 4):
	one = rows[i]
	two = rows[i+1]
	three = rows[i+2]
	four = rows[i+3]

	if one == 1:
		rows[four] = rows[two] + rows[three]
	elif one == 2:
		rows[four] = rows[two] * rows[three]
	elif one == 99:
		break


print(rows[0])

# part 2

for x in range(100):
	for y in range(100):

		with open('data.txt', 'r') as f:
			rows = f.read().strip().split(',')

		for i in range(len(rows)):
			rows[i] = int(rows[i])

		rows[1] = x
		rows[2] = y

		for i in range(0, len(rows)-1, 4):
			one = rows[i]
			two = rows[i+1]
			three = rows[i+2]
			four = rows[i+3]

			if one == 1:
				rows[four] = rows[two] + rows[three]
			elif one == 2:
				rows[four] = rows[two] * rows[three]
			elif one == 99:
				break

		if rows[0] == 19690720:
			print(x, y)

# credits to suprajs user on reddit!

instructions = [(l.strip()[0], int(l.strip()[1:])) for l in open('data.txt', 'r')]

distance = {'N':0, 'E':0, 'W':0, 'S': 0}
dirs = 'ESWN'
curr_dir = dirs[0]

def changeDirection(turn: str, angle: int):
    if turn == 'L':
        return -angle//90
    if turn == 'R':
        return angle//90


for instr in instructions:
	if instr[0] == 'L' or instr[0] == 'R':
		curr_dir = dirs[(dirs.find(curr_dir) + changeDirection(instr[0],instr[1]))%4]
	elif instr[0] == 'F':
		distance[curr_dir] += instr[1]
	else:
		distance[instr[0]] += instr[1]

print(f"1. {abs(distance['N'] - distance['S']) + abs(distance['E'] - distance['W'])}")

# Part 1 solution using complex numbers (credits to jvanelteren on github):

lines = [line.rstrip('\n') for line in open('data.txt', 'r')]

direc = complex(1,0) # starts from 1 unit east
location = complex(0,0)

for line in lines:
	ins = line[0]
	amount = int(line[1:])
	if ins == 'N':
		location += complex(0, amount)
	if ins == 'E':
		location += complex(amount, 0)
	if ins == 'W':
		location += complex(-amount, 0)
	if ins == 'S':
		location += complex(0, -amount)
	if ins == 'F':
		location += direc*amount
	if ins == 'L':
		for i in range(amount//90):
			direc *= 1j
	if ins == 'R':
		for i in range(amount//90):
			direc *=-1j

print(f"1. {abs(location.real) + abs(location.imag)}")

# Part 1 solution using math library and direct dictionary for directions (credits to donth77 on github)

from math import sin, cos, radians

dirs = {'N' :(0,1), 'E' :(1,0), 'W' :(-1,0), 'S' :(0,-1)}

xpos, ypos = 0, 0
angle = 90 # E

with open('data.txt', 'r') as f:
	line = f.readline()

	while line:
		action, value = line[0], int(line.strip()[1:])

		if action in dirs:
			dx, dy = dirs[action]
			xpos += value *dx
			ypos += value *dy
		elif action in {'L', 'R'}:
			angle += (value if action == 'R' else 360-value)
			angle %=360
		elif action == 'F':
			theta = radians(angle)
			xpos += int(sin(theta) * value)
			ypos += int(cos(theta) * value)
		line = f.readline()

print(f"1. {abs(xpos) + abs(ypos)}")


# Part 2 using complex numbers

lines = [line.rstrip('\n') for line in open('data.txt', 'r')]

location = complex(10,1) # starts from 10 unit east, 1 north
ship_loc = complex(0,0)

for line in lines:
	ins = line[0]
	amount = int(line[1:])
	if ins == 'N':
		location += complex(0, amount)
	if ins == 'E':
		location += complex(amount, 0)
	if ins == 'W':
		location += complex(-amount, 0)
	if ins == 'S':
		location += complex(0, -amount)
	if ins == 'F': # ship moves only in F
		ship_loc += location*amount
	if ins == 'L':
		for i in range(amount//90): #**** changes direction of waypoint
			location = complex(-location.imag, location.real)
	if ins == 'R':
		for i in range(amount//90):
			location = complex(location.imag, -location.real)

print(f"2. {abs(ship_loc.real) + abs(ship_loc.imag)}")
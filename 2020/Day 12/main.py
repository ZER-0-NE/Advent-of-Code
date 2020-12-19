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

print(abs(distance['N'] - distance['S']) + abs(distance['E'] - distance['W']))
with open('data.txt', 'r') as f:
	A,B = f.readlines()

dx = dict(zip('RULD', [1,0,-1,0]))
dy = dict(zip('RULD', [0,1,0,-1]))

def get_points(directions):
	x, y = 0, 0 # current position in the grid
	pts = {} # min distance traveled for each point visited
	length = 0 # the length of the path thus far

	for cmd in directions:
		side = cmd[0]
		dist = int(cmd[1:])

		for _ in range(dist):
			x += dx[side]
			y += dy[side]

			length+=1
			if not (x, y) in pts.keys():
				pts[(x,y)] = length

	return pts

path_a = get_points(A.split(','))
path_b = get_points(B.split(','))
intersects = path_a.keys() & path_b.keys()

# print(path_a)

print(f"1. {min(abs(x) + abs(y) for x,y in intersects)}")
print(f"2. {min(path_a[p] + path_b[p] for p in intersects)}")

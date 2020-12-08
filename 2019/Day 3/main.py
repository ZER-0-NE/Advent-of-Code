with open('data.txt', 'r') as f:
	A,B = f.readlines()

print(A.split(','))

dx = dict(zip('RULD', [1,0,-1,0]))
dy = dict(zip('RULD', [0,1,0,-1]))

# def get_points(directions):

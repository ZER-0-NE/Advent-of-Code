# part1: 
# Think about the mathematical representation of a line: y = ax + b, where a is the slope and b is the intercept.

# Now imagine you are testing one point in the grid to see how many asteroids are visible from that point. 
# Consider a frame of reference where this point is the origin (x = 0 and y = 0). For a line that goes through 
# the origin the intercept is zero (b = 0).

# Now you look around at each surrounding point, and calculate the slope. This is basically equivalent to 
# calling the atan2 function. Points with the same slope are on the same line. Since they are on the same 
# line, one of them will be visible (the closest one), the rest will be behind it (not visible). Therefore 
# the answer is the number of unique slope values calculated for all the points/asteroids in the grid.

# If you use the atan2 function you already have everything you need:

# - For each point

# calculate atan2to every other point and count the number of unique values - that will be the number of 
# visible asteroids

# - Return the maximum number of visible asteroids

# https://www.youtube.com/watch?v=p-xa-3V5KO8&feature=youtu.be&ab_channel=Numberphile

import math

with open('data.txt') as f:
	asteroid_map = f.read().split()


def get_monitoring_point(coordinates):
	max_asteroids = 0
	best_x = best_y = 0
	for x,y in asteroid_coordinates:
		point_slopes = set()
		for x2, y2 in asteroid_coordinates:
			if (x,y) != (x2,y2):
				dx, dy = x2-x, y2-y
				dx, dy = dx//math.gcd(dx,dy) , dy//math.gcd(dx,dy)
				point_slopes.add((dx,dy))
		if len(point_slopes) > max_asteroids:
			max_asteroids = len(point_slopes)
			best_x, best_y = x, y
	return max_asteroids, (best_x, best_y)

def get_vaporization_order(coordinates, mx, my):
	vaporized = [(mx, my)]
	while len(vaporized) != len(coordinates):
		closest_points = {}
		for x, y in coordinates:
			if (x, y) not in vaporized:
				dx, dy = x-mx, y-my
				dx, dy = dx//math.gcd(dx,dy) , dy//math.gcd(dx,dy)
				closest_x, closest_y = closest_points.get((dx,dy), (float('inf'), float('inf')))
				if abs(x-mx) + abs(y-my) < abs(closest_x-mx) + abs(closest_y-my):
					closest_points[(dx, dy)] = (x,y)
		vaporized += sorted(closest_points.values(), key=lambda p: -math.atan2(p[0]-mx, p[1]-my))

	return vaporized


asteroid_coordinates = [(x,y) for y, row in enumerate(asteroid_map) for x, value in enumerate(row) if value == '#']
# print(asteroid_coordinates)

part1, monitoring_point = get_monitoring_point(asteroid_coordinates)

print(f"1. {part1}")

vaporization_order = get_vaporization_order(asteroid_coordinates, monitoring_point[0], monitoring_point[1])
part2 = vaporization_order[200][0] * 100 + vaporization_order[200][1]

print(f"2. {part2}")



# another sol for part1:

with open('data.txt') as f:
	area = f.read()

def angle(A, B):
	return math.atan2(B[1]-A[1], B[0]-A[0])

x, y = -1, 0
l, sol, check = [], [], []

for i in range(len(area)):
	if area[i] == '\n':
		y += 1
		x = -2 # so that x becomes -1 when a new line starts
	x += 1

	if area[i] == '#':
		l.append((x,y))

for i in range(len(l)):
	check = []
	sol.append(len(l) - 1)
	for j in l:
		if angle(l[i], j) in check and l[i] != j:
			sol[i]-=1
		check.append(angle(l[i], j)) if l[i]!=j else None

print(max(sol))
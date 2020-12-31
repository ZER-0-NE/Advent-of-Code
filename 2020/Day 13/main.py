import numpy as np

with open('data.txt') as file:
	earliestt = int(file.readline())
	buses = [int(bus) for bus in file.readline().split(',') if bus != 'x']

print(f"1. {np.prod(min((bus - earliestt % bus, bus) for bus in buses))}")

# another solution part 1

from itertools import count

def earliest(buses, time):
	for departure in count(time):
		for b in buses:
			if departure%b == 0:
				return b * (departure - time)

print(f"1. {earliest(buses, int(earliestt))}")


# PART 2

with open('data.txt', 'r') as f:
	earliestt = int(f.readline())
	buses = [(index, int(bus)) for index, bus in enumerate(f.readline().split(',')) if bus!= 'x']

# print(buses)

time, step = 0, 1

for offset, bus in buses:
	while (time+offset)%bus:
		time+=step

	step*=bus

print(time)
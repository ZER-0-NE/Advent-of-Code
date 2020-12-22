import numpy as np
from itertools import count

with open('data.txt') as file:
	earliestt = int(file.readline())
	buses = [int(bus) for bus in file.readline().split(',') if bus != 'x']

print(f"1. {np.prod(min((bus - earliestt % bus, bus) for bus in buses))}")

# another solution part 1

def earliest(buses, time):
	for departure in count(time):
		for b in buses:
			if departure%b == 0:
				return b * (departure - time)

print(f"1. {earliest(buses, int(earliestt))}")
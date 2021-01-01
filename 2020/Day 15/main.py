data = [7,14,0,17,11,1,2]
test_data = [0,3,6]

last = dict()
lnum = None
for i in range(30000000): # change to 2020 for part 1
	if i<len(data):
		num = data[i]
	else:
		if lnum not in last:
			num = 0
		else:
			num = (i-1)-last[lnum]
	last[lnum] = i-1
	lnum = num

print(num)

# another solution

digit = 30000000
nums = {7:0, 14:1, 0:2, 17:3, 11:4, 1:5,}

lastnum = 2
pos = 6
while pos<digit-1:
	if lastnum in nums.keys():
		aux = lastnum
		lastnum = pos - nums[lastnum]
		nums[aux] = pos
	else:
		nums[lastnum] = pos
		lastnum = 0
	pos+=1

print(lastnum)
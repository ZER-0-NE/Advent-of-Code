with open('data.txt') as f:
    data = f.read().strip().split('\n')

nums = [int(x) for x in data]

def valid(nums, n):
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if nums[i] + nums[j] == n:
				return True
	return False


for i in range(25, len(nums)):
	if not valid(nums[i-25:i], nums[i]):
		target = nums[i]
		print("1: " + str(target))

for i in range(len(nums)):
	for j in range(i+1, len(nums)):
		if sum(nums[i:j]) == target:
			print("2: " + str(min(nums[i:j]) + max(nums[i:j])))

# Part 2 prints two answers. The second one is just 2*magic and comes from just selecting the 
# range [i, i+1) if i is the index with the magic number and can be ignored.

#credits to bluepichu
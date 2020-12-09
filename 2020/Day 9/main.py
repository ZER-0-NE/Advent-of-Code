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
		print(nums[i])

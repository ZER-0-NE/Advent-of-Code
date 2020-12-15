# with open('data.txt', 'r') as f:
# 	A,B = f.readlines().split('-')

A, B = 152085, 670283
def is_increasing(num):
	num = str(num)
	first_digit = num[0]

	for digit in num[1:]:
		if digit < first_digit:
			return False
		first_digit = digit

	return True

def two_adjacent_same(num):
	num = str(num)

	first_digit = num[0]

	for digit in num[1:]:
		if digit == first_digit:
			return True
		first_digit = digit

	return False

def double_adjacent_same(num):
	num = str(num)
	first_digit = num[0]

	group_len = 1

	for digit in num[1:]:
		if first_digit == digit:
			group_len += 1
		else:
			if group_len == 2:
				return True
			group_len = 1
			first_digit = digit

	return group_len == 2

res1, res2 = 0, 0

for i in range(A, B+1):
	if is_increasing(i) and two_adjacent_same(i):
		res1+=1
	if is_increasing(i) and double_adjacent_same(i):
		res2 += 1

print(f"1. {res1}")
print(f"2. {res2}")
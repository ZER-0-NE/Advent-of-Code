with open('data.txt', 'r') as f:
	data = f.read().strip().split('\n')

mem = {}

# for num in data:
# 	if num.startswith('mask'):
# 		_, mask = num.split('=')
# 	elif num.startswith('mem'):
# 		

lines = open('data.txt', 'r').read().splitlines()
instructions = [line.replace('mem', '').replace('[', '').replace(']', '').split(' = ') for line in lines]

print(instructions)
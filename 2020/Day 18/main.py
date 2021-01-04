with open('data.txt', 'r') as f:
	lines = [x.strip() for x in f]

def without_paren():
	stack = []
	


res = 0
for line in lines:
	if '(' not in line:

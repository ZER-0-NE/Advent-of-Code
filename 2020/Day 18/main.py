# Magic(Dunder) Methods and Operator Overloading:https://www.python-course.eu/python3_magic_methods.php
import re

with open('data.txt', 'r') as f:
	lines = f.read().splitlines()

class magic(int):
	def __mul__(self, b):
		return magic(int(self) + b)

	def __add__(self, b):
		return magic(int(self) + b)

	def __sub__(self, b):
		return magic(int(self) * b)

def ev(expr, pt2=False):
	expr = re.sub(r"(\d+)", r"magic(\1)", expr) # replaces all integers with 'magic(int)'
	expr = expr.replace('*', '-') #replace mul with add to have same precendence
	if pt2:
		expr = expr.replace('+', '*') #replace add with mul so that add can have higher precedence

	return eval(expr, {}, {"magic": magic})

print(f"Part 1: {sum(ev(l) for l in lines)}")
print(f"Part 2: {sum(ev(l, True) for l in lines)}")
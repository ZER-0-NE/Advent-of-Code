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


# another solution using ast (abstract syntax tree)

import ast
from typing import List

class SubToMult(ast.NodeTransformer):
	def visit_Sub(self, node):
		return ast.Mult()

class MultToAdd(ast.NodeTransformer):
	def visit_Mult(self, node):
		return ast.Add()

def part1(lines: List[str]):
	result = []
	for line in lines:
		tree = ast.parse(f"this_result = {line.replace('*', '-')}")
		print(f"tree: {tree}")
		SubToMult().visit(tree)
		code = compile(tree, filename="<ast>", mode="exec")
		exec(code, globals())
		result.append(this_result)
	return sum(result)

def part2(lines: List[str]):
	result = []
	for line in lines:
		tree = ast.parse(f"this_result = {line.replace('*', '-').replace('+', '*')}")
		MultToAdd().visit(tree)
		SubToMult().visit(tree)
		code = compile(tree, filename="<ast>", mode="exec")
		exec(code, globals())
		result.append(this_result)
	return sum(result)

print(f"1: {part1(lines)}")
print(f"2: {part2(lines)}")

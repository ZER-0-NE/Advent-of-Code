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


# another solution using deque

import re
from collections import deque
from math import prod
from operator import add, mul

def equal_precedence(tokens, operators={'+': add, '*': mul}):
	tokens = deque(tokens.split())
	res = int(tokens.popleft())
	while tokens:
		op, nr = tokens.popleft(), int(tokens.popleft())
		res = operators[op](res, nr)
	return res

def add_before(tokens):
	return prod(map(equal_precedence, tokens.split('*')))

def evaluate(tokens, inner_eval, brackets_regex = re.compile(r'(\([^()]+\))')):
	'''
	the regex outputs the innermost brackets to evaluate them :- <re.Match object; span=(4, 23), 
	match='(3 + 9 * 2 + 5 * 5)'>
	for the line '4 + (3 + 9 * 2 + 5 * 5)'
	'''
	inside_brackets = brackets_regex.search(tokens)
	if not inside_brackets:
		return inner_eval(tokens)

	inside_brackets = inside_brackets.group(1)
	brackets_result = inner_eval(inside_brackets.strip('()'))
	new_tokens = tokens.replace(inside_brackets, str(brackets_result))
	return evaluate(new_tokens, inner_eval)

def solve_first(lines):
	return sum(evaluate(line, equal_precedence) for line in lines)

def solve_second(lines):
	return sum(evaluate(line, add_before) for line in lines)

print(f"1. {solve_first(lines)}")
print(f"2. {solve_second(lines)}")
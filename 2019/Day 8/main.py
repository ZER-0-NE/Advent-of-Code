WIDTH = 25
HEIGHT = 6

def chunks(xs, size):
	return [xs[i:i+size] for i in range(0, len(xs), size)]

with open('data.txt', 'r') as f:
	digits = [int(c) for c in f.read().rstrip()]
	layers = chunks(digits, WIDTH*HEIGHT)

def part1(layers):
	least_zeroes = min(layers, key=lambda layer: layer.count(0))
	return least_zeroes.count(1) * least_zeroes.count(2)

print(f"1. {part1(layers)}")

def part2(layers):
	merged = (next(n for n in stack if n!=2) for stack in zip(*layers))
	rendered = ''.join(' ' if n == 0 else '#' for n in merged)
	return '\n'.join(chunks(rendered, WIDTH))

print(f"2. \n {part2(layers)}")
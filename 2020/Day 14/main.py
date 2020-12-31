lines = open('data.txt', 'r').read().splitlines()
instructions = [line.replace('mem', '').replace('[','').replace(']', '').split(' = ') for line in lines]

def part1(instructions):
	set0mask, set1mask, mem = 0, 0, {}
	for instruction, value in instructions:
		if instruction == 'mask':
			set0mask, set1mask = int(value.replace('X', '1'),2), int(value.replace('X', '0'),2)
		else:
			address, value = int(instruction), int(value)
			mem[address] = value & set0mask | set1mask
	return sum(mem.values())

print(f"1. {part1(instructions)}")
with open("data.txt", 'r') as file:
	lines = [lines.replace('\n', ' ') for lines in file.read().strip().split('\n\n')]

# print(lines)

passports = []

passports = [{key: value for word in line.split() for key, value in [word.split(':')]} for line in lines]

mandatory = ['byr', 'pid', 'eyr', 'iyr', 'hgt', 'hcl', 'ecl']

valid_passports = []

for passport in passports:
	keys = list(passport.keys())
	if 'cid' in keys:
		keys.remove('cid')

	if set(keys) == set(mandatory):
		valid_passports.append(passport)

print(len(valid_passports))
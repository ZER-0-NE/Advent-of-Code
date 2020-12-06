with open("data.txt", 'r') as file:
	lines = [lines.replace('\n', ' ') for lines in file.read().strip().split('\n\n')]

# print(lines)
# part 1

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

# Part 2

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

import re

valids = 0
keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

for line in lines:
	if all(key + ":" in line for key in keys):
		passport = {key:value for part in line.split(" ") for key,value in [part.split(":")]}
		# print(passport)
		if (
			int(passport['byr']) >= 1920 and int(passport['byr']) <=2002 and
			int(passport['iyr']) >= 2010 and int(passport['iyr']) <=2020 and
			int(passport['eyr']) >= 2020 and int(passport['eyr']) <=2030 and
			re.match("^(1([5-8][0-9]|9[0-3])cm|(59|[6][0-9]|[7][0-6])in)$", passport['hgt']) and
			re.match("#[0-9a-f]{6}", passport['hcl']) and
			re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", passport['ecl']) and
			re.match("^\d{9}$", passport['pid'])
			):
			valids+=1

print(valids)

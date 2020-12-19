# inspired from om_henners on reddit!

import numpy as np
import parse

# 1 @ 7,589: 24x11

claim_matcher = '''#{id:d} @ {x:d},{y:d}: {width:d}x{height:d}\n'''

fabric = np.zeros((1000, 1000), dtype=np.int)

for line in open('data.txt'):
	r = parse.parse(claim_matcher, line)
	claim = fabric[r['y']:r['y'] + r['height'], r['x']:r['x']+r['width']]
	claim[:] = claim+1
	# print(claim)

print(f"1. {np.sum(np.where(fabric>1,1,0))}")

for line in open('data.txt'):
	r = parse.parse(claim_matcher, line)
	claim = fabric[r['y']:r['y'] + r['height'], r['x']:r['x']+r['width']]
	if claim.max() == 1:
		print(f"2. {r['id']}")


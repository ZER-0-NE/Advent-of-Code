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


# SO answer:
# import numpy as np

# A = np.zeros((100, 100))
# B = np.zeros((100, 100))

# A[rect1.top : rect1.bottom,  rect1.left : rect1.right] = 1
# B[rect2.top : rect2.bottom,  rect2.left : rect2.right] = 1

# area_of_union     = np.sum((A + B) > 0)
# area_of_intersect = np.sum((A + B) > 1)

# In this example, we create two zero-matrices that are the size of the canvas. For each rectangle, 
# fill one of these matrices with ones where the rectangle takes up space. Then sum the matrices. 
# Now sum(A+B > 0) is the area of the union, and sum(A+B > 1) is the area of the overlap. 
# This example can easily generalize to multiple rectangles.


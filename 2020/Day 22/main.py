from collections import deque

with open('data.txt', 'r') as f:
	player1, player2 = f.read().split('\n\n')

q1, q2 = deque(map(int, player1.split('\n')[1:])), deque(map(int, player2.split('\n')[1:]))

while q1 and q2:
	if q1[0]>q2[0]:
		q1.append(q1.popleft())
		q1.append(q2.popleft())
	else:
		q2.append(q2.popleft())
		q2.append(q1.popleft())

res = 0

while q1:
	res += len(q1) * q1.popleft()
while q2:
	res += len(q2) * q2.popleft()

print(f"1. {res}")
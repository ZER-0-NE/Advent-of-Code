# part 1
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

# another sol for part 1 

# Deck = deque[int]

with open('data.txt') as file:
	player_input = file.read().strip().split('\n\n')

decks = [deque(map(int, player.split('\n')[1:])) for player in player_input]

round_number = 0
winner, loser = 0, 0

# print(decks)

while all(decks):
	round_number += 1
	drawn_cards = [deck.popleft() for deck in decks]
	# print(f"Round {round_number}: cards: {drawn_cards}, decks: {decks}")
	winner, loser = (0, 1) if drawn_cards[0]>drawn_cards[1] else (1, 0)
	for i in winner, loser:
		decks[winner].append(drawn_cards[i])
print(f"1. Player {winner+1} wins")
print(sum([(i + 1) * card for i, card in enumerate(reversed(decks[winner]))]))


# another sol for part 1 and 2

player1_line, player2_line = open('data.txt').read().replace('\r\n', '\n').replace('\n\n', '|').replace('\n', ' ').split('|')

player1 = list(map(int, player1_line.split(':')[1].split()))
player2 = list(map(int, player2_line.split(':')[1].split()))

def multiply(player):
	score, multiplier = 0, 1
	while player:
		score += multiplier * player.pop()
		multiplier += 1
	return score

def part1(player1, player2):
	player1, player2 = player1[:], player2[:]
	while player1 and player2:
		player1_top, player2_top = player1.pop(0), player2.pop(0)
		player1 += [player1_top, player2_top] if player1_top>player2_top else []
		player2 += [player2_top, player1_top] if player2_top>player1_top else []
	return player1 if player1 else player2

winner1 = part1(player1, player2)
print(f"1. {multiply(winner1)}")

def part2(player1, player2):
	states = set()
	while player1 and player2:
	    state = (tuple(player1), tuple(player2))
	    if state in states:
	        return (1, player1)

	    player1_top, player2_top = player1.pop(0), player2.pop(0)

	    if player1_top <= len(player1) and player2_top <= len(player2):
	        winner, _ = part2(player1[:player1_top], player2[:player2_top])
	    else:                
	        winner = 1 if player1_top > player2_top else 2

	    player1 += [player1_top, player2_top] if winner == 1 else []
	    player2 += [player2_top, player1_top] if winner == 2 else []
	    states.add(state)

	return (1, player1) if player1 else (2, player2)

_, winner2 = part2(player1, player2)
print(f"2. {multiply(winner2)}")
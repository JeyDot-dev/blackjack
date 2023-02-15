import art
import random
from time import sleep
from os import system
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
signs = ['♠', '♥', '♦', '♣']
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
high_value_cards = ['10', 'J', 'Q', 'K']
def clear():
	system('clear')

p_hand = {}
d_hand	= {}
p_score = 0
d_score = 0


def draw_card(nb, player):
	value = 0
	sign = ''
	number = ''
	for _ in range(nb) :
		value = random.choice(cards)
		if value == 11 :
			number = 'A'
		elif value == 10 :
			number = random.choice(high_value_cards)
		else :
			number = str(value)
		sign = random.choice(signs)
		player[len(player) + 1] = [value, number, sign]

def total_score(cards) :
	total = 0
	for n in cards :
		total += cards[n][0]
	return total

def ace_to_one(cards) :
	score = total_score(cards)
	for a in cards:
		if score > 21 and cards[a][0] == 11:
			score -= 10
			cards[a][0] = 1
def	print_hand(hand) :
	for card in hand :
		sleep(0.5)
		art.print_card(hand[card][1], hand[card][2])

def	current_game (p_score, p_hand, d_score, d_hand) :
	clear()
	print("\t\t\t\t")
	print_hand(d_hand)
	print(f"Dealer has {d_score}.")
	print("\n\n\n\n\n")
	print_hand(p_hand)
	print(f"\t\t\t\tYou have {p_score}")

print(art.logo)
play = input("Would you like to play a round of blackjack ? y or n : ")


while play == 'y' :
	draw_card(1, p_hand)
	draw = 'x'
	draw_card(1, d_hand)
	d_score = total_score(d_hand)
	while draw != 'n' :
		draw_card(1, p_hand)
		if draw == 'x' and total_score(p_hand) == 21 :
			break
		ace_to_one(p_hand)
		p_score = total_score(p_hand)
		current_game(p_score, p_hand, d_score, d_hand)
		if p_score > 21 :
			break

		draw = input("Would you like to draw a card ? y or n : ")
		if draw != 'n' and draw != 'y':
			draw = 'n'
	if draw == 'x' :
		current_game(p_score, p_hand, d_score, d_hand)
		input("Wow ! Blackjack, well played ! (press any key) ")
	elif p_score <= 21 :
		while d_score < p_score and d_score < 21 :
			draw_card(1, d_hand)
			ace_to_one(d_hand)
			d_score = total_score(d_hand)
			current_game(p_score, p_hand, d_score, d_hand)
	if p_score > 21 or (d_score <= 21 and d_score > p_score) :
		input("Yikes you lost :(.. (press any key)")
	elif draw != 'x' and (d_score > 21 or p_score > d_score) :
		input("Congrats ! You won ! (press any key)")
	elif draw != 'x':
		input("It's a draw ! (press any key)")
	play = input("Would you like to play a round of blackjack ? y or n : ")

	if play != 'n' and play != 'y':
		play = 'n'
	p_hand.clear()
	d_hand.clear()
	clear()

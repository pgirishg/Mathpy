import random

#Probability of getting a head in a coin toss
coin_toss = random.choice(['Head', 'Tail'])
print(f"coin toss: {coin_toss}")

#Probability of rollin specific number on a die
die_roll = random.randint(1,6)
print(f"die roll: {die_roll}")

#simulateing multiple coin tosses   
tosses = [random.choice(['Head', 'Tail']) for _ in range(1000)]
heads=tosses.count('Head')
tails=tosses.count('Tail')
print(f"Heads: {heads}  Tails: {tails}")

#probability of drawing specific card from a deck of cards
deck = [f"{rank} of {suit}" for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades'] for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']]
card = random.choice(deck)
print(f"Card: {card}")

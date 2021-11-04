import random

values = ["Ace", '2', '3', '4', '5', '6', '7', '8', '9', '10', "Jack", "Queen", "King"]
suits = ["Spades", "Clubs", "Diamonds", "Hearts"]

class Card:
    def __init__(self):
        self.value = random.choice(list(values))
        self.suit = random.choice(list(suits))

    def display(self):
        print(self.value + " of " + self.suit)
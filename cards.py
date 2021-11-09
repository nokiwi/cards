import random

values = ["Ace", '2', '3', '4', '5', '6', '7', '8', '9', '10', "Jack", "Queen", "King"]
suits = ["Spades", "Clubs", "Diamonds", "Hearts"]

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def generateRandom(self):
        self.value = random.choice(list(values))
        self.suit = random.choice(list(suits))

    def display(self):
        print(f"{self.value} of {self.suit}")


class Deck:
    def __init__(self):
        self.cards = []
        self.buildDeck()
    
    def buildDeck(self):
        for suit in suits:
            for value in range(0, 13):
                self.cards.append(Card(suit, values[value]))

    def display(self):
        for card in self.cards:
            card.display()

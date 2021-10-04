import random
import seaborn as sns

"""
1. Write a for loop that produces a Python list called unshuffled_deck that represents a 52-card deck.
A standard 52-card deck consists of numbers from 2 to 10 as well as a jack, a queen, a king, and an ace in 4 different suits: clubs, diamonds, hearts, and spades. In our deck, we will assume that there is no difference between suits due to their impotency in the game.
Represent each card in the list with a numerical value as follows:
- Assign their own value for the cards from 2 to 10.
- Assign 10 for each jack, queen, and king.
- Assign 11 for each ace as an initial value. In the game, aces can have a value of 1 or 11, and we will account for their different possible values in a later milestone.
As a result, the list should include 52 numerical elements.
"""

class Card():
    def __init__(self, suit, label):
        self.suit = suit
        self.label = label
        if label in list(['jack', 'queen', 'king']):
            self.value = 10
        elif label in list(['ace', '1']) :
            self.value = 11
            self.label = 'ace'
        else:
            self.value = int(label)

    def __str__(self):
        return "Card(label={}, suit={}, value={})".format(self.label, self.suit, self.value)

    def __repr__(self):
        return str(self)

def unshuffled_deck():
    deck = []
    for suit in list(['club', 'diamond', 'heart', 'spade']):
        for label in (list(map(lambda x: str(x), list(range(1, 11)))) + ['jack', 'queen', 'king']):
            deck.append(Card(suit, label))
    random.shuffle(deck)
    return deck

"""
2. Visualize the histogram of the list of the deck.
Plot a chart that shows the histogram of the values in the list.
"""
deck = unshuffled_deck()
sns.histplot(data=list(map(lambda card: card.value, deck)))

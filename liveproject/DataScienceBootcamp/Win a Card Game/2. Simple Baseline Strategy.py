import random
from tqdm import tqdm
random.seed(0)
import seaborn as sns

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


class Deck():
    def __init__(self):
        self.deck = unshuffled_deck()
        self.index = -1
    
    def hit(self):
        self.index += 1
        return self.deck[self.index]  

class Hand():
    def __init__(self):
        self.cards = []

    def append(self, card):
        self.cards.append(card)

    def alter(self):
        for card in self.cards:
            if card.value == 11:
                card.value = 1
                break
    
    def has_ace(self):
        for card in self.cards:
            if card.value == 11:
                return True
        return False
    
    def value(self):
        return sum(list(map(lambda card: card.value, self.cards)))
    
    def __repr__(self):
        return str(self.cards)
      
hands = []

for i in tqdm(range(100000)):
    deck = Deck()
    hand = Hand()

    hand.append(deck.hit())
    hand.append(deck.hit())

    while hand.value() < 22 or hand.has_ace():
        if hand.value() >= 22:
            hand.alter()
        while hand.value() <= 16:
            hand.append(deck.hit())
        if hand.value() < 22:
            break

    hands.append(hand.value())

sns.histplot(data=hands)

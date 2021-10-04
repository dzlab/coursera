import random
from collections import Counter
from tqdm import tqdm
random.seed(0)

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
      
      
def simulate_game(deck, threshold):
    hand = Hand()

    hand.append(deck.hit())
    hand.append(deck.hit())

    while hand.value() < 22 or hand.has_ace():
        if hand.value() >= 22:
            hand.alter()
        while hand.value() <= threshold:
            hand.append(deck.hit())
        if hand.value() < 22:
            break
    return hand

def winner(value1, value2, threshold1, threshold2):
    if value1 > value2:
        return threshold1
    elif value2 > value1:
        return threshold2
    else:
        return 0

def duel_play(threshold1, threshold2):
    deck = Deck()
    hand1 = simulate_game(deck, threshold1)
    hand2 = simulate_game(deck, threshold2)
    value1 = hand1.value()
    value2 = hand2.value()
    if value1 == value2:
        return 0
    if value1 < 22 and value2 < 22:
        return winner(value1, value2, threshold1, threshold2)
    elif value1 > 22 and value2 > 22:
        return winner(value2, value1, threshold2, threshold1)
    elif value1 > 22:
        return threshold2
    else:
        return threshold1

frequency_wins = []

t1 = 15
for i in tqdm(range(10000)):
    winners = []
    for j in range(1000):
        t2 = random.choice([13, 14, 16, 17])
        winners.append(duel_play(t1, t2))
    freqs = Counter(winners)
    win_rate = (1.0 * freqs[t1]) / (1000.0 - freqs[0])
    frequency_wins.append(win_rate)
        
      
import seaborn as sns
sns.histplot(data=frequency_wins)

from scipy import stats
import numpy as np

stats.norm.interval(0.95, loc=np.mean(frequency_wins), scale=np.std(frequency_wins))

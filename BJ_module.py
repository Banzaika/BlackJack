class Card(object):
    SUITS = ['c', 'd', 'h', 's']
    RANKS = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']

    def __init__(self, suit, rank, face_up=True):
        self.face_up = face_up
        self.suit = suit
        self.rank = rank

    def flip(self):
        self.face_up = not self.face_up

    def __str__(self):
        if self.face_up:
            rep = self.rank + self.suit
            return rep
        else:
            return 'XX'

class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + '\t'
            return rep
        else:
            return "<пусто>"
    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give_card(self, other_hand, card):
        other_hand.add(card)
        self.cards.remove(card)

class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card(rank, suit)
                self.cards.add(card)
    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        #type(hands) == list
        for round in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give_card(hand, top_card)
                else:
                    print('Нет могу больше раздавать, карты закончились!')
class Player(Hand):
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    def __str__(self):
        return self.name + ':/t' + str(self.scores)

if __name__ == '__main__':
    print('Вы запустили модуль для BJ')
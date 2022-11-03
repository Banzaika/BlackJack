from BJ_module import *
from games import *

class BJ_Card(Card):
    ACE_VALUE = 1

    @property
    def value(self):
        #Если карта лежит рубашкой вверх, то вернется None
        if self.face_up:
            value = BJ_Card.RANKS.index(self.rank) + 1
            if value > 10:
                value = 10
            return value


class BJ_Deck(Deck):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(BJ_Card(suit, rank))


class BJ_Hand(Hand):
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += '(' + str(self.total) + ')'
        return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        t = 0
        contains_ace = False
        for card in self.cards:
            t += card.value
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        if contains_ace and t < 12:
            t += 10
        return t

    def is_busted(self):
        return self.total > 21

class Player(BJ_Hand):
    def is_hitting(self):
        response = ask_yes_no(f'{self.name}, xотите взять еще одну карту? (Y/N): ')
        return response == 'y'
    def bust(self):
        print(self.name, 'перебрал.')

    def win(self):
        print(self.name, 'выиграл.')

    def lose(self):
        print(self.name, 'проиграл.')

    def push(self):
        print(self.name, 'сыграл с компьютером вничью.')

class Dealer(BJ_Hand):
    def is_hitting(self):
        return self.total < 17
    def bust(self):
        print(self.name, 'перебрал')

    def lose(self):
        print(self.name, 'проиграл')

    def flip_first_card(self):
        self.cards[0].flip()


class BJ_Game(object):
    def __init__(self, names):
        self.players = []
        for name in names:
            player = Player(name)
            self.players.append(player)
        self.dealer = Dealer('Диллер')
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __adittional_cards(self, player):
        while player.is_hitting() and not player.is_busted():
            self.deck.deal(per_hand=1, hands = [player])
            print(player)
            if player.is_busted():
                player.bust()
                player.lose()
                break

    def play(self):
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)

        for player in self.players:
            self.__adittional_cards(player)

        self.dealer.flip_first_card()

        if not self.still_playing:
            print(self.dealer)

        else:
            print(self.dealer)
            self.__adittional_cards(self.dealer)
            if self.dealer.is_busted():
                for player in self.still_playing:
                    player.win()
            else:
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        for player in self.players:
            player.clear()
        self.dealer.clear()

def main():
    names = []
    player_count = ask_number('Сколько всего игроков?(1-8): ', 1, 8)
    for i in range(player_count):
        name = input('Введите имя игрока: ')
        names.append(name)
        print()
    game = BJ_Game(names)
    again = None
    while again != 'n':
        game.play()
        again = ask_yes_no('Хотите сыграть ещё? (n/y): ')
        print('\n\n\n')
main()
input('Введите Enter, чтобы выйти.')




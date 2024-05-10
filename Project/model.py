import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]  # Define suit names here

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        if self.rank == 1:
            self_rank = 14
        else:
            self_rank = self.rank

        if other.rank == 1:
            other_rank = 14
        else:
            other_rank = other.rank

        return self_rank < other_rank

    def __str__(self):
        rank_names = ["", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        suit_symbols = {"Clubs": "♣", "Diamonds": "♦", "Hearts": "♥", "Spades": "♠"}
        return f"{rank_names[self.rank]} {suit_symbols[self.suit_names[self.suit]]}"

class CardDeck:
    def __init__(self):
        self.deck = []
        self.fill()

    def fill(self):
        for suit in range(4):
            for rank in range(1, 14):
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if len(self.deck) == 0:
            return None
        return self.deck.pop()

    def get_size(self):
        return len(self.deck)

class Player:
    def __init__(self, name):
        self.name = name
        self.play_pile = Pile()
        self.won_pile = Pile()
        self.fill_play_pile()

    def fill_play_pile(self):
        deck = CardDeck()
        deck.shuffle()
        for _ in range(26):  # Each player starts with 26 cards
            card = deck.deal()
            self.play_pile.add_card(card)

    def play_card(self):
        if self.play_pile.get_size() == 0:
            self.use_won_pile()

        if self.play_pile.get_size() > 0:
            return self.play_pile.next_card()
        return None

    def collect_card(self, card):
        self.won_pile.add_card(card)

    def collect_cards(self, pile):
        self.won_pile.add_cards(pile)

    def use_won_pile(self):
        self.play_pile.clear()
        self.play_pile.add_cards(self.won_pile)
        self.won_pile.clear()

    def num_cards(self):
        return self.play_pile.get_size() + self.won_pile.get_size()

    def get_name(self):
        return self.name

class Pile:
    def __init__(self):
        self.pile = []
        self.front = 0
        self.end = 0

    def get_size(self):
        return self.end - self.front

    def clear(self):
        self.front = 0
        self.end = 0

    def add_card(self, card):
        self.pile.append(card)
        self.end += 1

    def add_cards(self, pile):
        while pile.get_size() > 0:
            self.add_card(pile.next_card())

    def next_card(self):
        if self.front == self.end:
            return None
        card = self.pile[self.front]
        self.front += 1
        return card

class Game:
    def __init__(self):
        self.p1 = Player("Ernie")
        self.p2 = Player("Burt")
        self.turn_count = 1  # Initialize turn count to 1

    def reset(self):
        self.turn_count = 1
        self.p1 = Player("Ernie")
        self.p2 = Player("Burt")

    def play(self):
        cd = CardDeck()
        cd.shuffle()

        while cd.get_size() >= 2 and self.turn_count <= 52:  # Limit to 52 turns
            self.p1.collect_card(cd.deal())
            self.p2.collect_card(cd.deal())

        self.p1.use_won_pile()
        self.p2.use_won_pile()

        down = Pile()  # Pile for cards in a war

        for t in range(1, 101):
            if not self.enough_cards(1):
                break
            c1 = self.p1.play_card()
            c2 = self.p2.play_card()

            if c1 < c2:
                self.p2.collect_card(c1)
                self.p2.collect_card(c2)
            elif c1 > c2:
                self.p1.collect_card(c1)
                self.p1.collect_card(c2)
            else:  # War
                down.clear()
                down.add_card(c1)
                down.add_card(c2)

                done = False
                while not done:
                    num = min(self.p1.num_cards(), self.p2.num_cards(), 4)  # Ensure there are enough cards for a war
                    if num < 4:
                        break
                    for _ in range(num):
                        c1 = self.p1.play_card()
                        c2 = self.p2.play_card()
                        down.add_card(c1)
                        down.add_card(c2)
                    if c1 < c2:
                        self.p2.collect_cards(down)
                        done = True
                    elif c1 > c2:
                        self.p1.collect_cards(down)
                        done = True

            self.turn_count += 1

    def enough_cards(self, n):
        return self.p1.num_cards() >= n and self.p2.num_cards() >= n

    def get_winner(self):
        if self.p1.num_cards() > self.p2.num_cards():
            return self.p1
        elif self.p2.num_cards() > self.p1.num_cards():
            return self.p2
        else:
            return None
      
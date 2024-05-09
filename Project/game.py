class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

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
        suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
        return f"{rank_names[self.rank]} of {suit_names[self.suit]}"

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

class Game:
    def __init__(self):
        self.p1 = None
        self.p2 = None

    def play(self):
        cd = CardDeck()
        cd.shuffle()
        self.p1 = Player("Ernie")
        self.p2 = Player("Burt")

        while cd.get_size() >= 2:
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

            print("\nTurn", t, ": ")
            print(self.p1.get_name() + ": " + str(c1) + " ", end="")
            print(self.p2.get_name() + ": " + str(c2) + " ", end="")

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
                    num = c1.get_rank()
                    if not self.enough_cards(num):
                        break
                    print("\nWar! Players put down", num, "card(s).")
                    for _ in range(num):
                        c1 = self.p1.play_card()
                        c2 = self.p2.play_card()
                        down.add_card(c1)
                        down.add_card(c2)
                        print(self.p1.get_name() + ": " + str(c1) + " ", end="")
                        print(self.p2.get_name() + ": " + str(c2) + " ", end="")
                    if c1 < c2:
                        self.p2.collect_cards(down)
                        done = True
                    elif c1 > c2:
                        self.p1.collect_cards(down)
                        done = True

        print(self.p1.num_cards(), "to", self.p2.num_cards())

    def enough_cards(self, n):
        return self.p1.num_cards() >= n and self.p2.num_cards() >= n

    def get_winner(self):
        if self.p1.num_cards() > self.p2.num_cards():
            return self.p1
        elif self.p2.num_cards() > self.p1.num_cards():
            return self.p2
        else:
            return None

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

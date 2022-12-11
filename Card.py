class Card:

    # Ranks are 1-13
    # Ace is 1
    # Jack, Queen, King is 11, 12, 13

    # Suits are 1-4
    # Club Diamond Heart Spade

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        suit = ''
        if (self.suit == 1):
            suit = 'Club'
        elif (self.suit == 2):
            suit = 'Diamond'
        elif (self.suit == 3):
            suit = 'Heart'
        elif (self.suit == 4):
            suit = 'Spade'
        return f"{self.rank} of {suit}s"

    def __eq__(self, other):
        return ((self.rank == other.rank) and (self.suit == other.suit))
    
    def __repr__(self):
        return str(self)
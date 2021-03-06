import random


class Deck:
    """
    The responsibility of Deck is to draw a random number from 1 to 13. 

    Attributes:
        
    """

    def __init__(self):
        """Constructs a new instance of Deck.

        Args:
            self (Die): An instance of Die.
        """
        self.first_card = random.randint(1,13)
        self.cards = [] 
        self.cards.append(self.first_card)
        self.current_card = self.cards[-1]

        
        

    def draw(self):
        """
        Gets a new card for our game. 

        Args:
            self (Deck): An instance of Die.
        """

        self.current_card = random.randint(1, 13)

        # make sure to discard number if the same as previous and redraw
        while self.current_card == self.cards[-1]:
            self.current_card = random.randint(1,13)
        
        # add the current card to the list of cards
        self.cards.append(self.current_card)

        

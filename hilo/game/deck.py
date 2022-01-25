import random


class Deck:
    """

    The responsibility of Deck is to draw a random number from 1 to 13. 

    Attributes:
        
    """

    def __init__(self):
        """Constructs a new instance of Deck with a value and points attribute.

        Args:
            self (Die): An instance of Die.
        """
        self.first_card = random.randint(1,13)
        self.cards = [] 
        self.current_card = None
        #self.score = 0

        self.cards.append(self.first_card)
        

    def draw(self):
        """

        Args:
            self (Deck): An instance of Die.
        """

        self.current_card = random.randint(1, 13)
        # make sure to discard number if the same as previous and redraw

        self.cards.append(self.current_card)

        print(self.cards[-1])

    def cards_list(self):
        pass


    # def score(self):
    #     '''
    #     If card was higher add 100 points 

    #     Args:
    #         self (Die): An instance of Deck
    #     '''
    #     if self.cards[-2] > self.cards[-1]:
    #         self.points + 100
    #     else:
    #         self.points - 75
        

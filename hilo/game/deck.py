import random


# TODO: Implement the Die class as follows...


# 1) Add the class declaration. Use the following class comment.

class Deck:
    """

    The responsibility of Deck is to ...

    Attributes:
        
    """


# 2) Create the class constructor. Use the following method comment.

    def __init__(self):
        """Constructs a new instance of Deck with a value and points attribute.

        Args:
            self (Die): An instance of Die.
        """

        self.value = 0
        self.points = 0

# 3) Create the roll(self) method. Use the following method comment.

    def roll(self):
        """
        
        Args:
            self (Die): An instance of Die.
        """

        self.value = random.randint(1, 6)
        if self.value == 1:
            self.points = 100
        elif self.value == 5:
            self.points = 50
        else:
            self.points = 0

        return self.points

from game.deck import Deck


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:

        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        self.is_playing = True
        #self.score = 0
        self.total_score = 300

        self.deck = Deck()

        

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        #deck = Deck()

        while self.is_playing == True:
            #self.get_inputs(self.deck)
            print(f'The card is: {self.deck.current_card}')
            choice = self.get_inputs()
            # self.do_updates(choice, self.total_score, self.deck.cards)
            self.do_updates(choice, self.deck.cards)
            self.do_outputs()

        


    def get_inputs(self):
        """Display the current card and Ask the user if they want to go higher or lower.

        Args:
            self (Director): An instance of Director.
        """

        self.choice = input("Higher or lower [h/l] ")

        #self.is_playing == self.game_status

        return self.choice

    #def do_updates(self, choice, cards):
    def do_updates(self, choice, cards):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        self.deck.draw()

        print(f'Next card is: {self.deck.cards[-1]}')

        if choice == 'h' and cards[-2] < cards[-1]:
            self.total_score += 1 * 100
        elif choice == 'h' and cards[-2] > cards[-1]:
            self.total_score -= 1 * 75
        elif choice == 'l' and cards[-2] > cards[-1]:
            self.total_score += 1 * 100
        elif choice == 'l' and cards[-2] < cards[-1]:
            self.total_score -= 1 * 75        

        print(f'Your score is: {self.total_score}')

        #self.is_playing == game_status

        

    def do_outputs(self):
        """Displays the previous card, option to play 

        Args:
            self (Director): An instance of Director.
        """

        game_status = input('Play again? [y/n] ')
        if game_status == 'n':
            self.is_playing == False
        else: 
            self.is_playing == True

        # return self.is_playing == (input('Play again? [y/n] '))
        

        
        
        # print the previous card
        # show the option to play
        # show the next card 
        # show their score

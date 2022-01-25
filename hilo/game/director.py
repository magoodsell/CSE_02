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

        self.is_playing = 'y'
        #self.score = 0
        self.total_score = 300

        

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing == 'y':
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        


    def get_inputs(self):
        """Ask the user if they want to go higher or lower.

        Args:
            self (Director): An instance of Director.
        """
        # print(f'The Card is: {Deck.cards[-1]}') 
        print(f'The Card is: {Deck.draw(self)}') 

        self.choice = input("Higher or lower [h/l] ")

        self.game_status = input('Play again? [y/n] ')

        return self.choice, self.game_status

    def do_updates(self, game_status):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        current_score = Deck.score()

        print(f'Next card is: {Deck.cards[-1]}')

        print(f'Your score is: {current_score}')

        self.is_playing == game_status

        return self.total_score + current_score
        

    def do_outputs(self, total_score):
        """Displays the previous card, option to play 

        Args:
            self (Director): An instance of Director.
        """
        current_card = Deck.draw(self)


        print(f'Next card is: {current_card}')
        print(f'Your score is: {total_score}')

        
        # print the previous card
        # show the option to play
        # show the next card 
        # show their score

    def score(self, choice, total_score):
        '''
        If card was higher add 100 points 

        Args:
            self (Die): An instance of Deck
        '''

        if choice == 'h' & self.cards[-2] < self.cards[-1]:
            total_score + 100
        elif choice == 'h' & self.cards[-2] > self.cards[-1]:
            total_score - 75
        elif choice == 'l' & self.cards[-2] > self.cards[-1]:
            total_score + 100
        elif choice == 'l' & self.cards[-2] < self.cards[-1]:
            total_score - 75

        return total_score

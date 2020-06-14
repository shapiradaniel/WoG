# GuessGame.py

from Game import Game
import random


# Will prompt the user for a number between 1 to difficulty and return the number
def get_guess_from_user(difficulty):
    while True:
        user_guess = input("Please enter number between 1 - %d : " % difficulty)
        if not user_guess.isdigit():
            print("You enter wrong guess answer type (%s)" % user_guess)
            continue
        return int(user_guess)


# Game class
class GuessGame(Game):
    secret_number = 0

    # Will generate number between 1 to difficulty and save it
    def generate_number(self, difficulty):
        self.secret_number = random.randint(1, difficulty)

    # Will compare the the secret generated number to the one prompted
    def compare_results(self, guess_num):
        print("The number was : %d" % self.secret_number)
        return self.secret_number == guess_num

    # Play the game
    def play(self, difficulty):
        self.generate_number(difficulty)
        return self.compare_results(get_guess_from_user(difficulty))

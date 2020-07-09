# Live.py

from MemoryGame import MemoryGame
from GuessGame import GuessGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Score import add_score

# CONST definitions
GAME_LIST = (
                {
                    "name": MemoryGame,
                    "desc": "Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back"
                },
                {
                    "name": GuessGame,
                    "desc": "Guess Game - guess a number and see if you chose like the computer"
                },
                {
                    "name": CurrencyRouletteGame,
                    "desc": "Currency Roulette - try and guess the value of a random amount of USD in ILS"
                }
            )
MIN_DIFFICULTY = 1
MAX_DIFFICULTY = 5


# Check if number in valid range
def check_number_validity(numb, min_num, max_num):
    if not max_num >= numb >= min_num:
        return False
    return True


# Print game list
def print_game_list():
    game_id = 0
    for game_name in GAME_LIST:
        game_id += 1
        print("%d. %s" % (game_id, game_name["desc"]))
    return game_id


# Function show game menu and return the chosen game number
def get_game_number():
    while True:
        game_number = input("Make your choice : ")
        if not game_number.isdigit() or not check_number_validity(int(game_number), 1, len(GAME_LIST)):
            print("You chose non existing game (%s)" % game_number)
            continue
        return int(game_number)


# Function return chosen game difficulty
def get_game_difficulty():
    while True:
        game_difficulty = input("Please choose game difficulty from 1 to 5 : ")
        if not game_difficulty.isdigit() or not check_number_validity(int(game_difficulty), MIN_DIFFICULTY, MAX_DIFFICULTY):
            print("You chose non existing game difficulty (%s)" % game_difficulty)
            continue
        return int(game_difficulty)


# Welcome notice
def welcome(name):
    return "Hello %s and welcome to the World of Games (WoG).\nHere you can find many cool games to play." % name


# Load the game
def load_game():
    print_game_list()
    game_number = get_game_number()
    game_difficulty = get_game_difficulty()
    game = GAME_LIST[game_number-1]["name"]()
    if game.play(game_difficulty):
        print("You WIN")
        add_score(game_difficulty)
    else:
        print("You LOSE")

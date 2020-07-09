# MainGame.py

from Live import load_game, welcome
from Utils import screen_cleaner
from MainScores import score_server


gamer_name = str(input("Please enter your name: "))
screen_cleaner()
print(welcome(gamer_name))
load_game()
score_server()

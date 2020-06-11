# MainGame.py

from Live import load_game, welcome
import os


gamer_name = str(input("Please enter your name: "))
os.system("CLS")
print(welcome(gamer_name))
load_game()

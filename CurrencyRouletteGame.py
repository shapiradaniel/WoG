# CurrencyRouletteGame.py

import random
import currency_converter


# Game class
class CurrencyRouletteGame:
    usd_value = 0
    ils_value = 0

    # Constructor
    def __init__(self):
        self.usd_value = random.randint(1, 101)

    # Get the current currency rate from USD to ILS interval
    def get_money_interval(self, difficulty):
        currency = currency_converter.CurrencyConverter()
        self.ils_value = currency.convert(self.usd_value, "USD", "ILS")
        return self.ils_value-(5-difficulty), self.ils_value+(5-difficulty)

    # Prompt a guess from the user
    def get_guess_from_user(self):
        while True:
            user_ils_guess = input("What should be ILS value for %dUSD? " % self.usd_value)
            if not user_ils_guess.isdigit():
                print("You enter wrong guess answer type (%s)" % user_ils_guess)
                continue
            return int(user_ils_guess)

    # Play the game
    def play(self, difficulty):
        gamer_ils_value = self.get_guess_from_user()
        lower_interval, upper_interval = self.get_money_interval(difficulty)
        print(f"The {self.usd_value}USD is {self.ils_value:.2f}ILS")
        return upper_interval >= gamer_ils_value >= lower_interval

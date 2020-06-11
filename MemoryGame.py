# MemoryGame.py

import random
import time
import os


# Will return a list of numbers prompted from the user
def get_list_from_user(list_size):
    user_list = []
    print("Please enter numbers followed by Enter key...")
    for counter in range(1, list_size+1):
        while True:
            guess_number = input("%d. : " % counter)
            if not guess_number.isdigit():
                print("You enter wrong guess answer type (%s)" % guess_number)
                continue
            user_list.append(int(guess_number))
            break
    return user_list


# Compare two lists if they are equal
def is_list_equal(l1, l2):
    print("The numbers was : %s" % l1)
    return l1.sort() == l2.sort()


# Game class
class MemoryGame:
    numbers_list = []

    # Generate a list of random numbers between 1 to 101
    def generate_sequence(self, list_size):
        for counter in range(list_size):
            self.numbers_list.append(random.randint(1, 101))
        return self.numbers_list

    # Play the game
    def play(self, difficulty):
        self.generate_sequence(difficulty)
        print(self.numbers_list)
        time.sleep(0.7)
        os.system("CLS")
        return is_list_equal(self.numbers_list, get_list_from_user(difficulty))

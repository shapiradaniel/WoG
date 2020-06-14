# Game.py

from abc import ABC, abstractmethod


# Abstract class
class Game(ABC):
    # Abstract method
    @abstractmethod
    def play(self, difficulty):
        pass

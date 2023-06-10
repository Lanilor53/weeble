import requests
from game import Game

_game = Game() # todo: make this work with multiple servers

class Command:

    # start game
    @classmethod
    def weeble(cls):
        global _game
        result = _game.start_game()
        return result
    
    @classmethod
    def guess(cls, msg):
        global _game
        result = _game.guess(msg)
        return result
    
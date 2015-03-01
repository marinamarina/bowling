from sys import argv
from .player import Player

prompt = '> '

class Bowling(object):

    def __init__(self, game):
        self.game = game
        self.players = []

    def add_player(self, name):
        p = Player(name)
        self.players.append(p)
        print "Player " + name + " added!"

    def play(self):
        # making sure input works for Python 3 (converting to raw_input)
        try:
            input = raw_input
        except NameError:
            pass

        while True:
            i = input("Enter player's name (or press Enter to quit): " + prompt)
            if not i:
                break
            self.add_player(i)
        print("---------------------------------------------------------------" )
        print("Let's start the game!")

    def __repr__(self):
        return '<Bowling> players {}'.format(
            self.players
        )

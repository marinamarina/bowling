from sys import argv
from .player import Player

prompt = '> '


class Bowling(object):
    """Bowling game. The class takes care of adding the users and running the game"""

    def __init__(self, game):
        self.game = game
        self.players = []

    def add_player(self, name):
        if any(name == p.name for p in self.players):
            print "There is a player with this name in the game already. Please, choose a different name."
        else:
            p = Player(name)
            self.players.append(p)
            print "Player " + name + " added!"

    @property
    def players_participating(self):
        return len(self.players)

    def print_frame_heading(self):
        print("\n===============================================================")
        print "FRAME {0}".format(self.game._frame_index)
        print("-----------------------------------------------------------------")

    def print_frame_heading(self):
        print("\n===============================================================" )
        print "FRAME {0}".format(self.game._frame_index)
        print("---------------------------------------------------------------" )


    def play(self):
        # making sure input works for Python 3 (converting to raw_input)
        try:
            input = raw_input
        except NameError:
            pass

        while self.players_participating < 6:
            i = input("Enter player's name (or press Enter to quit): " + prompt)
            if not i:
                break
            self.add_player(i)
        print("---------------------------------------------------------------" )
        print("Let's start the game!")

        self.print_frame_heading()
        for p in self.players:
            print p.name + "'s turn:"

    def __repr__(self):
        return '<Bowling> players {}'.format(
            self.players
        )

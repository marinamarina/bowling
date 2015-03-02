from sys import argv
from .player import Player
from .game import Game

prompt = '> '


class Bowling(object):
    """Bowling game. The class takes care of adding the users and running the game"""

    def __init__(self):
        self.players = []
        self.frame_index = 1

    def add_player(self, name):
        if any(name == p.name for p in self.players):
            print "There is a player with this name in the game already. Please, choose a different name."
        else:
            p = Player(name, Game())
            self.players.append(p)
            print "Player " + name + " added!"

    @property
    def players_participating(self):
        return len(self.players)

    def print_frame_heading(self):
        print("\n===============================================================" )
        print "FRAME {0}".format(self.frame_index)
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

        for f in range(1, 11):
            for p in self.players:
                print "{0}'s turn".format(p)
                #f = 1, game_frame = 1
                #i = input("Pins: " + prompt)
                #player.game.roll(int(i))

                while f > p.game.frame_index - 1 :
                    i = input("Pins: " + prompt)
                    try:
                        p.game.roll(int(i))
                    except ValueError:
                        print "Please, do not cheat, user! This does not count ;-) Try again!"

                    if p.game.current_frame.completed:
                        break

    def __repr__(self):
        return '<Bowling> players {}'.format(
            self.players
        )

from .player import Player
from .game import Game
from term_colours import colours
from operator import attrgetter


prompt = '> '


class Bowling(object):
    """Bowling! The class takes care of adding the users and running the game"""

    def __init__(self):
        self.players = []

    def _add_player(self, name):
        if any(name == p.name for p in self.players):
            print "There is a player with this name in the game already. Please, choose a different name."
        else:
            p = Player(name, Game())
            self.players.append(p)
            print "Player " + name + " added!"

    def _print_frame_heading(self, player, frame_index):
        print colours.OKBLUE + \
                "\n{0}'s turn. Frame {1}".format(player, frame_index)\
                + colours.ENDC\


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
            self._add_player(i)
        print("---------------------------------------------------------------" )
        print (colours.UNDERLINE + colours.HEADER + "\nLet's start the game!\n" \
                              + colours.ENDC)

        for f in range(1, 11):
            for p in self.players:
                self._print_frame_heading(p, f)

                #f = 1, game_frame = 1
                while f > p.game.frame_index - 1:
                    i = input(colours.BOLD + colours.OKBLUE + "Pins: " + prompt + colours.ENDC)
                    try:
                        p.game.roll(int(i))
                        print f, p.game.frame_index
                    except ValueError:
                        print (colours.ERROR + "\nPlease, do not cheat, user! This does not count ;-) Try again!\n"\
                               + colours.ENDC)

                    if p.game.current_frame.completed:
                        p.score = p.game.total_score
                        break

    @property
    def players_participating(self):
        return len(self.players)

    def __repr__(self):
        winner = max(self.players, key=attrgetter('score'))
        winner_score = winner.score

        return '<Bowling> players {0}.\nWinner is: {1} with a total score of {2}!'.format(
            self.players,
            winner,
            winner_score
        )
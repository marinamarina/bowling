import unittest
from bowling.game import Game

# python -m unittest discover


class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_add_frame(self):
        self.game.roll(2)
        self.game.roll(8)
        self.game.roll(3)
        self.game.roll(3)
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(6)
        self.game.roll(3)
        print self.game

    def test_only_10_frames_allowed(self):
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(7)
        print self.game

    def test_only_10_pins_per_frame(self):
        self.game.roll(1)
        try:
            self.game.roll(10)
        except ValueError as e:
            print ("Wrong number entered, please enter a different number of pins!")

        self.game.roll(2)
        print self.game

    def test_only_10_pins_per_roll(self):
        try:
            self.game.roll(11)
        except ValueError as e:
            print ("There should be 0 to 10 pins per roll!")

        self.game.roll(2)
        print self.game

    def test_calculate_game_score(self):
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(2)
        self.assertEqual(self.game.calculate_game_score()[-1], 46, "Cumulated score for the three frames")

        self.assertEqual(len(self.game.calculate_game_score()), 3, "Three frames in that game")


    def roll_many(self, pins, times):
        for t in range(0, times + 1):

            self.game.roll(pins)

    def test_perfect_game(self):
        pass
        #print self.game.calculate_game_score()
        #self.assertEqual(self.game.calculate_game_score(), 300)

        print self.game
        print self.game.calculate_game_score()

    def tearDown(self):
        self.game = None
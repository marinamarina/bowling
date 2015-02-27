import unittest
from bowling.game import Game

# python -m unittest discover


class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_add_frame(self):
        self.game.roll(2)
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(3)
        self.game.roll(10)
        self.game.roll(3)
        print self.game


    """def test_all_ones(self):
        self.game.roll_many(3, 20)

        self.assertEqual(self.game.score(), 60)
        print self.game

    def test_one_strike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.game.roll_many(0, 17)
        self.assertEqual(self.game.score(), 24)
        print self.game

    def test_one_spare(self):
        self.game.roll(6)
        self.game.roll(4)
        self.game.roll(3)
        self.game.roll_many(0, 17)
        self.assertEqual(self.game.score(), 16)
        print self.game

    def test_roll_many(self):
        #self.assertTrue()
        print("----TESTING ROLL MANY-----")
        self.game.roll_many(1, 20)
        print self.game


    def test_perfect_game(self):
        self.game.roll_many(10, 12)
        self.assertEqual(self.game.score(), 300)
        print self.game"""

    def tearDown(self):
        self.game = None
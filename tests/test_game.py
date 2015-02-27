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
        except Exception as e:
            print ("Wrong number entered, please enter a different number of pins!")

        self.game.roll(2)
        print self.game

    def test_only_10_pins_per_roll(self):
        try:
            self.game.roll(11)
        except Exception as e:
            print ("There should be 0 to 10 pins per roll!")

        self.game.roll(2)
        print self.game


    def test_calculate_score(self):
        self.game.roll(2)
        self.game.roll(8)
        self.game.roll(3)
        self.game.roll(3)
        print "This is the game"
        print self.game
        print self.game.calculate_score()

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
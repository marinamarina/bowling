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

    def test_only_10_pins_per_frame(self):
        self.game.roll(1)
        try:
            self.game.roll(10)
        except ValueError as e:
            self.assertTrue(self.game._frames[-1].frame_score == 1, "Invalid roll has been ignored")

        self.game.roll(2)
        self.assertTrue(self.game._frames[-1].frame_score == 3, "Invalid roll has been ignored")

    def test_only_10_pins_per_roll(self):
        try:
            self.game.roll(11)
        except ValueError as e:
            self.assertTrue(self.game._frames[-1].frame_score == 0, "Invalid roll has been ignored")

        self.game.roll(2)
        self.assertTrue(self.game._frames[-1].frame_score == 2, "Invalid roll has been ignored")

    def test_calculate_game_score(self):
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(2)
        self.assertEqual(self.game.calculate_game_score()[-1], 46, "Cumulated score for the three frames in the game")

        self.assertEqual(len(self.game.calculate_game_score()), 3, "Three frames in that game")

    def test_last_frame_spare(self):
        self.roll_many(0,18)
        self.game.roll(1)
        self.game.roll(9)
        self.game.roll(9)
        self.assertEqual(len(self.game._frames), 10, "Ten frames in that game")
        self.assertTrue(len(self.game._frames[-1].rolls) == 3, "Last frame's length is 3")
        self.assertTrue(self.game._frames[-1].is_spare, "Last frame is spare")
        print self.game._frames[-1].is_spare

        from pprint import pprint
        pprint(self.game)

    def test_last_frame_strike(self):
        self.roll_many(0,18)
        self.game.roll(10)
        self.game.roll(9)
        self.game.roll(9)
        self.assertEqual(len(self.game._frames), 10, "Ten frames in that game")
        self.assertTrue(len(self.game._frames[-1].rolls) == 3, "Last frame's length is 3")
        self.assertTrue(self.game._frames[-1].is_strike, "Last frame is strike")
        print self.game._frames[-1].is_strike

        from pprint import pprint
        pprint(self.game)

    @unittest.skip("skip")
    def test_perfect_game(self):
        pass
        #print self.game.calculate_game_score()
        #self.assertEqual(self.game.calculate_game_score(), 300)

        print self.game
        print self.game.calculate_game_score()

    def roll_many(self, pins, times):
        for t in range(0, times):

            self.game.roll(pins)

    def tearDown(self):
        self.game = None
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

    @unittest.skip("")
    def test_calculate_game_score(self):
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(2)
        self.assertEqual(self.game.calculate_frame_score()[-1], 46, "Cumulated score for the three frames in the game")

        self.assertEqual(len(self.game.calculate_frame_score()), 3, "Three frames in that game")

    def test_last_frame_spare(self):
        self.roll_many(0,18)
        self.game.roll(1)
        self.game.roll(9)
        self.game.roll(9)
        self.assertEqual(len(self.game._frames), 10, "Ten frames in that game")
        self.assertTrue(len(self.game._frames[-1].rolls) == 3, "Last frame's length is 3")
        self.assertTrue(self.game._frames[-1].is_spare, "Last frame is spare")

    def test_last_frame_strike(self):
        self.roll_many(0,18)
        self.game.roll(10)
        self.game.roll(9)
        self.game.roll(9)
        self.assertEqual(len(self.game._frames), 10, "Ten frames in that game")
        self.assertTrue(len(self.game._frames[-1].rolls) == 3, "Last frame's length is 3")
        self.assertTrue(self.game._frames[-1].is_strike, "Last frame is strike")

    @unittest.skip("")
    def test_frame_score_spare(self):
        self.game.roll(1)
        self.game.roll(9)
        self.game.calculate_frame_score()

        self.game.roll(1)
        self.game.roll(1)
        self.game.calculate_frame_score()

        self.game.roll(1)
        self.game.roll(9)
        self.game.calculate_frame_score()
        self.assertEqual(self.game._scoreboard[-1], 23, "Last frame cumulated score")

        self.game.roll(1)
        self.game.roll(9)
        self.game.calculate_frame_score()
        self.assertEqual(self.game._scoreboard[0], 11, "First frame cumulated score")
        self.assertEqual(self.game._scoreboard[1], 13, "Second frame cumulated score")
        self.assertEqual(self.game._scoreboard[2], 24, "Third frame cumulated score")
        self.assertEqual(self.game._scoreboard[3], 34, "Last frame cumulated score")

    def test_frame_score_strike(self):
        self.game.roll(10)
        self.game.calculate_frame_score()
        print self.game

        self.game.roll(10)
        self.game.calculate_frame_score()
        print self.game

        self.game.roll(10)
        self.game.calculate_frame_score()
        print self.game


        self.game.roll(10)
        self.game.calculate_frame_score()
        print self.game

        self.game.roll(10)
        self.game.calculate_frame_score()
        print self.game


        self.game.roll(10)
        self.game.calculate_frame_score()
        print self.game

        self.game.roll(9)
        self.game.roll(1)
        self.game.calculate_frame_score()
        print self.game

        self.game.roll(2)
        self.game.roll(1)
        self.game.calculate_frame_score()
        print self.game



    def test_perfect_game(self):
        self.roll_many(10,12)
        self.game.calculate_frame_score()
        print self.game
        #self.assertEqual(self.game.calculate_game_score(), 300)

    def roll_many(self, pins, times):
        for t in range(0, times):
            self.game.roll(pins)

    def tearDown(self):
        self.game = None
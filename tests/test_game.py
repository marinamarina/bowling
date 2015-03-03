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
            self.assertTrue(self.game.current_frame.frame_score == 1, "Invalid roll has been ignored")

        self.game.roll(2)
        self.assertTrue(self.game.current_frame.frame_score == 3, "Invalid roll has been ignored")

    def test_only_10_pins_per_roll(self):
        try:
            self.game.roll(11)
        except ValueError as e:
            self.assertTrue(self.game.current_frame.frame_score == 0, "Invalid roll has been ignored")

        self.game.roll(2)
        self.assertTrue(self.game.current_frame.frame_score == 2, "Invalid roll has been ignored")

    def test_frame_length(self):
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(2)
        self.assertEqual(self.game._frame_index, 3, "Three frames in that game")

    def test_frame_score_spare(self):
        self.game.roll(1)
        self.game.roll(9)
        self.assertEqual(self.game.scoreboard[0], '-', "First frame, no score yet! Waiting for the bonus...")

        self.game.roll(1)
        self.game.roll(1)
        self.assertEqual(self.game.scoreboard[0], 11, "First frame score updated, with added bonus")
        self.assertEqual(self.game.scoreboard[1], 13, "Second frame cumulated score")

        self.game.roll(1)
        self.game.roll(9)
        self.assertEqual(self.game.scoreboard[0], 11, "First frame score")
        self.assertEqual(self.game.scoreboard[1], 13, "Second frame score")
        self.assertEqual(self.game.scoreboard[2], '-', "Third frame, no score yet! Waiting for the bonus...")

        self.game.roll(1)
        self.game.roll(9)
        self.assertEqual(self.game.scoreboard[0], 11, "First frame score")
        self.assertEqual(self.game.scoreboard[1], 13, "Second frame score")
        self.assertEqual(self.game.scoreboard[2], 24, "Third frame, score with the added bonus")
        self.assertEqual(self.game.scoreboard[3], '-', "Fourth frame, score with the added bonus")

    def test_last_frame_spare(self):
        self.roll_many(0, 18)
        self.game.roll(1)
        self.game.roll(9)
        self.game.roll(9)
        # dummy roll that would not be added due to validation
        self.game.roll(9)
        self.assertEqual(len(self.game._frames), 10, "There are ten frames in that game")
        self.assertTrue(len(self.game.current_frame.rolls) == 3, "Last frame's length is 3")
        self.assertTrue(self.game.current_frame.is_spare, "Last frame is spare")
        self.assertEqual(self.game.scoreboard[-1], 19, "Last frame score is calculated correctly")
        self.assertTrue(self.game.completed, "Game has been completed")

    def test_frame_score_strike(self):
        self.game.roll(0)
        self.game.roll(0)
        self.roll_many(10,9)
        self.roll_many(3,2)
        # dummy roll that would not be added due to validation
        self.game.roll(9)
        self.assertEqual(self.game.scoreboard[-1], 249, "Last frame score")

    def test_perfect_game(self):
        self.roll_many(10,12)
        self.assertEqual(self.game.scoreboard[-1], 300)

    def test_another_one(self):
        try:
            self.game.roll(90)
        except ValueError:
            print "Bad user!"

        self.game.roll(1)
        self.game.roll(3)
        print "THIS IS IT"
        print self.game

        #self.assertEqual(self.game.scoreboard[0], '-', "First frame, no score yet! Waiting for the bonus...")


    def roll_many(self, pins, times):
        for t in range(0, times):
            self.game.roll(pins)

    def tearDown(self):
        self.game = None
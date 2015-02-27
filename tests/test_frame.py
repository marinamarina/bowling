import unittest
from bowling.game import Frame

# python -m unittest discover


class FrameTest(unittest.TestCase):
    def setUp(self):
        self.frame = Frame()

    def test_completed(self):
        self.assertFalse(self.frame.completed, "The frame has not been completed")

        self.frame.roll_once(1)

        self.assertFalse(self.frame.completed, "The frame has not been completed")

        self.frame.roll_once(8)

        self.assertTrue(self.frame.completed, "The frame has been completed")
        print self.frame.rolls, "The frame has been completed"

    def test_frame_score(self):
        self.frame.roll_once(1)
        self.frame.roll_once(2)
        self.assertEqual(self.frame.frame_score, 3, "Frame score")
        self.assertTrue(self.frame.completed, "The frame has been completed")
        print self.frame.rolls, "The frame sum is {}".format(self.frame.frame_score)

    def test_is_strike(self):
        self.frame.roll_once(10)
        self.assertTrue(self.frame.is_strike, "This is strike")
        self.assertTrue(self.frame.completed, "The frame has been completed")
        print self.frame.rolls, "The frame has been completed ans is strike"

    def test_is_spare(self):
        self.frame.roll_once(1)
        self.frame.roll_once(9)
        self.assertTrue(self.frame.is_spare, "This is spare")
        self.assertTrue(self.frame.completed, "The frame has been completed")
        print self.frame.rolls, "The frame has been completed and is a spare"

    def tearDown(self):
        self.frame = None


    def tearDown(self):
        self.game = None
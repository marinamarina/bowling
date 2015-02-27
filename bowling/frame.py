from collections import namedtuple
#roll, frame, scoreboard


class Frame(object):
    """Represents a frame in the game of bowling"""

    def __init__(self, frame_index=0):

        self.rolls = []
        self.score = 0
        self.frame_index = frame_index

    def roll_once(self, pins):
        """Roll once!"""
        self.rolls.append(pins)

    '''def strike_score(self):
        return self.frame_score +'''

    @property
    def completed(self):
        return sum(self.rolls) == 10 or len(self.rolls) == 2

    @property
    def frame_score(self):
        """
        :rtype: int
        :return: Returns total score for the frame
        """
        return sum(self.rolls)

    @property
    def is_strike(self):
        """
        :rtype: bool
        :return: True if the frame is a strike
        """
        return len(self.rolls) == 1 and self.frame_score == 10

    @property
    def is_spare(self):
        """
        :rtype: bool
        :return: True if the frame is a spare
        """
        return len(self.rolls) == 2 and self.frame_score == 10

    @property
    def is_miss(self):
        """
        :rtype: bool
        :return: True if the frame is a miss (no pins have been knocked down)
        """
        return self.frame_score == 0

    def __repr__(self):
        return '<Frame> rolls: {}'.format(
            self.rolls
            )
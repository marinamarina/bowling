class Frame(object):
    """Represents a frame in a game of ten-pin bowling"""

    def __init__(self):
        self.rolls = []
        self.score = 0

    def roll_once(self, pins):
        """Roll it!"""
        if pins > 10:
                raise ValueError("Pins in a single throw exceed 10")
        else:
            self.rolls.append(pins)

    @property
    def is_last(self):
        return False

    @property
    def completed(self):
        """
        :rtype: bool
        :return: Returns true if the frame was completed
        """
        return sum(self.rolls) == 10 or len(self.rolls) == 2


    @property
    def frame_score(self):
        """
        :rtype: int
        :return: Returns total score for the frame
        """
        return sum(self.rolls[0:2])

    @property
    def is_strike(self):
        """
        :rtype: bool
        :return: True if the frame is a strike
        """
        return self.completed and self.rolls[0] == 10

    @property
    def is_spare(self):
        """
        :rtype: bool
        :return: True if the frame is a spare
        """
        return self.completed and sum(self.rolls[0:2]) == 10

    def __repr__(self):
        return '<Frame> rolls : {}'.format(
            self.rolls
        )
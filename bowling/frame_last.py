from .frame import Frame

class FrameLast(Frame):
    """Represents the 10th frame in a game of ten-pin bowling"""

    def __init__(self):
        self.rolls = []
        self.score = 0

    @property
    def is_last(self):
        return True

    @property
    def length(self):
        return len(self.rolls)

    @Frame.frame_score.getter
    def frame_score(self):
        """
        :rtype: int
        :return: Returns total score for the frame
        """
        if self.is_strike:
            return 10
        return super(FrameLast, self).frame_score


    @Frame.completed.getter
    def completed(self):
        """
        :rtype: bool
        :return: Returns true if the frame was completed
        """
        if sum(self.rolls[0:2]) < 10:
            # standard frame
            return self.length == 2

        elif self.length == 3 and sum(self.rolls[0:2]) == 10:
            # spare
            return True

        if self.length == 3 and self.rolls[0] == 10:
            # strike
            return True

    def __repr__(self):
        return '<FrameLast> rolls: {}'.format(
            self.rolls
            )
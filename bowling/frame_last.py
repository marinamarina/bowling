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

    @Frame.completed.getter
    def completed(self):

        if sum(self.rolls[0:2]) < 10:
            return self.length == 2

        elif self.length == 3 and sum(self.rolls[0:2]) == 10:
            return True

        if self.length == 3 and self.rolls[0] == 10:
            return True

    def __repr__(self):
        return '<FrameLast> rolls: {}'.format(
            self.rolls
            )
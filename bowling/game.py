from .frame import Frame
from .frame_last import FrameLast
from pprint import pprint


class Game(object):
    """Represents a game of ten-pin bowling"""

    def __init__(self):
        #start with one frame in the list
        self._frames = [self._add_frame()]
        self._max_frame_count = 10
        self._frame_index = 1
        self._scoreboard = []

    def _add_frame(self):
        return Frame()

    def _add_last_frame(self):
        return FrameLast()

    def update_scoreboard(func):
        """
        Decorator that ensures the scoreboard is updated after the end of each frame
        :param func: calculate_frame_score()
        :return: wrapper
        """

        def wrapper(self, *args):
            #do something before the roll
            func( self, *args)
            # update the scoreboard ONLY once the frame has been completed
            if self._frames[-1].completed:
                # calculate score after the end of each frame
                self.calculate_frame_score()
        return wrapper

    @update_scoreboard
    def roll(self, pins):

        # f is the last frame from the list of frames
        f = self._frames[-1]

        # only 10 frames allowed
        if self._frame_index == self._max_frame_count and self._frames[-1].completed:
            return True

        if not f.completed:

            if not f.is_last and pins + f.frame_score > 10:
                raise ValueError("Frame pins summary exceeds 10")

            if pins > 10:
                raise ValueError("Pins in a single throw exceed 10")

            #if f.is_last and f.is_spare:

            f.roll_once(pins)
            self._frames[-1] = f
        else:
            f = self._add_last_frame() if self._frame_index == self._max_frame_count - 1 else self._add_frame()

            f.roll_once(pins)
            self._frames.append(f)
            # increment the frame index
            self._frame_index += 1

    def bonus(self, frame, following_rolls, pos):
        if following_rolls:
            if frame.is_strike:
                return self.strike_bonus(following_rolls)
            elif frame.is_spare:
                print "2"
                return self.spare_bonus(following_rolls)
            else:
                return 0
        else:
            return 0

    def spare_bonus(self, following_rolls):
        return following_rolls[0]

    def strike_bonus(self, following_rolls):
        return following_rolls[0] + following_rolls[1]

    def calculate_frame_score(self):
        # creating list of lists from the list of frames
        game_rolls2d = [f.rolls for f in self._frames]
        self._scoreboard = []

        for f_index, f in enumerate(self._frames):


            following_rolls_2d = game_rolls2d[f_index + 1:]
            following_rolls_flat = sum(following_rolls_2d, [])

            bonus = 0
            f_score = f.frame_score
            prev_score = self._scoreboard[-1] if self._scoreboard else 0

            if f.is_last:
                bonus =  f.rolls[-1]


            if f.is_spare:
                bonus = following_rolls_flat[0] if following_rolls_flat else 0

            if not f.is_strike and not f.is_spare:
                bonus = 0

            # do not display the score until it is possible to calculate the bonus

            if f.is_strike:

                try:
                    bonus = sum(f.rolls[-2::]) if f.is_last else following_rolls_flat[0] + following_rolls_flat[1]
                    self._scoreboard.append(f_score + prev_score + bonus)

                except IndexError:
                    self._scoreboard.append("-")
            elif f.is_spare:
                try:
                    bonus = f.rolls[-1] if f.is_last else following_rolls_flat[0]
                    self._scoreboard.append(f_score + prev_score + bonus)
                except IndexError:
                    self._scoreboard.append("-")
            else:
                self._scoreboard.append(f_score + prev_score + bonus)

    def __repr__(self):
        return '<Game> frames: {0} Frame Index: {1} \nScoreboard: {2} \n'.format(
            [f.rolls for f in self._frames],
            self._frame_index,
            self._scoreboard
        )


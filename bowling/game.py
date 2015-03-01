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

    def _score_decorator(func):

        def wrapper(self, *args):
            #do something before the roll
            func( self, *args)
            #do something after the roll
            if self._frames[-1].completed:
                # dummy score
                # TODO calculate real score
                self._scoreboard.append(1)
        return wrapper

    @_score_decorator
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

    # TODO output symbols strike/spare, etc.
    def calculate_frame_score(self):
        results = []

        # creating list of lists from the list of frames
        game_rolls2d = [f.rolls for f in self._frames]
        prev_score = results[-1] if results else 0

        # frames so far
        for f_index, f in enumerate(self._frames):
            f_score = f.frame_score
            results.append(prev_score + f_score)

        return results

    def calculate_game_score(self):
        results = []

        # creating list of lists from the list of frames
        game_rolls2d = [f.rolls for f in self._frames]
         # that's how I can get the frame number, no need to store it in fields?
        for f_index, f in enumerate(self._frames):

            f_score = f.frame_score
            following_frames_2d = game_rolls2d[f_index + 1:]
            following_frames_flat = sum(following_frames_2d, [])

        # that's how I can get the frame number, no need to store it in fields?
        for f_index, f in enumerate(self._frames):

            f_score = f.frame_score
            following_frames_2d = game_rolls2d[f_index + 1:]
            following_frames_flat = sum(following_frames_2d, [])

            if f.is_strike:
                bonus = following_frames_flat[0] + following_frames_flat[1]
            elif f.is_spare:
                bonus = following_frames_flat[0]
            else:
                bonus = 0

            prev_score = results[-1] if results else 0

            results.append(prev_score + f_score + bonus)
        return results

    def __repr__(self):
        return '<Game> frames: {0} Frame Index: {1} \n Scoreboard: {2} \n'.format(
            [f.rolls for f in self._frames],
            self._frame_index,
            self._scoreboard
        )


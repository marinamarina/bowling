from .frame import Frame
from pprint import pprint


class Game(object):
    """Represents a game of ten-pin bowling"""

    def __init__(self):
        #start with one frame in the list
        self._frames = [self._add_frame()]

        self._max_frame_count = 10
        self._frame_index = 1
        self._current_frame = self._frames[-1]

    def _add_frame(self):
        return Frame()

    def roll(self, pins):
        # f is the last frame from the list of frames
        f = self._frames[-1]

        # only 10 frames allowed
        if self._frame_index == 10 and self._frames[-1].completed:
            return True

        if not f.completed:
            print 'Frame not completed'

            if pins + f.frame_score > 10:
                raise ValueError("Frame pins summary exceeds 10")

            if pins > 10:
                raise ValueError("Pins in a single throw exceed 10")

            f.roll_once(pins)
            self._frames[-1] = f
        else:
            print 'Completed, add a new frame'
            f = Frame()
            f.roll_once(pins)
            self._frames.append(f)
            # increment the frame index
            self._frame_index += 1


    # TODO record results in a cumulative way
    # output symbols strike/spare, etc.

    def calculate_game_score(self):

        results = []

        # creating list of lists from the list of frames
        game_rolls2d = [f.rolls for f in self._frames]

        # flattenning the rolls 2d list
        game_rolls = sum(game_rolls2d, [])

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

    # main method
    def play(self):
        self.roll_once(4)

    def __repr__(self):
        return '<Game> frames: {0} Frame Index: {1} \n'.format(
            self._frames,
            self._frame_index
            )
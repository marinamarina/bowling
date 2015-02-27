from .frame import Frame
from pprint import pprint


class Game(object):

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
        if self._frame_index == 10:
            return True

        if not f.completed:
            print 'Frame not completed'

            if pins + f.frame_score > 10:
                raise Exception("Frame pins summary exceeds 10")

            if pins > 10:
                raise Exception("Pins in a single throw exceed 10")

            f.roll_once(pins)
            self._frames[-1] = f
        else:
            print 'Completed, add a new frame'
            f = Frame()
            f.roll_once(pins)
            self._frames.append(f)
            # increment the frame index
            self._frame_index += 1

    def calculate_score(self):

        results = []

        # that's how i can get the frame number, no need to store it in fields?
        for frame_index, frame in enumerate( self._frames):
            frame_score = 0
            if frame.is_strike:
                results.append('X')
            elif frame.is_spare:
                results.append('/')
            else:
                results.append(frame.frame_score)

        return results

    # main method
    def play(self):
        self.roll_once(4)

    def __repr__(self):
        return '<Game> frames: {0} Frame Index: {1}'.format(
            self._frames,
            self._frame_index
            )

from .frame import Frame
from pprint import pprint

class Game(object):

    def __init__(self):

        #self._initial_frame = Frame()
        self._frames = [self._add_frame()]
        self._max_frame_count = 10
        self._frame_index = 1
        self._current_frame = self._frames[-1]

    def _add_frame(self):
        return Frame()

    # TODO:
    # create a new frame every time

    def roll(self, pins):
        # f is the last frame from the list of frames
        f = self._frames[-1]
        if not f.completed:
            print 'Not completed'
            f.roll_once(pins)
            self._frames[-1] = f

        else:
            print 'Completed, add a new frame'
            f = Frame()
            f.roll_once(pins)
            self._frames.append(f)
            # increment the frame index
            self._frame_index += 1

    def play(self):
        #create a new frame?

        self.roll_once(4)

    def __repr__(self):
        return '<Game> frames: {}, total score:  points'.format(
            self._frames
            )
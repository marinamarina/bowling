class Roll(object):

    def __init__(self, roll):
        self.pins = None
        self.next_roll = roll;

    def is_played(self):
        return True if self.pins is not None else False


    @property
    def pins (self):
        return self.pins

    @pins.setter
    def pins (self, value):
        self.pins = value

    def next_roll(self):
        if self.next_roll is None:
            return None

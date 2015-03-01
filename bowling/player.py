class Player(object):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, turn):
        if type(turn) is int:
            self._turn = turn
        else:
            raise TypeError('{0} should be an integer!'.format(turn))

    def __repr__(self):
        return '<Player> name: {0}'.format(
            self.name
        )

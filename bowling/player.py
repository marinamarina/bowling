class Player(object):

    def __init__(self, name):
        self._name = name
        self._final_score = 0

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

    @property
    def final_score(self):
        return self._final_score

    def __repr__(self):
        return '<Player> name: {0}, final_score: {1}'.format(
            self.name,
            self._final_score
        )

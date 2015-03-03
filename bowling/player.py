class Player(object):
    """Represent a player in the bowling game"""

    def __init__(self, name, game):
        self._name = name
        self._score = 0
        self._game = game

    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, v):
        self._score = v

    @property
    def game(self):
        return self._game

    def __repr__(self):
        return '{0}'.format(
            self.name
        )
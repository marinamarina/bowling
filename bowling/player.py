class Player(object):
     def __init__(self, name, turn):

        #self._initial_frame = Frame()
        self.name = name
        self.turn = turn
        self.final_score = 0

     def __repr__(self):
        return '<Player> name: {0}, final_score: {1}'.format(
            self.name,
            self.final_score
            )

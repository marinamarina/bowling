from bowling.game import Game
from bowling.bowling import Bowling


def main():
    g = Game()
    b = Bowling(g)
    b.play()
    print b

if __name__ == '__main__':
    main()
import argparse
from bowling.game import Game


def main():
    #parser = argparse.ArgumentParser()
    #parser.add_argument('-r', default=ex)
    #namespace = parser.parse_args(sys.argv[1:])

    game = Game()
    #result = game.get_final_result()
    game.play()

    print game

if __name__ == '__main__':
    main()
from game import GameOfLife
from constants import BLOCK, BLINKER, RPENTOMINO


def main():
    game = GameOfLife(RPENTOMINO, board_size=(1000, 1000), shift=30)
    game.play()


if __name__ == "__main__":
    main()

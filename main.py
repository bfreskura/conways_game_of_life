from game import GameOfLife
from constants import BLOCK, BLINKER, RPENTOMINO


def main():
    b = 1000
    game = GameOfLife(RPENTOMINO, board_size=(b, b), shift=b // 2)
    game.play()


if __name__ == "__main__":
    main()

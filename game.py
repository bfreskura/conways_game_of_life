from itertools import combinations
import time

ALIVE = "+"
DEAD = "."

class GameOfLife:
    def __init__(self, pattern, board_size = (50, 50), center = (0, 0)):
        self.center = center
        self.active = pattern
        self.board = [[DEAD for j in range(board_size[0])] for i in
                       range(board_size[1])]
        for x, y in pattern:
            self.board[x][y] = ALIVE


    def update(self):
        # TODO add dead cells which have alive cells around them
        change = [self.apply_rules(x, y) for x, y in self.active]
        for x, y, s in change:
            self.board[x][y] = s

        self.display()
        time.sleep(1)


    def apply_rules(self, x, y):
        neigh = [(0,1), (1,0), (0, -1), (-1, 0)]
        alive = [(x + i, y + j) for i, j in neigh if self.board[x + i][y + j]
                 == ALIVE]

        if (len(alive) < 2 or len(alive) > 3) and self.board[x][y] == ALIVE:
            self.active.remove((x, y))
            return (x, y, DEAD)

        elif self.board[x][y] == DEAD and len(alive) == 3:
            self.active.append((x, y))
            return (x, y, ALIVE)
        else:
            self.active.append((x, y))
            return (x, y, ALIVE)



    def display(self):
        """
        Displays the current game status
        """

        # TODO Render only board around alive +- padding
        [print(' '.join(row)) for row in self.board]


    def play(self):
      while True:
         self.update()



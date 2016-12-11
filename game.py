import time

from constants import ALIVE, DEAD


class GameOfLife:
    def __init__(self, pattern, board_size=(500, 500), shift=0):
        """
        :param pattern: Seed pattern (list of (x,y) coordinates)
        :param board_size: Tuple of x and y dimensions
        :param shift:
        """
        self.board_size_x = board_size[0]
        self.board_size_y = board_size[1]
        self.board = [[DEAD for _ in range(board_size[0])] for _ in
                      range(board_size[1])]
        pattern = [(x + shift, y + shift) for x, y in pattern]
        for x, y in pattern:
            self.board[x][y] = ALIVE

    def update(self, frequency=1):
        """

        :param frequency: Update frequency in seconds
        :return:
        """
        change = []
        max_x, max_y, min_x, min_y = self.find_limits(1)

        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                change.append(self.apply_rules(x, y))

        for x, y, s in change:
            self.board[x][y] = s

        self.display()
        time.sleep(frequency)

    def apply_rules(self, x, y):
        neigh = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1),
                 (-1, 1)]

        alive = []
        for i, j in neigh:
            h = (x + i) < self.board_size_x and (y + j) < self.board_size_y
            l = (x + i) >= 0 and (y + j) >= 0
            if h and l:
                if self.board[x + i][y + j] == ALIVE:
                    alive.append((x, y))

        # Rules 1 and 2
        if (len(alive) < 2 or len(alive) > 3) and self.board[x][y] == ALIVE:
            return x, y, DEAD

        # Rule 3
        elif self.board[x][y] == ALIVE and (len(alive) == 2 or len(alive) == 3):
            return x, y, ALIVE

        # Rule 4
        elif self.board[x][y] == DEAD and len(alive) == 3:
            return x, y, ALIVE

        # Unchanged cell
        else:
            return x, y, self.board[x][y]

    def find_limits(self, padding=1):
        """
        Searches for an active area of board with some padding
        :return: Minimum and maximum coordinates of an active area
        """
        max_x, max_y = 0, 0
        min_x, min_y = self.board_size_x, self.board_size_y
        for x in range(self.board_size_x):
            for y in range(self.board_size_y):
                if self.board[x][y] == ALIVE:
                    max_x = max(max_x, x)
                    max_y = max(max_y, y)
                    min_x = min(min_x, x)
                    min_y = min(min_y, y)

        # Adjust for padding
        max_x = min(max_x + padding, self.board_size_x)
        max_y = min(max_y + padding, self.board_size_y)
        min_x = max(min_x - padding, 0)
        min_y = max(min_y - padding, 0)

        return max_x, max_y, min_x, min_y

    def display(self, padding=5):
        """
        Displays the current game status
        """
        max_x, max_y, min_x, min_y = self.find_limits(padding)
        new_board = [[self.board[x][y] for y in range(min_y, max_y)] for x in
                     range(min_x, max_x)]

        [print(' '.join(row)) for row in new_board]
        print("= " * len(new_board[0]))

    def play(self):
        iteration = 0
        while True:
            self.update(frequency=0.5)
            iteration += 1

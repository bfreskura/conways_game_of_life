# Conway's game of life

## Rules
The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead. Every cell interacts with its eight neighbours, which are the cells that are directly horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:
* Any live cell with fewer than two live neighbours dies (referred to as underpopulation or exposure[1]).
* Any live cell with more than three live neighbours dies (referred to as overpopulation or overcrowding).
* Any live cell with two or three live neighbours lives, unchanged, to the next generation.
* Any dead cell with exactly three live neighbours will come to life.

The initial pattern constitutes the 'seed' of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed — births and deaths happen simultaneously, and the discrete moment at which this happens is sometimes called a tick. (In other words, each generation is a pure function of the one before.) The rules continue to be applied repeatedly to create further generationsfe

## Requirements
* Python3

## Adding custom seeds
To add a custom seed open `constants.py` and add a new seed constant with starting coordinates. E.g.:
`MY_SEED = [(1, 0), (2, 0), (1, 1), (1, 2), (0, 1)]`


In `main.py` you can then import the constant and use it as a starting seed of the game like this:
```
from constants import MY_SEED
...
game = GameOfLife(MY_SEED, board_size=(b, b), shift=b // 2)
...
```
